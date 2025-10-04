from flask import Flask, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

Gemini_API_KEY = os.getenv("GEMINI_API_KEY")
if not Gemini_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in .env")
# Init Gemini client
client = genai.Client(api_key=Gemini_API_KEY)


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)  # disables thinking
            ),
        )

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
