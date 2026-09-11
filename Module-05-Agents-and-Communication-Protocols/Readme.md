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

Kept to one notebook — enough to make the slide concepts tangible without
turning this into a LangGraph/MCP engineering deep-dive.

| Lab | Notebook/Folder | Description |
|-----|------------------|-------------|
| 1 | `Lab-1-Agentic_Workflow_with_Langgraph.ipynb` | A first agentic workflow with LangGraph, built up in stages: a basic LLM node, then a tool-calling agent, then conversational memory across a thread — the "augmented LLM" concept, live. |

Requires an OpenAI key, plus a (free) Tavily key for Lab-1's web-search
tool section.

`Model-Context-Protocol/` currently has no hands-on demo — its previous
weather/news example was removed; see `Model-Context-Protocol/Readme.MD`
for status. MCP is still covered conceptually on the slides.

---
