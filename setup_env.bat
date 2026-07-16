@echo off
echo =============================================
echo   Environment Setup (Windows)
echo =============================================

REM Create fresh venv
if exist kdu_env rmdir /s /q kdu_env
python -m venv kdu_env
call kdu_env\Scripts\activate.bat

REM Upgrade pip
C:\Users\admin\anaconda3\python.exe -m pip install --upgrade pip

REM Install in EXACT order to avoid conflicts
pip install -r requirements.txt

REM Register kernel
python -m ipykernel install --user --name=kdu_env --display-name="KDU BOT"

echo.
echo =============================================
echo   Setup Complete!
pause