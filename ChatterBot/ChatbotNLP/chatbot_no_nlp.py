#%pip install --upgrade pip setuptools wheel
#%pip install git+https://github.com/gunthercox/ChatterBot.git

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "NotebookBot",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Me desculpe, não consegui entender.",
            "maximum_similarity_threshold": 0.95
        }
    ],
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

    #Levenshtein distance
    response = chatbot.get_response(user_input)
    print("Bot:", response)
