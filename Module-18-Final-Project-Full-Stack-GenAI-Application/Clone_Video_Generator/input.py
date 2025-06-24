from openai import OpenAI
from gtts import gTTS
from dotenv import load_dotenv
import os   
# Load environment variables
load_dotenv()   
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
prompt = "Create a 3 to 4 sentences that promots Indian culture"

response = OpenAI().chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)
script = response.choices[0].message.content
tts = gTTS(script)
tts.save("input_gpt_script.wav")
