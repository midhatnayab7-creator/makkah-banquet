@echo off
REM Makkah Banquet AI - Local Testing Script
REM This starts the Flask backend on port 5001

echo.
echo ============================================
echo  MAKKAH BANQUET AI - LOCAL TEST
echo ============================================
echo.

REM Check if GROQ_API_KEY is set
if "%GROQ_API_KEY%"=="" (
    echo ERROR: GROQ_API_KEY not set!
    echo.
    echo Please set it first:
    echo   set GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
    echo.
    exit /b 1
)

echo Starting Makkah Banquet AI Server...
echo Listen on: http://localhost:5001
echo.
echo To test:
echo   1. Open index.html in your browser
echo   2. Click the chat button (💬)
echo   3. Send a message to Noor
echo.

cd %~dp0
python ai_server.py

pause
