#%pip install git+https://github.com/gunthercox/ChatterBot.git

from chatterbot import ChatBot

chatbot = ChatBot(
    "ChatbotAprendizado",
    read_only=False         #Define se o bot irá ou não aprender com a interação
)

print("Digite 'sair' para encerrar a conversa.\n")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Bot: Até logo!")
        break
    resposta = chatbot.get_response(pergunta)
    print("Bot:", resposta)

