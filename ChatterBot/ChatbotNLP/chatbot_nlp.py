#%pip install --upgrade pip setuptools wheel
#%pip install git+https://github.com/gunthercox/ChatterBot.git
#%pip install spacy
#!python -m spacy download pt_core_news_sm

import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

nlp = spacy.load("pt_core_news_sm") #Carregar modelo em português

chatbot = ChatBot(
    "NotebookBot",
    logic_adapters=["chatterbot.logic.BestMatch"],
    read_only=True
)

trainer = ListTrainer(chatbot)

trainer.train([
    "Oi",
    "Olá! Seja bem-vindo ao suporte de notebooks.",
    "Meu notebook não liga",
    "Verifique se o carregador está conectado corretamente.",
    "A tela está preta",
    "Tente reiniciar pressionando o botão power por 10 segundos.",
    "Valeu",
    "De nada, estamos aqui para ajudar!"
])

print("Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit"]:
        break

    doc = nlp(user_input) #Usar o spacy para processar a entrada do usuário

    #Lematiação e remoção de stopwords (NLP)
    # Lematização é o processo de reduzir uma palavra à sua forma “de dicionário” (o lema)
    # Ex: ligando, liguei, ligarão = ligar
    #Stopwords são palavras muito comuns que, na maioria das vezes, não mudam o sentido principal da frase.
    #Ex: o, a, de, em, para, um, com, não.
    tokens_limpos = [token.lemma_.lower() for token in doc if not token.is_stop]
    frase_processada = " ".join(tokens_limpos)

    print("[Entrada processada]:", frase_processada)

    # Envia texto processado para o bot
    response = chatbot.get_response(frase_processada)
    print("Bot:", response)
