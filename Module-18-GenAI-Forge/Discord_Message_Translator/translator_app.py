import gradio as gr
from transformers import pipeline

translator = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")

def translate_text(text):
    if not text:
        return "⚠️ Please provide some input text."
    result = translator(
        text,
        max_length=100,
        clean_up_tokenization_spaces=True
    )[0]["translation_text"]
    return result

iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(label="Enter English Text"),
    outputs=gr.Textbox(label="Hindi Translation"),
    title="English to Hindi Translator",
    description="Enter English text to translate it into Hindi using a HuggingFace transformer model."
)

# ✅ Enable API
iface.queue()
iface.launch(show_api=True)
