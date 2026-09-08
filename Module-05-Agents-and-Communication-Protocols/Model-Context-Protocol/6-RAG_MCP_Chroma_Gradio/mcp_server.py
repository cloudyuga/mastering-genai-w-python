# mcp_server.py
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import hashlib
import json

METADATA_FILE = "ingested_files.json"


load_dotenv()
mcp = FastMCP("rag_mcp")
client = OpenAI()

CHROMA_DIR = "chroma_db"
EMBEDDINGS = OpenAIEmbeddings()

# 🧩 1. Ingest PDF into ChromaDB
def get_file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def is_already_ingested(file_hash):
    if not os.path.exists(METADATA_FILE):
        return False
    with open(METADATA_FILE, "r") as f:
        data = json.load(f)
    return file_hash in data

def mark_as_ingested(file_hash, filename):
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[file_hash] = filename
    with open(METADATA_FILE, "w") as f:
        json.dump(data, f)

@mcp.tool()
def ingest_pdf(pdf_path: str) -> str:
    file_hash = get_file_hash(pdf_path)
    if is_already_ingested(file_hash):
        return f"{pdf_path} is already ingested ✅"

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=EMBEDDINGS,
        persist_directory=CHROMA_DIR,
        collection_name=file_hash  # Store under a unique collection

    )
    vectordb.persist()    
    mark_as_ingested(file_hash, pdf_path)
    return f"✅ Ingested {len(chunks)} chunks from {pdf_path}"

# 🧩 2. RAG Question Answering
@mcp.tool()
def rag_query(question: str, pdf_path: str) -> str:
    file_hash = get_file_hash(pdf_path)
    vectordb = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=EMBEDDINGS,
        collection_name=file_hash
    )
    results = vectordb.similarity_search_with_score(question, k=3)

    threshold = 0.4
    filtered = []
    scores_log = []

    for doc, score in results:
        scores_log.append(score)
        if score > threshold:
            filtered.append(doc)

    if not filtered:
        return f"[LLM Answer - No RAG context found] {scores_log}\nSorry, no relevant information was found in the database."

    context = "\n".join([f"- {doc.page_content}" for doc in filtered])
    prompt = f"""Use the following context to answer the question:\n\n{context}\n\nQ: {question}\nA:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return f"[RAG Answer - Based on Retrieved Context] {scores_log}\n{response.choices[0].message.content.strip()}"

if __name__ == "__main__":
    mcp.run(transport="sse")
