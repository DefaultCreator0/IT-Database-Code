cd "$PSScriptRoot"
$env:FLASK_APP="FlaskBackend"
py -m flask run
pause