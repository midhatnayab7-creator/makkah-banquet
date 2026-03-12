# 🚀 Makkah Banquet AI — Render Deployment Guide

## ✅ What's Ready to Deploy
- ✅ Flask backend (`ai_server.py`)
- ✅ Requirements.txt with all dependencies
- ✅ Procfile for Render
- ✅ .render.yaml configuration
- ✅ Updated frontend with smart URL detection
- ✅ All features: Welcome Hook + Contact Manager + AI Assistant (Noor)

---

## 📋 Deployment Steps (5 minutes)

### Step 1: Push to GitHub
```bash
cd C:\Users\kk\makkah-banquet
git push origin 002-shopping-cart
```

### Step 2: Go to Render Dashboard
1. Open: https://dashboard.render.com/
2. Sign up with GitHub (or login)
3. Click **"New +"** → **"Web Service"**

### Step 3: Connect Repository
1. Select your GitHub repo: `anthropics/claude-code` (or your fork)
2. Choose branch: `002-shopping-cart`
3. Root directory: `makkah-banquet`
4. Runtime: **Python 3.11**

### Step 4: Configure Environment
1. **Name**: `makkah-banquet-ai` (or any name you want)
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `gunicorn ai_server:app`
4. **Environment Variables** → Click "Add Environment Variable":
   - **Key**: `GROQ_API_KEY`
   - **Value**: `YOUR_GROQ_API_KEY_HERE`

### Step 5: Deploy
1. Click **"Create Web Service"**
2. Wait ~2-3 minutes for deployment to complete
3. Copy your Render URL (looks like: `https://makkah-banquet-ai.onrender.com`)

### Step 6: Update Frontend (if needed)
The frontend is **already configured** to auto-detect the Render URL. No changes needed!

---

## ✨ What You Get After Deployment

| Feature | Status |
|---------|--------|
| 🏛️ Welcome Hook | ✅ Working |
| 📞 Contact Manager | ✅ Working |
| 💬 AI Assistant (Noor) | ✅ Working |
| 🌍 Accessible Anywhere | ✅ Live URL |
| 📱 Mobile Friendly | ✅ Responsive |

---

## 🔗 Your Live Website URLs

**Frontend (Vercel)**: https://makkah-banquet.vercel.app
**Backend (Render)**: https://makkah-banquet-ai.onrender.com

---

## 🧪 Testing After Deployment

1. Open your Vercel URL
2. Click the 💬 Chat button
3. Send a message to Noor
4. ✅ Should respond with AI (powered by Groq)

---

## 💡 Local Testing (Optional)

To test locally before deploying:
```bash
set GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
python ai_server.py
```

Then open `index.html` in browser — AI chat will work on `http://localhost:5001`

---

## 📞 If Something Goes Wrong

1. Check Render logs: Dashboard → Your Service → "Logs"
2. Verify GROQ_API_KEY is set correctly
3. Check that root directory is `makkah-banquet`

---

**Questions? Contact support@render.com or check Render docs: https://render.com/docs**
