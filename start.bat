@echo off

python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and add it to the PATH.
    pause
    exit /b
)

echo Installing required modules...
pip install -r requirements.txt

echo Running Python script...
python "C:\Users\PC\Desktop\WEB CRACKER\src\main.py"

pause
