from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

DB_PATH = "db/chatbot_en.sqlite3"

chatbot_en = ChatBot(
    "MyBotEN",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{DB_PATH}",
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace', #Remove espaços em branco extras
        'chatterbot.preprocessors.unescape_html', #Converte de HTML para texto simples
        'chatterbot.preprocessors.convert_to_ascii' #Converte ncaracteres especiais para ASCII
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

# Treinamento básico
trainer_en.train([
    "Hello", "Hi!",
    "How are you?", "I'm fine, thank you.",
    "What is your name?", "My name is MyBot.",
    "Goodbye", "Bye!",
])
