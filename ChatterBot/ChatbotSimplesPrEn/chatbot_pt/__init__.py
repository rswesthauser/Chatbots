from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

DB_PATH = "db/chatbot_pt.sqlite3"

chatbot_pt = ChatBot(
    "MeuBotPT",
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

trainer_pt = ListTrainer(chatbot_pt)

trainer_pt.train([
    "Oi", "Olá!",
    "Como você está?", "Estou bem, obrigado!"
])
