# **How MCP works?**
![MCP Architeture](mcp.png)

# 🧠 MCP Demo

One hands-on MCP integration, kept deliberately small so it can be shown live
in a training session without a database or third-party account beyond your
OpenAI key.

| Folder | Description | Key Features |
|--------|-------------|---------------|
| **`Meeting_Scheduler_MCP_Demo`** | An MCP server exposing `check_availability` and `book_meeting` tools over a small mocked in-memory calendar, called by a Gradio chatbot via OpenAI function calling. | - No database or extra accounts — just your OpenAI key<br>- Recreates the module slide's own "Book a meeting with Raj tomorrow at 10 AM" example |

Two ways to run it:

- **`Meeting_Scheduler_MCP_Demo.ipynb`** — everything in one Colab notebook.
  The `fastmcp` client connects directly to the in-process `FastMCP` server
  object (no separate server process, same protocol) — just run the cells
  top to bottom. Closest fit for a live training session.
- **`mcp_meeting_scheduler.py` + `gradio_client.py`** — the server and
  client as separate processes over a real SSE connection, useful if you
  want to show MCP's client/server split explicitly. See
  `Meeting_Scheduler_MCP_Demo/How-to-Run.md` for setup steps, and its
  `.env` file for which key to fill in.
