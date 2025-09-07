# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheelpython 
python -m pip install -r requirements.txt
python -m pip install numpy==2.2.0
python -m pip install spacy==3.8.3
python -m spacy download en_core_web_sm
pip install transformers torch


