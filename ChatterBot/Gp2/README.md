# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheelpython 
python -m pip install -r requirements.txt
python -m pip install flask
pip install transformers torch


