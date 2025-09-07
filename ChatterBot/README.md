
# Reposiórios relacionados
https://github.com/gunthercox/ChatterBot
https://github.com/gunthercox/chatterbot-corpus

# 1 - Instalar o python de acordo com o Sistema Operacional
https://www.python.org/downloads/

# 2 - Criar um env para cada exeplo, para evtiar conflito entre as dependências 
/ChatbotSimplesPrEn/menuChatbot.py
/TrabalhandoComDs/chatbotDsExterno.py
/TrabalhandoComDs/chatbotDsSimples.py

# 2.1 - Criando um env on MAC/Linux
- Criar o venv
python3 -m venv env
- Ativar o venv
source env/bin/activate
- Instalar os requisitos
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

# 2.1 - Criando um env on Windows (cmd)
- Criar o venv
py -3.10 -m venv env
- Ativar o venv
env\Scripts\activate.bat
- Instalar os requisitos
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

```
py -3.10 -m venv env
env\Scripts\activate.bat
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

# 2.1 - Criando um env on Windows (PowerShell)
- Permitir execução de scripts (se necessário)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Criar o venv
py -3.10 -m venv env
- Ativar o venv
.\env\Scripts\Activate.ps1
- Instalar os requisitos
python.exe -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
py -3.10 -m venv env
.\env\Scripts\Activate.ps1
python.exe -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```

# 3 - Baixar modelo de dados
```
python -m spacy download en_core_web_sm 
pip install chatterbot-corpus
pip install --upgrade datasets fsspec huggingface_hub
```

# 4 - Verificar a isntalação
```
where python
python -m pip list | findstr spacy
python -m spacy validate
```
- O output deverá ser algo assim:
```
>> python -m pip list | findstr spacy
>> python -m spacy validate
spacy              3.8.7
spacy-legacy       3.0.12
spacy-loggers      1.0.5
✔ Loaded compatibility table

================= Installed pipeline packages (spaCy v3.8.7) =================
ℹ spaCy installation:
E:\Workspace\Chatterbot_python_chatbot\Exemplos\NLP\chatbot_nlp\env\lib\site-packages\spacy


NAME             SPACY            VERSION
en_core_web_sm   >=3.8.0,<3.9.0   3.8.0   ✔
```

# Descrição das dependências
- O spaCy dentro do ChatterBot serve basicamente para:
    - Tokenização (separar palavras da frase).
    - POS tagging (identificar a função das palavras: verbo, substantivo, etc.).
    - Similaridade semântica (medir o quanto uma frase nova parece com frases já conhecidas).

- ChatterBot + spaCy (inglês)
    - Vantagens:
        - O bot consegue entender variações de frases (ex.: "Oi, tudo bem?" ≈ "Olá, como vai?").
        - Pode generalizar melhor sem precisar treinar com todas as variações possíveis.
    - Desvantagens:
        - Só funciona oficialmente em inglês (en_core_web_sm).

# Rodando os exemplos
```
python Exemplos/ChatbotSimplesPrEn/menuChatbot.py
python Exemplos/MatcherOnly/chatbotSimples.py
python Exemplos/TrabalhandoComDs/chatbotDsExterno.py
python Exemplos/TrabalhandoComDs/chatbotDsSimples.py
```

# Datasts externos (https://huggingface.co/datasets)
- DailyDialog
        - Descrição: Conversas do dia a dia, 13.000 diálogos.
        - Uso: Conversas cotidianas simples.
        - https://huggingface.co/datasets/ConvLab/dailydialog (TrabalhandoComDsExternos)

- Cornell Movie Dialogs
    - Link: cornell movie dialogs
    - Descrição: Diálogos de filmes antigos, bastante variados e naturais.
    - Uso: Conversas mais criativas ou engraçadas.
    - Formato: [speaker1, speaker2] → converter para pares [pergunta, resposta].
    - https://huggingface.co/datasets/cornell_movie_dialogs

- Persona-Chat
    - Link: Persona-Chat
    - Descrição: Conversas com personagens que têm personalidade.
    - Uso: Criar bots com “personalidade”, respostas mais coerentes.
    - Observação: Cada linha tem diálogo + atributos de personalidade, então você precisa extrair apenas os turns para treinar.
    - https://huggingface.co/datasets/persona_chat

- OpenSubtitles (Legendado de filmes)
    - Link: OpenSubtitles
    - Descrição: Legendas de filmes, muito grande (milhões de linhas).
    - Uso: Treinar bots com muitas variações de conversa.
    - Observação: Pode ser necessário filtrar frases curtas e limpas.
    - https://huggingface.co/datasets/opensubtitles

- Outros datasets úteis
    - empathetic_dialogues – Conversas focadas em empatia.
    - blended_skill_talk – Mistura de chit-chat, conhecimentos gerais e empatia.
    - reddit datasets – Conversas de fóruns, mas precisa de limpeza.

# Como saber se dá para usar o dataset no ChatterBot?
Para ChatterBot, o que importa é transformar o dataset em uma lista de pares [pergunta, resposta].
    - Para ChatterBot, qualquer dataset deve ser convertido em pares [pergunta, resposta]
    - Cada dataset do Hugging Face tem documentação mostrando os campos.
    - Por exemplo, no ConvLab/dailydialog:

```
from datasets import load_dataset
dataset = load_dataset("ConvLab/dailydialog")
print(dataset['train'][0])
```

Isso mostra algo como:

```
{'dialog': ['Hello!', 'Hi!', 'How are you?', ...], 'emotion': [...], ...}
```

* Você pode usar dialog para treinar o bot.
* Regra prática: qualquer dataset com sequências de frases ou diálogos pode ser convertido em pares sequenciais para treinar um bot simples com ListTrainer 

# Transformando o dataset em ChatterBot
```
from datasets import load_dataset
from chatterbot.trainers import ListTrainer

dataset = load_dataset("ConvLab/dailydialog")
trainer = ListTrainer(chatbot_en)

# Converte diálogos em pares [pergunta, resposta]
for dialog in dataset['train']:
    turns = dialog['dialog']
    for i in range(len(turns)-1):
        trainer.train([turns[i], turns[i+1]])

```

# Inspecionar o banco de trainamento
Usar alguma ferramenta para fazer consultas no SqLite, ou rodar o comando abaixo, dentro da basta db:
```
 python .\listarDadosDb.py
 ```

# Spacy models
https://spacy.io/models
https://spacy.io/models/en