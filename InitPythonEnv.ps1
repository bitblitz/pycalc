# In PowerShell
py -3 -m venv env
env\scripts\activate
pip install -r requirements.txt
Set-Item Env:FLASK_ENV development
Set-Item Env:FLASK_APP ".\application.py"

Write-Host "Setup Complete. Run with 'flask run'"

