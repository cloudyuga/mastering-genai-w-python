# 🧰 Popular Tools & Frameworks

A landscape tour of the GenAI ecosystem — Gradio, HuggingFace, embeddings and
vector databases, Retrieval-Augmented Generation, and LangChain — with a
live demo built into each concept rather than a slide alone.

---

## 📊 Slides

Maintained as a Canva design ("Module 3: Popular Tools & Frameworks").
Ordered so Gradio comes first (live-demo hook), followed by HuggingFace,
vector databases, RAG, and LangChain, closing with a case study on the
Nvidia–HuggingFace acquisition.

## 🧪 Labs

### Gradio — building a UI in minutes
| Lab | Notebook | Description |
|-----|----------|-------------|
| 1 | `Lab-1-Prompt_Execution_Gradio.ipynb` | Wire a prompt up to a simple `gr.Interface`. |
| 2 | `Lab-2-Types_of_Gradio_App.ipynb` | Survey of the three Gradio app types — Interface-based, Blocks-based, and ChatInterface-based. |
| 3 | `Lab-4-Birthday_Message_Apps.ipynb` | A tiny, fun end-to-end Gradio app — multiple inputs, streaming responses, temperature control. |

### HuggingFace — the model hub
| Lab | Notebook | Description |
|-----|----------|-------------|
| 4 | `Lab-7-HuggingFace_Models.ipynb` | Tour of HuggingFace model types — sentiment/emotion classification, embeddings, text generation, NER — plus a chat-model-based stand-in for summarization, Q&A, and translation now that `transformers` v5 dropped those pipeline shortcuts. |

### Embeddings, Vector Databases & RAG
| Lab | Notebook | Description |
|-----|----------|-------------|
| 5 | `Lab-5-Chat_with_Paragraph_Embedding_Gradio.ipynb` | The simplest possible RAG demo — embed one paragraph, chat with it. |
| 6 | `Lab-6-Chat_with_PDF_Embedding_RAG.ipynb` | Upload a PDF, ask it questions — the flagship RAG demo for this module. |
| 7 | `Lab-8-Chroma_hrdataset_QA.ipynb` | RAG over the shared `hrdataset/` using a persisted ChromaDB index. |

LangChain is still covered on the slides (see below), but currently has no
dedicated lab in this module — `Lab-9-RAG_with_Langchain.ipynb` was removed.

Notebook filenames keep their original `Lab-N-*` numbering from before the
module was trimmed down to these 7 labs, so the numbers run 1, 2, 4–8 (no
`Lab-3`, no `Lab-9`) — that gap is cosmetic, not a missing file.

Several RAG labs depend on the `hrdataset/` folder at the repo root.

---
