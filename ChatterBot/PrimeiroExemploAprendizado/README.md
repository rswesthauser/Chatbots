# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1

pip install git+https://github.com/gunthercox/ChatterBot.git
python -m spacy download en_core_web_sm
```



%pip install git+https://github.com/gunthercox/ChatterBot.git
