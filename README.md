# Makkah Banquet

Karachi's premier luxury banquet hall website — featuring AI-powered customer assistance, online booking, and a full gallery experience.

**Live Site:** [makkah-banquet.vercel.app](https://makkah-banquet.vercel.app)

---

## Features

- **7 Full Pages** — Home, Services, Menu, Gallery, Video, Booking, and Contact
- **AI Assistant (Noor)** — Intelligent chat widget powered by Groq + Llama 4 that answers visitor questions about events, pricing, and availability
- **Online Booking Form** — Guests can request event bookings directly from the website
- **Video & Gallery** — Showcase banquet hall ambiance with photos and video
- **Responsive Design** — Fully mobile-friendly layout
- **SEO Optimized** — Meta tags, Open Graph, sitemap, and robots.txt included
- **Multi-Platform Deployment** — Frontend on Vercel, AI backend on Render

## Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS, JavaScript          |
| AI Backend  | Python, Flask, Flask-CORS      |
| AI Model    | Groq API + Llama 4             |
| Hosting     | Vercel (frontend), Render (AI) |

## Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/midhatnayab7-creator/makkah-banquet.git
   cd makkah-banquet
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Groq API key**
   ```bash
   export GROQ_API_KEY="your-key-here"
   ```

4. **Start the AI backend**
   ```bash
   python ai_server.py
   ```
   The AI server runs on `http://localhost:5001`.

5. **Open the website**

   Open `index.html` in your browser, or use a local server:
   ```bash
   python -m http.server 8080
   ```
   Then visit `http://localhost:8080`.

## Project Structure

```
makkah-banquet/
├── index.html          # Home page
├── services.html       # Services offered
├── menu.html           # Food & catering menu
├── gallery.html        # Photo gallery
├── video.html          # Video showcase
├── booking.html        # Event booking form
├── contact.html        # Contact information
├── css/style.css       # Stylesheet
├── js/main.js          # Frontend logic & chat widget
├── images/             # Media assets
├── ai_server.py        # Noor AI backend (Flask)
├── api/chat.py         # Vercel serverless function
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel config
├── netlify.toml        # Netlify config
├── sitemap.xml         # SEO sitemap
└── robots.txt          # Crawler rules
```

## License

This project is proprietary to Makkah Banquet.
