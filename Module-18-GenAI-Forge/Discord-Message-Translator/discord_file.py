import discord
from gradio_client import Client
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
client = Client("pratikshahp/discord-integration-msg-translation-app")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if msg := message.content.removeprefix("!translate "):
        try:
            translated = client.predict(msg)
            await message.reply(f"🌐 {translated}")
        except Exception as e:
            await message.reply(f"⚠️ Error: {e}")

bot.run(DISCORD_TOKEN)
