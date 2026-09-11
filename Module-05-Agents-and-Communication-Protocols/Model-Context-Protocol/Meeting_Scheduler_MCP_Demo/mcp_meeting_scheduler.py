from fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("meeting_scheduler")

WORK_HOURS = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00"]

# A small mocked calendar: person -> day -> list of already-booked "HH:MM" slots.
# Kept in-memory on purpose - this is a live demo, not a real scheduling system.
_calendar = {
    "Raj": {"today": ["10:00", "14:00"], "tomorrow": ["09:00"]},
    "Priya": {"today": ["11:00"], "tomorrow": ["10:00", "15:00"]},
    "Karan": {"today": [], "tomorrow": ["11:00", "12:00"]},
    "Neha": {"today": ["09:00", "16:00"], "tomorrow": []},
}


def _resolve_day(day: str) -> str:
    return "tomorrow" if "tomorrow" in day.strip().lower() else "today"


@mcp.tool()
def check_availability(person: str, day: str) -> str:
    """Check a colleague's free meeting slots for 'today' or 'tomorrow'."""
    person = person.strip().title()
    day_key = _resolve_day(day)

    if person not in _calendar:
        return f"I don't have a calendar for {person}. Known colleagues: {', '.join(_calendar)}."

    busy = _calendar[person][day_key]
    free = [t for t in WORK_HOURS if t not in busy]

    if not free:
        return f"{person} has no free slots {day_key}."
    return f"{person} is free {day_key} at: {', '.join(free)}"


@mcp.tool()
def book_meeting(person: str, day: str, time: str, purpose: str = "") -> str:
    """Book a meeting with a colleague at a given time on 'today' or 'tomorrow'."""
    person = person.strip().title()
    day_key = _resolve_day(day)
    time = time.strip()

    if person not in _calendar:
        return f"I don't have a calendar for {person}. Known colleagues: {', '.join(_calendar)}."
    if time not in WORK_HOURS:
        return f"{time} isn't a valid slot. Working hours are: {', '.join(WORK_HOURS)}."
    if time in _calendar[person][day_key]:
        return f"{person} is already booked at {time} {day_key}. Try a different time."

    _calendar[person][day_key].append(time)
    purpose_text = f' for "{purpose}"' if purpose else ""
    return f"Booked: meeting with {person} {day_key} at {time}{purpose_text}. Confirmation sent."


if __name__ == "__main__":
    mcp.run(transport="sse")
