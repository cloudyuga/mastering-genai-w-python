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
| 1 | `Lab-0-Prompt_Execution.ipynb` | Wire a prompt up to a simple UI. |
| 2 | `Lab-1-Types_of_Gradio_App.ipynb` | Survey of the different Gradio app types/components. |
| 3 | `Lab-2-Birthday_Message_Apps.ipynb` | A tiny, fun end-to-end Gradio app. |

### HuggingFace — the model hub
| Lab | Notebook | Description |
|-----|----------|-------------|
| 4 | `Lab-1-HuggingFace_Transformers.ipynb` | Run a pretrained model straight from the Hub. |
| 5 | `Lab-2-HuggingFace_Models.ipynb` | Browsing/using different model types on HuggingFace. |
| 6 | `Lab-3-Gradio_Feedback_Analysis.ipynb` | Combine a HuggingFace model with a Gradio front end. |

### Embeddings & Vector Databases
| Lab | Notebook | Description |
|-----|----------|-------------|
| 7 | `Lab-0-Meaning_Embedding.ipynb` | What an embedding actually captures — a visual "meaning as vectors" demo. |
| 8 | `Lab-1-Embedding_&_Similarity_Search.ipynb` | Nearest-neighbor similarity search over embeddings. |
| 9 | `Lab-2-Load_Vectorstore_from_pkl.ipynb` | Loading a persisted vector store. |

### Retrieval-Augmented Generation (RAG)
| Lab | Notebook | Description |
|-----|----------|-------------|
| 10 | `Lab-0-Chat_with_Paragraph.ipynb` | The simplest possible RAG demo — chat with one paragraph. |
| 11 | `Lab-1-Chat_with_Paragraphs.ipynb` | RAG over multiple paragraphs. |
| 12 | `Lab-2-Chat_with_PDF.ipynb` | Upload a PDF, ask it questions — the flagship RAG demo for this module. |
| 13 | `Lab-3-Chroma_hrdataset_QA.ipynb` | RAG over the shared `hrdataset/` using Chroma. |
| 14 | `Lab-4-Pinecone_Gradio_HR_dataset_QA.ipynb` | Same idea, backed by Pinecone, with a Gradio front end. |
| 15 | `Lab-5-Hybrid_Search_with_Pinecone.ipynb` | Hybrid (keyword + vector) search — a more production-grade RAG pattern. |

### LangChain
| Lab | Notebook | Description |
|-----|----------|-------------|
| 16 | `Lab-1-Langchain_basic.ipynb` | Core LangChain building blocks. |
| 17 | `Lab-2-RAG_with_Langchain.ipynb` | RAG assembled with LangChain instead of raw calls. |

Several RAG labs depend on the `hrdataset/` folder at the repo root.

---
