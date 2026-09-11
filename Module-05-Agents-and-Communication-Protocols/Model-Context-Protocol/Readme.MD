# **How MCP works?**
![MCP Architeture](mcp.png)

# 🧠 MCP Demo

One hands-on MCP integration, kept deliberately small so it can be shown live
in a training session without a database or third-party account beyond the
API keys below.

| Folder | Description | Key Features |
|--------|-------------|---------------|
| **`Weather_News_MCP_Demo`** | An MCP server exposing a weather tool and a news tool, called by a Gradio chatbot via OpenAI function calling. | - Small, self-contained MCP server (`mcp_weather_news.py`)<br>- Gradio UI shows which tool was picked and what it returned<br>- No database — just two free API keys (OpenWeather, NewsAPI) plus your OpenAI key |

See `Weather_News_MCP_Demo/How-to-Run.md` for setup steps, and its `.env`
file for which keys to fill in.
