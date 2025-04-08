cd "$PSScriptRoot"
cd "React-Flask"
cd "frontend"
start powershell -ArgumentList '-Command "npm run dev'
cd ".."
cd "backend"
start "http://localhost:5173/"
$env:FLASK_APP="FlaskBackend"
py -m flask run