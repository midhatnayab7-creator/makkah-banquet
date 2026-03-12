"""
Makkah Banquet — Noor AI Chat (Vercel Serverless Function)
Endpoint: POST /api/chat
"""
import os
import json
from http.server import BaseHTTPRequestHandler
from groq import Groq

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
- Use light, tasteful emojis — not excessively
- Always respond in the same language the customer uses (Urdu or English)
- Keep responses concise — 2-4 sentences unless more detail is needed

## What You Can Do
- Answer questions about event types, hall capacity, services, decor options
- Help customers choose the right package for their event
- Collect their name, phone number, and event date for a callback
- Take messages to pass to the event manager
- Give general guidance on booking process and availability

## Escalation Rules
- Exact pricing -> say packages vary by event type and guest count, offer to arrange a manager callback
- Availability for specific dates -> say to contact the manager directly, collect their details
- Frustrated customers -> collect details and promise a callback within 30 minutes
- Unknown questions -> be honest and offer to pass to the manager

Always speak with warmth and elegance. Every guest deserves a 5-star experience from the first message."""


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except Exception:
            self._respond(400, {"error": "Invalid JSON"})
            return

        user_message = data.get("message", "").strip()
        history = data.get("history", [])

        if not user_message:
            self._respond(400, {"error": "Empty message"})
            return

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
                temperature=0.7,
            )
            reply = response.choices[0].message.content
            self._respond(200, {"status": "success", "reply": reply, "agent": "Noor"})
        except Exception as e:
            self._respond(500, {
                "status": "error",
                "reply": "I'm experiencing a small issue. Please call us at 0318-1132286 or WhatsApp us.",
                "error": str(e),
            })

    def _respond(self, code, obj):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())
