@echo off
echo Installing frontend dependencies...
cd frontend
call npm install

echo Building React frontend...
call npm run build

echo Cleaning old static and template files in backend...
cd ..
rmdir /s /q backend\static
mkdir backend\static
del /q backend\templates\index.html

echo Copying new build to backend...
xcopy /s /i /y frontend\dist\assets backend\static\
copy frontend\dist\index.html backend\templates\
copy frontend\public\logo.png backend\static\

echo Installing backend Python dependencies...
cd backend
python -m pip install -r requirements.txt || python3 -m pip install -r requirements.txt

echo Build complete.
pause
