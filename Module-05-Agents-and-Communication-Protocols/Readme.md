# 🤖 Agents and Communication Protocols

What an AI agent is, how it differs from a plain chatbot, LangGraph as a way
to build agentic workflows, and the Model Context Protocol (MCP) as the
emerging standard for connecting agents to tools and data.

---

## 📊 Slides

Maintained as a Canva design ("Module 5: Agents and Communication
Protocols"). Covers agent fundamentals (perception/action, memory, planning,
degrees of autonomy), LangChain/LangGraph, MCP and why it matters now, a
real-world agent examples slide, and closes with a recap.

## 🧪 Labs

### Agent fundamentals & LangGraph
| Lab | Notebook | Description |
|-----|----------|-------------|
| 1 | `Lab-1-Agentic_Workflow_with_Langgraph.ipynb` | A first agentic workflow built with LangGraph. |
| 2 | `Lab-2-Hr_Assistant_with_Memory.ipynb` | An agent with conversational memory — the "augmented LLM" concept, live. |
| 3 | `Lab-3-Connect_LangSmith.ipynb` | Observability for agent runs via LangSmith. |
| 4 | `Lab-4-Langsmith_Langgraph_Demo.ipynb` | LangGraph + LangSmith combined. |
| — | `LangGraph/` (`LG01`–`LG11`) | A deeper, sequential set of LangGraph labs — basic concepts, ReAct agents, RAG-with-LangGraph, streaming, human-in-the-loop, multi-agent — see `LangGraph/readme.MD`. |

### Model Context Protocol (MCP)
| Folder | Description |
|--------|-------------|
| `Model-Context-Protocol/` | Seven hands-on MCP integrations — Claude Desktop, stdio, SSE, an external weather/news API, a Postgres-backed RAG agent, a Chroma-backed RAG agent, and an MCP + Zapier + Gmail agent that actually sends email. See `Model-Context-Protocol/Readme.MD` for the full breakdown. |

Several of the MCP demos require their own API keys/credentials — see the
`.env` placeholders inside each subfolder.

---
