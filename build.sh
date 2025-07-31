#!/bin/bash

echo " Installing frontend dependencies..."
cd frontend
npm install

echo " Building React frontend..."
npm run build

echo " Cleaning old static and template files in backend..."
rm -rf ../backend/static/*
rm -f ../backend/templates/index.html

echo "Copying new build to backend..."
cp -r dist/assets ../backend/static/
cp dist/index.html ../backend/templates/
cp public/logo.png ../backend/static/

echo " Installing backend Python dependencies..."
cd ../backend
py -m pip install -r requirements.txt


echo " Build complete!"
