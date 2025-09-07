# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1

pip install transformers
pip install transformers torch
```