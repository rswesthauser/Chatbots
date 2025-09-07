#%pip install --upgrade pip setuptools wheel
#%pip install git+https://github.com/gunthercox/ChatterBot.git
#%pip install numpy
#%pip install spacy
#%pip install chatterbot-corpus
#!python -m spacy download en_core_web_sm

import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    "ChatbotNlpCorpora",
    logic_adapters=["chatterbot.logic.BestMatch"],
    read_only=True
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")#https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    doc = nlp(user_input)

    tokens = [token.lemma_.lower() for token in doc if not token.is_stop]
    processed_input = " ".join(tokens)

    response = chatbot.get_response(processed_input)
    print("Bot (nlp):", response)

    responseNoNlp = chatbot.get_response(user_input)
    print("Bot:", responseNoNlp)