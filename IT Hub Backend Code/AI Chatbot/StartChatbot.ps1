cd "$PSScriptRoot"
cd "React-Flask"
cd "frontend"
start powershell -ArgumentList '-Command "Start-Sleep -Seconds 1; npm run dev'
cd ".."
cd "backend"
start "http://localhost:5173/"
$env:FLASK_APP="FlaskBackend"
Start-Sleep -Seconds 3
py -m flask run