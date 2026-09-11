# **How MCP works?**
![MCP Architeture](mcp.png)

# 🧠 MCP Demo

One hands-on MCP integration, kept deliberately small so it can be shown live
in a training session without a database or third-party account beyond your
OpenAI key.

| Folder | Description | Key Features |
|--------|-------------|---------------|
| **`Meeting_Scheduler_MCP_Demo`** | An MCP server exposing `check_availability` and `book_meeting` tools over a small mocked in-memory calendar, called by a Gradio chatbot via OpenAI function calling. | - Small, self-contained MCP server (`mcp_meeting_scheduler.py`)<br>- Gradio UI shows which tool was picked and what it returned<br>- No database or extra accounts — just your OpenAI key<br>- Recreates the module slide's own "Book a meeting with Raj tomorrow at 10 AM" example |

See `Meeting_Scheduler_MCP_Demo/How-to-Run.md` for setup steps, and its
`.env` file for which key to fill in.
