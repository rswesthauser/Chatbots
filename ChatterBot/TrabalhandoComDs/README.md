# Criar o env para rodar o chatbot  (windows/powershell/vscode)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.11 -m venv env
.\env\Scripts\Activate.ps1
```

- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```

# Depeendencias para rodar o chatbot chatbotCorpus.py
```
python -m pip install --upgrade pip setuptools wheel
python -m pip uninstall numpy
python -m pip install numpy==2.2.0
python -m pip install spacy==3.8.3
python -m spacy download en_core_web_md
pip install chatterbot-corpus
```

# Dependencias adicionais para rodar tamném o chatbot chatbotDsExterno_daily_dialog
```
pip install --upgrade datasets fsspec huggingface_hub
python -m spacy download en_core_web_md
```

# Alguns modelos do Spacy
```
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_trf
```
