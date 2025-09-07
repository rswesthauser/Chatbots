# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.10 -m venv env
.\env\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```