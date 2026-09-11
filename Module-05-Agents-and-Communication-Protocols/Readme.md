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

Kept to one notebook and one MCP demo — enough to make the slide concepts
tangible without turning this into a LangGraph/MCP engineering deep-dive.

| Lab | Notebook/Folder | Description |
|-----|------------------|-------------|
| 1 | `Lab-1-Agentic_Workflow_with_Langgraph.ipynb` | A first agentic workflow with LangGraph, built up in stages: a basic LLM node, then a tool-calling agent, then conversational memory across a thread — the "augmented LLM" concept, live. |
| — | `Model-Context-Protocol/Meeting_Scheduler_MCP_Demo/` | An MCP server exposing check_availability/book_meeting tools over a small mocked calendar, called via OpenAI function calling from a Gradio UI. Recreates the "Book a meeting with Raj tomorrow at 10 AM" example already drawn on this module's own slide — live. Runs either as one Colab notebook (`Meeting_Scheduler_MCP_Demo.ipynb`) or as a separate server/client pair (`.py` files) — see `Model-Context-Protocol/Readme.MD`. |

Requires an OpenAI key for both, plus a (free) Tavily key for Lab-1's
web-search tool section. The MCP demo needs no other accounts — its
calendar is mocked in-memory.

---
