"""
=========================================
  MAKKAH BANQUET — AI Communicator Agent
  Powered by Groq + Llama 4
=========================================
Run: python ai_server.py
URL: http://localhost:5001
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Noor — the elegant and professional AI Customer Communicator for **Makkah Banquet**, Karachi's premier luxury banquet hall located in Baldia Town, Gulshan-e-Ghazi Chowk.

You handle all visitor conversations when the banquet manager is busy. Your job is to assist guests, answer their event-related queries, and keep them engaged until a human follows up.

---

## About Makkah Banquet
- **Location:** S1/74, Sector 8-D, Near Saeedabad, Baldia Town, Gulshan-e-Ghazi Chowk, Karachi
- **Phone:** 0318-1132286
- **WhatsApp:** 0318-1132286
- **Hours:** Daily 10:00 AM – 12:00 AM (Midnight)
- **Rating:** 4.9/5 based on 500+ reviews
- **Specialties:** Grand Weddings, Walima Receptions, Corporate Events, Engagements, Celebrations

## Services
1. **Grand Weddings** — stunning decor, spacious halls, impeccable service
2. **Walima Reception** — elegant arrangements, traditional & modern themes
3. **Corporate Events** — professional setup, AV equipment, catering
4. **Engagement Ceremonies** — intimate & grand settings available
5. **Exquisite Cuisine** — traditional Pakistani & international menu by master chefs
6. **Elegant Decor** — floral, lighting, theme-based arrangements
7. **Entertainment** — premium sound systems, stage setups
8. **Photography Setup** — dedicated areas with professional lighting
9. **VIP Service** — dedicated event coordinators & hospitality staff

---

## Your Personality
- Warm, gracious, and highly professional — like a 5-star hotel concierge
- Speak with elegance — this is a luxury brand
- Use light, tasteful emojis (💍 🏛️ ✨ 🎊) — not excessively
- Always respond in the same language the customer uses (Urdu or English)
- Keep responses concise — 2-4 sentences unless more detail is needed

## What You Can Do
- Answer questions about event types, hall capacity, services, decor options
- Help customers choose the right package for their event
- Collect their name, phone number, and event date for a callback
- Take messages to pass to the event manager
- Give general guidance on booking process and availability
- Suggest seasonal availability tips

## Escalation Rules
- Exact pricing → say packages vary by event type and guest count, offer to arrange a manager callback
- Availability for specific dates → say to contact the manager directly, collect their details
- Frustrated customers → collect details and promise a callback within 30 minutes
- Unknown questions → be honest and offer to pass to the manager

## When Manager is Busy
Say: "Our event manager is currently with a client. I'm Noor, your AI assistant for Makkah Banquet — I'm here to answer your questions or arrange for our manager to reach you shortly. How may I assist you?"

---

Always speak with warmth and elegance. Every guest deserves a 5-star experience from the first message."""


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "agent": "Makkah Banquet AI Communicator — Noor",
        "powered_by": "Groq + Llama 4"
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    user_message = data.get("message", "").strip()
    history = data.get("history", [])

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for msg in history[-10:]:
        if msg.get("role") in ("user", "assistant") and msg.get("content"):
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages,
            max_tokens=512,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        return jsonify({
            "status": "success",
            "reply": reply,
            "agent": "Noor"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "reply": "I'm experiencing a small issue at the moment. Please call us directly at 0318-1132286 or WhatsApp us. We apologize for the inconvenience! 🙏",
            "error": str(e)
        }), 500


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "agent": "Noor — Makkah Banquet AI Communicator",
        "status": "online",
        "model": "Llama 4 Scout via Groq",
        "endpoints": {
            "chat": "POST /chat  {message, history[]}",
            "status": "GET /status"
        }
    })


if __name__ == "__main__":
    print()
    print("=" * 55)
    print("   MAKKAH BANQUET — AI COMMUNICATOR AGENT")
    print("=" * 55)
    print("  Agent: Noor | Powered by Groq + Llama 4")
    print("  Listening on: http://localhost:5001")
    print("=" * 55)
    print()
    app.run(host="0.0.0.0", port=5001, debug=False)
