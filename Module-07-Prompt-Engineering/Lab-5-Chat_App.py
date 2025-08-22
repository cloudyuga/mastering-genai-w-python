#
# Chat App for WhatsApp & Telegram
# Objective: To create a robust, parser-free, multi-page Gradio application
# for chatting with any exported chat data using a RAG pipeline.
#

# Step 1: Install necessary libraries (with langchain-openai added)
!pip install -q gradio google-generativeai openai langchain langchain-community langchain-google-genai langchain-openai langchain_text_splitters faiss-cpu

# Step 2: Import libraries
import gradio as gr
import google.generativeai as genai
from openai import OpenAI
import os

# --- RAG components from LangChain ---
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings # NEW: Import OpenAI embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# --- Backend Logic ---

# CORRECTED: The function now accepts the provider to choose the correct embedding model.
def setup_rag_pipeline(api_key, file_content, provider):
    """
    Sets up the RAG pipeline. It now dynamically selects the embedding model
    based on the chosen provider.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )
        docs = text_splitter.split_text(file_content)

        if not docs:
            raise ValueError("File content is empty or could not be split into chunks.")

        # NEW: Conditional logic to select the embedding model
        if provider == "Google Gemini":
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
        elif provider == "OpenAI":
            embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        else:
            raise ValueError("Invalid provider selected for embeddings.")

        vector_store = FAISS.from_texts(docs, embeddings)
        return vector_store

    except Exception as e:
        raise gr.Error(f"Failed to build RAG pipeline: {e}")


def process_chat_request(user_question, chat_history, state_data):
    """
    The main chat logic function using the RAG pipeline.
    """
    provider = state_data.get("provider")
    api_key = state_data.get("api_key")
    temp = state_data.get("temp")
    vector_store = state_data.get("vector_store")

    if not all([provider, api_key, temp is not None, vector_store]):
        raise gr.Error("Configuration is incomplete or RAG pipeline not set. Please restart.")
    if not user_question:
        raise gr.Error("Please enter a question.")

    retrieved_docs = vector_store.similarity_search(user_question, k=5)
    context = "\n---\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
    You are a helpful assistant that analyzes a chat history. Based ONLY on the provided context below,
    answer the user's question. Do not use any external knowledge. If the answer is not in the context,
    state that you cannot find the answer in the provided chat history.

    --- RELEVANT CHAT CONTEXT ---
    {context}
    --- END OF CONTEXT ---

    QUESTION:
    "{user_question}"
    """

    try:
        if provider == "Google Gemini":
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt, generation_config={"temperature": temp})
            bot_response = response.text
        elif provider == "OpenAI":
            client = OpenAI(api_key=api_key)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo", # CORRECTED: Changed to the faster, cheaper model
                messages=[
                    {"role": "system", "content": "You are an expert chat analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temp,
            )
            bot_response = completion.choices[0].message.content
        else:
            bot_response = "Error: Invalid provider."

    except Exception as e:
        raise gr.Error(f"An API error occurred: {e}")

    chat_history.append((user_question, bot_response))
    return "", chat_history

# --- Gradio UI Definition ---

with gr.Blocks(theme=gr.themes.Soft(primary_hue="emerald", secondary_hue="emerald"), title="Chat Analyzer") as demo:
    app_state = gr.State({})

    # --- Page 1: Welcome Screen ---
    with gr.Column(visible=True) as welcome_page:
        gr.Markdown(
            """
            <div style='text-align: center; font-family: "Garamond", serif; padding-top: 50px;'>
                <h1 style='font-size: 4em;'>Chat with your History</h1>
                <p style='font-size: 1.5em; color: #555;'>Analyze any chat export using the power of RAG.</p>
            </div>
            """
        )
        gr.HTML(
            """
            <div style='text-align: center; padding: 30px;'>
                <img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2Vjb3M2eGZzN2FkNWZpZzZ0bWl0c2JqZzZlMHVwZ2l4b2t0eXFpcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YWjDA4k2n6d5Ew42zC/giphy.gif'
                     style='max-width: 400px; margin: auto; border-radius: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);' />
            </div>
            """
        )
        with gr.Row():
            enter_button = gr.Button("✨ Get Started ✨", variant="primary", scale=1, elem_id="enter_button")

    # --- Page 2: Configuration Screen ---
    with gr.Column(visible=False) as config_page:
        gr.Markdown("<h1 style='text-align: center;'>Setup Your Chat Environment</h1>")
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 1. Choose your AI Provider")
                provider_select = gr.Radio(["Google Gemini", "OpenAI"], label="Provider", value="Google Gemini")
                api_key_input = gr.Textbox(label="API Key", type="password", placeholder="Enter your key here...")
                gr.Markdown("### 2. Upload Chat File")
                chat_file_upload = gr.File(label="Upload Any .txt Chat Export")
            with gr.Column(scale=1):
                gr.Markdown("### 3. Customize Parameters")
                temp_slider = gr.Slider(0.0, 1.0, value=0.5, step=0.1, label="Temperature (Creativity)")
        lets_chat_button = gr.Button("💬 Build RAG Pipeline & Chat! 💬", variant="primary")

    # --- Page 3: Chat Interface ---
    with gr.Column(visible=False) as chat_page:
        gr.Markdown("<h1 style='text-align: center;'>Chat Analyzer</h1>")
        chatbot_ui = gr.Chatbot(height=600, bubble_full_width=False, label="Chatbot")
        with gr.Row():
            user_input_box = gr.Textbox(placeholder="Ask a question about your chat...", scale=5, label="Your Question")
            submit_button = gr.Button("Send", variant="primary", scale=1)

    # --- Page Transition and Data Handling Logic ---
    def go_to_config():
        return {
            welcome_page: gr.Column(visible=False),
            config_page: gr.Column(visible=True)
        }

    def go_to_chat(api_key, chat_file, provider, temp):
        if not api_key:
            raise gr.Error("API Key is required.")
        if chat_file is None:
            raise gr.Error("A chat file must be uploaded.")

        gr.Info("Processing chat file... This may take a moment for large files.")

        with open(chat_file.name, 'r', encoding='utf-8') as f:
            content = f.read()

        # CORRECTED: Pass the selected provider to the pipeline setup function.
        vector_store = setup_rag_pipeline(api_key, content, provider)

        new_state = {
            "provider": provider,
            "api_key": api_key,
            "vector_store": vector_store,
            "temp": temp,
        }

        return (
            new_state,
            gr.Column(visible=False),
            gr.Column(visible=True)
        )

    # Wire up the buttons
    enter_button.click(fn=go_to_config, inputs=None, outputs=[welcome_page, config_page])

    lets_chat_button.click(
        fn=go_to_chat,
        inputs=[api_key_input, chat_file_upload, provider_select, temp_slider],
        outputs=[app_state, config_page, chat_page]
    )

    submit_button.click(
        fn=process_chat_request,
        inputs=[user_input_box, chatbot_ui, app_state],
        outputs=[user_input_box, chatbot_ui]
    )

    user_input_box.submit(
        fn=process_chat_request,
        inputs=[user_input_box, chatbot_ui, app_state],
        outputs=[user_input_box, chatbot_ui]
    )

# --- Launch the App ---
print("\nLaunching Gradio App...")
demo.launch(debug=True, share=True)
