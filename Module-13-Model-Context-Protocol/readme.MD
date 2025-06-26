# **How MCP works?**
![MCP Architeture](mcp.png)

# 🧠 MCP Labs

This module includes a collection of practical integrations of modern AI models, API services, and databases using tools like Claude, Gradio, ChromaDB, and PostgreSQL. These modules are designed to be used individually or together for rapid experimentation and prototyping.

---

## 📦 Module Overview


| Module                         | Description                                                                 | Key Features |
|-------------------------------|-----------------------------------------------------------------------------|--------------|
| **`1-Claude_Desktop_Integration`** | Integration of Claude (Anthropic) with desktop apps.                        | - Loads config from `claude_desktop_config.json`<br>- Uses MCPServer tools<br>- Ideal for local AI assistants |
| **`2-Stdio`**                     | Interactive AI assistant via standard input/output.                         | - Terminal-based chatbot with Gradio<br>- No GUI dependencies<br>- MCP server runs in background |
| **`3-SSE`**                       | Server-Sent Events (SSE) integration module.                                | - Real-time FastAPI streaming via SSE<br>- Supports `fastmcp.client` transport |
| **`4-External_API_call_for_weather_&_news`** | Uses external APIs for contextual info.                              | - Integrates weather/news APIs<br>- Outputs formatted results<br>- Useful for AI agent enhancement |
| **`5-Postgres_DB_MCP_Gradio`**   | RAG app with PostgreSQL + pgvector backend.                                 | - LangChain RAG with pgvector<br>- Gradio frontend + MCP backend<br>- Requires Postgres setup |
| **`6-RAG_MCP_Chroma_Gradio`**    | Updated RAG pipeline using **ChromaDB** instead of Postgres.                | - Gradio UI for PDF upload + QA<br>- Stores embeddings in ChromaDB<br>- Lightweight, no DB setup needed |
