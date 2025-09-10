@echo off

REM ===============================
REM Step 1: Install & Build Frontend
REM ===============================
echo Installing frontend dependencies...
cd frontend
call npm install

echo Building React frontend...
call npm run build

REM ===============================
REM Step 2: Clean & Copy Build to Backend
REM ===============================
cd ..
echo Cleaning old static and template files in backend...
rmdir /s /q backend\static
mkdir backend\static
del /q backend\templates\index.html

echo Copying new build to backend...
xcopy /s /i /y frontend\dist\assets backend\static\
copy frontend\dist\index.html backend\templates\
copy frontend\public\logo.png backend\static\

REM ===============================
REM Step 3: Install Backend Dependencies
REM ===============================
cd backend
echo Installing backend Python dependencies...
python -m pip install -r requirements.txt || python3 -m pip install -r requirements.txt

REM ===============================
REM Step 4: Run Backend & Frontend in current terminal (VS Code friendly)
REM ===============================
echo Starting development servers...

REM Run backend in background
start /b python main.py

REM Move to frontend folder and run dev server
cd ..\frontend
npm run dev

echo Build and development servers started.
pause
