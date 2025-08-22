AI-Powered Chat Analyzer
An interactive and user-friendly web application that allows you to have conversations with your own chat history from WhatsApp and Telegram. Built with Python, Gradio, and the OpenAI API, this tool uses a powerful Retrieval-Augmented Generation (RAG) pipeline to understand and answer questions about your uploaded chat files without the need for complex parsing.

✨ Features
Universal Chat Support: Analyze any .txt chat export from platforms like WhatsApp and Telegram.

No More Parsing Errors: Uses a robust RAG pipeline, eliminating the need for fragile text parsers that break with format changes.

Intuitive UI: A simple, multi-page web interface built with Gradio that guides you from setup to chat in a few clicks.

Intelligent Analysis: Ask complex questions about your conversations and get accurate, context-aware answers.

Powered by OpenAI: Leverages the gpt-3.5-turbo model for fast and cost-effective responses.

🧠 How It Works
This application is built on a modern AI architecture called Retrieval-Augmented Generation (RAG). Instead of just blindly passing text to the AI, it follows a smarter process:

Load & Chunk: The entire chat history is loaded and broken down into small, overlapping chunks of text.

Embed & Index: Each chunk is converted into a numerical representation (a "vector embedding") using an OpenAI model. These are then stored in a high-speed search index (FAISS).

Retrieve: When you ask a question, the app searches the index to find the most relevant chunks from the chat history.

Generate: These relevant chunks are passed to the OpenAI gpt-3.5-turbo model along with your question. The model then generates an answer based only on the provided context.

This method ensures high accuracy and allows the application to handle very large chat files efficiently.

🚀 Setup and Usage
Follow these steps to get the Chat Analyzer running on your local machine.

1. Clone the Repository
First, clone the repository to your local machine. If you are contributing, make sure to fork it first.

git clone https://github.com/cloudyuga/mastering-genai-w-python.git
cd mastering-genai-w-python/Module-07-Prompt-Engineering

2. Install Dependencies
The application requires several Python libraries. You can install them all with a single command:

pip install -q gradio openai langchain langchain-community langchain-openai langchain_text_splitters faiss-cpu

3. Set Your OpenAI API Key
You will need an API key from OpenAI to use this application.

Get your key from the OpenAI Platform website.

The application will prompt you to enter this key in the web interface.

4. Run the Application
Execute the Python script to launch the Gradio web server:

python your_script_name.py

You will see output in your terminal with a local URL (usually http://127.0.0.1:7860). Open this URL in your web browser to use the app.

📲 Exporting Your Chat History
To use the app, you first need a .txt file of your chat history. Here’s how to get it from WhatsApp and Telegram.

On WhatsApp
Open the Chat: Go to the individual or group chat you want to export.

Access Chat Info:

On Android: Tap the three-dot menu (⋮) in the top-right corner, then select More > Export chat.

On iPhone: Tap the contact or group name at the top, scroll down, and select Export Chat.

Choose Export Options:

You will be asked if you want to include media. For this application, select "Without Media". This will create a much smaller .txt file.

Save the File: Save or send the .txt file to your computer. You can email it to yourself, save it to a cloud drive, or use any other preferred method.

On Telegram
Use Telegram Desktop: You must use the Telegram Desktop application on a Windows or macOS computer to export chat history.

Open the Chat: Select the chat you wish to export.

Find the Export Menu: Click the three-dot menu (⋮) in the top-right corner of the chat window.

Select "Export chat history":

A settings window will pop up.

Deselect all media types (Photos, Videos, Voice messages, etc.) to ensure you only get the text.

Make sure the format is set to "Human-readable HTML". Telegram will also provide a messages.html and other files, but the core text is what we need. Alternatively, if a plain text option is available, choose that.

Export and Locate: Click Export and wait for the process to complete. Telegram will save the files in a folder on your computer. You can then use the main text or HTML file.

🤝 Contributing
This project is part of the "Mastering GenAI with Python" course by Cloudyuga. Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Please create a pull request to the main branch of the repository to contribute.
