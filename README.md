# 🥬 Cabbage Discord Bot

A playful AI chatbot for Discord powered by **Gemini 2.5 Flash** and a custom **Flask API**.

---

## 🚀 Features

- Funny cabbage personality 🌿  
- Mentions-only chat activation (`@botname`)  
- Ping command (`!ping`)  
- Long message splitting for Discord’s 2000-char limit  
- Local Flask API backend using Gemini API  

---

## 🧠 Architecture
```yaml
Discord Chat → bot.py → POST → Flask server → Gemini → Response → Discord
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/ArdianPermanaW/Cabbage.git
cd Cabbage
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```bash 
DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_google_genai_api_key_here
API_URL=http://localhost:5000/generate
OWNER_ID=your_id_here
```

### 5. Run the Flask API
```bash
python server.py
```

### 6. Run the Discord bot
```bash
python cabbage.py
```

---

## 🧩 Commands

| Command | Description |
|----------|--------------|
| `!ping` | Replies with “Pong!” |
| `@Cabbage <message>` | Sends your message to the cabbage brain 🥬 |

---

## 🧩 Roadmap / To-Do

- [x] Core bot setup (`discord.py`)
- [x] Gemini API integration
- [ ] Personality toggle command
- [ ] Deploy to VPS
- [ ] Add RAG + memory 
- [ ] voice response?

---

## 📜 License

MIT License © 2025 [Ardian Permana W]

