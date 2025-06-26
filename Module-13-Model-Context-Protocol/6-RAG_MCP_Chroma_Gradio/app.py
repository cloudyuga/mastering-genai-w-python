import os, asyncio
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from fastmcp.client import Client
from fastmcp.client.transports import SSETransport

load_dotenv()
openai_client = OpenAI()
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")

# Wrapper to call tools
async def call_tool(tool_name: str, args: dict):
    async with Client(transport=SSETransport(MCP_SERVER_URL)) as client:
        return await client.call_tool(tool_name, args)

# PDF upload
def handle_pdf(pdf_file):
    # pdf_file is a NamedString, so treat it as a path
    import shutil
    save_path = os.path.join("uploads", os.path.basename(pdf_file))
    os.makedirs("uploads", exist_ok=True)
    shutil.copy(pdf_file, save_path)
    result = asyncio.run(call_tool("ingest_pdf", {"pdf_path": save_path}))
    if isinstance(result, list) and len(result) > 0:
        return result[0].text
    return "Ingestion failed."


# Ask RAG-based question
def ask_rag(question, pdf_file):
    result = asyncio.run(call_tool("rag_query", {
        "question": question,
        "pdf_path": pdf_file.name
    }))
    if isinstance(result, list) and len(result) > 0:
        return result[0].text
    return "No response received."

with gr.Blocks() as app:
    gr.Markdown("# 📄 RAG Chatbot using MCP with PDF Upload")

    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        upload_btn = gr.Button("Ingest PDF")
        upload_output = gr.Textbox(label="Ingestion Status")

    with gr.Row():
        question = gr.Textbox(label="Ask a Question", placeholder="What is this PDF about?")
        ask_btn = gr.Button("Get Answer")
        
        answer = gr.Textbox(label="Answer")
    upload_btn.click(handle_pdf, inputs=pdf_input, outputs=upload_output)
    ask_btn.click(ask_rag, inputs=[question, pdf_input], outputs=answer)


app.launch()
