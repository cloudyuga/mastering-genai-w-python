#
# AI Chat Analyzer - Simplified for Learning
#
# Objective: A simple, easy-to-understand Gradio application that uses an
# OpenAI-powered RAG (Retrieval-Augmented Generation) pipeline to analyze
# and answer questions about any uploaded chat history file.
#

# --- Step 1: Install Necessary Libraries ---
# We need 'gradio' for the web UI, 'openai' for the API, 'langchain' components
# for the RAG pipeline, and 'faiss-cpu' for efficient document searching.
!pip install -q gradio openai langchain langchain-community langchain-openai langchain_text_splitters faiss-cpu

# --- Step 2: Import Required Modules ---
import gradio as gr
from openai import OpenAI
import os

# Import the necessary components from the LangChain library.
# LangChain helps us build applications with Large Language Models (LLMs).
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# --- Step 3: Backend Logic (The "Brain" of the App) ---

def setup_rag_pipeline(api_key, file_content):
    """
    This function builds the core RAG (Retrieval-Augmented Generation) pipeline.
    RAG is a powerful technique that allows an LLM to answer questions based on
    a specific set of documents, like your chat history.

    Here's how it works:
    1.  Load & Split: The chat history text is loaded and split into small,
        manageable chunks. This is better than feeding one giant file to the AI.
    2.  Embed: Each chunk is converted into a numerical representation called an
        "embedding" using an OpenAI model. Think of this as creating a unique
        fingerprint for the meaning of each chunk.
    3.  Store & Index: These embeddings are stored in a special database (a FAISS
        vector store) that is highly optimized for finding the most similar
        chunks based on a user's question.

    Args:
        api_key (str): The user's OpenAI API key.
        file_content (str): The raw text content from the uploaded chat file.

    Returns:
        FAISS: A vector store object ready to be queried.
    """
    try:
        # 1. Split the document into chunks.
        # We use a text splitter that recursively tries to split text on
        # different characters (like newlines) to keep related pieces together.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # Max size of each chunk (in characters)
            chunk_overlap=100   # Overlap between chunks to maintain context
        )
        docs = text_splitter.split_text(file_content)

        if not docs:
            raise ValueError("File content is empty or could not be split.")

        # 2. Initialize the OpenAI embedding model.
        # This model is responsible for turning text chunks into vectors.
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)

        # 3. Create the FAISS vector store from the document chunks.
        # This indexes all the text chunks for fast and efficient searching.
        vector_store = FAISS.from_texts(docs, embeddings)
        return vector_store

    except Exception as e:
        # If anything goes wrong (e.g., invalid API key), we raise an error.
        raise gr.Error(f"Failed to build RAG pipeline: {e}")


