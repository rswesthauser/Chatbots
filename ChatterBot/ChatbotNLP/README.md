# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1
```
- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```

# Depeendencias
```
pip install --upgrade pip setuptools wheel
pip install git+https://github.com/gunthercox/ChatterBot.git
pip install spacy
python -m spacy download pt_core_news_sm
```