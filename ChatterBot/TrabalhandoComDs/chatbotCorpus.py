from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot_en = ChatBot(
    "ChatBotDs",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace', 
        'chatterbot.preprocessors.unescape_html', 
        'chatterbot.preprocessors.convert_to_ascii' 
    ],
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry, I did not understand.",
            "maximum_similarity_threshold": 0.80
        }
    ]
)

trainer_en = ListTrainer(chatbot_en)

trainer_en.train("chatterbot.corpus.english.greetings.yml")
trainer_en.train("chatterbot.corpus.english.conversations.yml")

print("Type 'exit' to finish the conversation.\n")
while True:
    pergunta = input("You: ")
    if pergunta.lower() in ["exit", "quit"]:
        print("Bot: See you later!")
        break
    resposta = chatbot_en.get_response(pergunta)
    print("Bot:", resposta)