def process_chat_request(user_question, chat_history, state_data):
    """
    This function handles the user's question and generates a response.

    Here's the process:
    1.  Retrieve Context: It takes the user's question and uses the FAISS
        vector store to find the most relevant text chunks from the original
        chat history. This is the "Retrieval" part of RAG.
    2.  Construct Prompt: It creates a detailed prompt for the AI, including
        the retrieved chunks as "context." This tells the AI: "Answer the
        user's question based ONLY on this information."
    3.  Generate Answer: It sends this prompt to the OpenAI chat model
        (gpt-3.5-turbo) to get an answer. This is the "Generation" part of RAG.
    """
    # Retrieve the necessary data (API key, vector store) from the app's state.
    api_key = state_data.get("api_key")
    temp = state_data.get("temp")
    vector_store = state_data.get("vector_store")

    # Basic validation.
    if not all([api_key, temp is not None, vector_store]):
        raise gr.Error("Configuration is incomplete. Please restart.")
    if not user_question:
        raise gr.Error("Please enter a question.")

    # 1. Retrieve relevant context from the vector store.
    # We perform a "similarity search" to find the top chunks most
    # relevant to the user's question.
    # --- KEY CHANGE ---
    # Increased 'k' from 5 to 8 to retrieve more context. This makes the
    # model more robust and reduces the chance of missing key information,
    # which solves the problem of inconsistent answers.
    retrieved_docs = vector_store.similarity_search(user_question, k=8)
    context = "\n---\n".join([doc.page_content for doc in retrieved_docs])

    # 2. Construct the prompt for the LLM.
    # This is a critical step. The prompt guides the AI to behave as we want.
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
        # 3. Call the OpenAI API to generate the response.
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using a fast and cost-effective model
            messages=[
                {"role": "system", "content": "You are an expert chat analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=temp,
        )
        bot_response = completion.choices[0].message.content

    except Exception as e:
        raise gr.Error(f"An API error occurred: {e}")

    # Add the conversation turn to the chat history.
    chat_history.append((user_question, bot_response))
    return "", chat_history

# --- Step 4: Gradio User Interface (The "Look and Feel") ---

with gr.Blocks(theme=gr.themes.Soft(primary_hue="emerald", secondary_hue="emerald"), title="Chat Analyzer") as demo:
    # A 'State' object is used to store data that needs to persist across
    # different pages or interactions, like the API key and the vector store.
    app_state = gr.State({})

    # --- Page 1: Welcome Screen ---
    # We use 'gr.Column' with the 'visible' property to create a multi-page app.
    # Only one column (page) is visible at a time.
    with gr.Column(visible=True) as welcome_page:
        gr.Markdown(
            """
            <div style='text-align: center; font-family: "Garamond", serif; padding-top: 50px;'>
                <h1 style='font-size: 4em;'>Chat with your History</h1>
                <p style='font-size: 1.5em; color: #555;'>Analyze any chat export using OpenAI.</p>
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
            enter_button = gr.Button("✨ Get Started ✨", variant="primary", scale=1)

    # --- Page 2: Configuration Screen ---
    with gr.Column(visible=False) as config_page:
        gr.Markdown("<h1 style='text-align: center;'>Setup Your Chat Environment</h1>")
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 1. OpenAI API Key")
                api_key_input = gr.Textbox(label="API Key", type="password", placeholder="Enter your OpenAI key here...")
                gr.Markdown("### 2. Upload Chat File")
                chat_file_upload = gr.File(label="Upload Any .txt Chat Export")
            with gr.Column(scale=1):
                gr.Markdown("### 3. Customize AI Creativity")
                temp_slider = gr.Slider(0.0, 1.0, value=0.5, step=0.1, label="Temperature")
        lets_chat_button = gr.Button("💬 Build Pipeline & Chat! 💬", variant="primary")

    # --- Page 3: Chat Interface ---
    with gr.Column(visible=False) as chat_page:
        gr.Markdown("<h1 style='text-align: center;'>Chat Analyzer</h1>")
        chatbot_ui = gr.Chatbot(height=600, bubble_full_width=False, label="Chatbot")
        with gr.Row():
            user_input_box = gr.Textbox(placeholder="Ask a question about your chat...", scale=5, label="Your Question")
            submit_button = gr.Button("Send", variant="primary", scale=1)

    # --- Step 5: Event Handling (Connecting UI to Backend) ---

    def go_to_config():
        """Function to switch from the welcome page to the config page."""
        return {
            welcome_page: gr.Column(visible=False),
            config_page: gr.Column(visible=True)
        }

    def go_to_chat(api_key, chat_file, temp):
        """
        Function to process the config, build the RAG pipeline, and switch
        to the chat page.
        """
        if not api_key:
            raise gr.Error("API Key is required.")
        if chat_file is None:
            raise gr.Error("A chat file must be uploaded.")

        # Show a notification to the user that processing has started.
        gr.Info("Processing chat file... This may take a moment.")

        # Read the content of the uploaded file.
        with open(chat_file.name, 'r', encoding='utf-8') as f:
            content = f.read()

        # Build the RAG pipeline. This is the most intensive step.
        vector_store = setup_rag_pipeline(api_key, content)

        # Save the configuration and the created vector store into the app state.
        new_state = {
            "api_key": api_key,
            "vector_store": vector_store,
            "temp": temp,
        }

        # Return the new state and the visibility updates for the pages.
        return (
            new_state,
            gr.Column(visible=False), # Hide config page
            gr.Column(visible=True)   # Show chat page
        )

    # This section "wires up" the buttons to their respective functions.
    # When a button is clicked, it calls the function specified in 'fn'.
    enter_button.click(fn=go_to_config, inputs=None, outputs=[welcome_page, config_page])

    lets_chat_button.click(
        fn=go_to_chat,
        inputs=[api_key_input, chat_file_upload, temp_slider],
        outputs=[app_state, config_page, chat_page]
    )

    # The chat submission can be triggered by clicking the 'Send' button...
    submit_button.click(
        fn=process_chat_request,
        inputs=[user_input_box, chatbot_ui, app_state],
        outputs=[user_input_box, chatbot_ui]
    )

    # ...or by pressing Enter in the textbox.
    user_input_box.submit(
        fn=process_chat_request,
        inputs=[user_input_box, chatbot_ui, app_state],
        outputs=[user_input_box, chatbot_ui]
    )

# --- Step 6: Launch the App ---
print("\nLaunching Gradio App...")
demo.launch(debug=True, share=True)
