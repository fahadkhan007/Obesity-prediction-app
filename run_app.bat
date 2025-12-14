@echo off
echo ========================================
echo   Obesity Level Predictor - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install/Update dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet
echo.

REM Run the Streamlit app
echo Starting Streamlit application...
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.
streamlit run app.py

pause
