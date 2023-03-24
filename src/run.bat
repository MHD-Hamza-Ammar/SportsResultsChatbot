@echo off
start cmd /c "rasa run -m models --enable-api"
start cmd /c "rasa run actions"
start cmd /c "python app.py"
timeout /t 10
start http://127.0.0.1:5000/
timeout /t 10
start http://127.0.0.1:5000/edit/1