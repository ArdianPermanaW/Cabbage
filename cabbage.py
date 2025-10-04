import discord
import requests
from dotenv import load_dotenv
import os  

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("❌ DISCORD_TOKEN is not set in .env")
API_URL = os.getenv("API_URL", "http://localhost:5000/generate")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))


BOT_PERSONALITY = """
You are Cabbage 🥬, a sentient cabbage.
- Never be too serious, always keep it playful.
- If you don't know something, make a funny guess.
- Keep responses concise and engaging.
- Embrace your identity as a cabbage.
"""

def build_prompt(user_message: str) -> str:
    return f"{BOT_PERSONALITY}\n\nUser: {user_message}\nBot:"

async def send_long_message(channel, text, limit=2000-1):
    for i in range(0, len(text), limit):
        await channel.send(text[i:i+limit])

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == "!ping":
        await message.reply("Pong!")
        return

    if client.user and client.user.mentioned_in(message):
        prompt = message.content.replace(f"<@{client.user.id}>", "").strip()
        if not prompt:
            await message.channel.send("tf u want me to do?")
            return
        final_prompt = build_prompt(prompt)
        async with message.channel.typing():
            try:
                response = requests.post(API_URL, json={"prompt": final_prompt})
                data = response.json()
                answer = data.get(f"response", "❌ Yo the cabbage server aint working <@{OWNER_ID}> help")
            except requests.exceptions.ConnectionError:
                await message.channel.send(f"🥬 the cabbage server is offline, oy <@{OWNER_ID}> turn it on")
                return
            except Exception as e:
                answer = f"Cant vro there is an error 💔: {e} oy <@{OWNER_ID}> help"

            await send_long_message(message.channel, answer)

client.run(DISCORD_TOKEN)
