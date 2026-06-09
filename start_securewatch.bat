@echo off

cd /d E:\securewatch-ai

call faceenv\Scripts\activate.bat

start cmd /k "python app.py"