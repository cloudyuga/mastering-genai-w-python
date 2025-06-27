import os
import gradio as gr
import base64
from openai import OpenAI
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load env and initialize
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
persist_directory = "gmail_embeddings"

openai = OpenAI()
# Global to cache vectordb
email_vectordb = None

def fetch_gmail_emails():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="").execute()
    messages = results.get('messages', [])
    email_texts = []

    for message in messages[:10]:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg['payload']
        headers = payload.get('headers', [])
        subject = "No Subject"
        for header in headers:
            if header.get('name') == 'Subject':
                subject = header.get('value')
                break
        parts = payload.get('parts', [])
        for part in parts:
            if part['mimeType'] == 'text/plain':
                body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                email_texts.append(f"Subject: {subject}\n\n{body}")
    return "\n".join(email_texts)

def create_chunks(email_text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.create_documents([email_text])
    return chunks

def embed_emails():
    global email_vectordb
    email_text = fetch_gmail_emails()
    chunks = create_chunks(email_text)
    email_vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    # ✅ No need to call .persist() manually
    return "✅ Emails fetched and embedded successfully."

def query_emails(prompt):
    if not email_vectordb:
        try:
            vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
        except Exception:
            return "❌ Please fetch and embed emails first."
    else:
        vectordb = email_vectordb

    docs = vectordb.similarity_search(prompt)
    if not docs:
        return "⚠️ No relevant information found in your emails."
    
    context = docs[0].page_content
    messages = [
        {"role": "system", "content": "You are an assistant to help with email queries."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}\n\nAnswer:"}
    ]
    try:
        response = openai.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=messages,
        )
        return response.choices[0].message.content
            
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 📬 Chat with Your Gmail Inbox using OpenAI + ChromaDB")

    fetch_button = gr.Button("🔄 Fetch & Embed Emails")
    status_output = gr.Textbox(label="Status", lines=1)

    question_input = gr.Textbox(label="Ask a Question about Your Emails", placeholder="e.g., What's the last newsletter I got?")
    ask_button = gr.Button("💬 Get Answer")
    answer_output = gr.Textbox(label="Answer", lines=4)

    fetch_button.click(fn=embed_emails, outputs=status_output)
    ask_button.click(fn=query_emails, inputs=question_input, outputs=answer_output)

demo.launch()
