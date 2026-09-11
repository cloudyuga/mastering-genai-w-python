## SSE RUN:
### Open a terminal
- We can use venv

- Install the requirements if they're not already in your venv:

```
pip install -r requirements.txt
```

- Run the MCP server:

```
fastmcp run mcp_meeting_scheduler.py:mcp --transport sse
```
### Another terminal (split):

- Activate your venv and run:

```
python gradio_client.py
```

### Try it live

- "Check Raj's availability tomorrow"
- "Book a meeting with Raj tomorrow at 10 AM" (the exact example from the
  Module 5 slide — this one succeeds, since 10:00 is free on Raj's mock
  calendar for "tomorrow")
- "Book a meeting with Priya tomorrow at 10 AM" (this one is already taken —
  a good moment to show the model picking a different free slot instead)
