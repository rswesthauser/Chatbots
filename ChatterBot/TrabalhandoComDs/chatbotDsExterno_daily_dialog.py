from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datasets import load_dataset
import sqlite3
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.comparisons import SpacySimilarity
import spacy

nlp = spacy.load("en_core_web_md")
SpacySimilarity.nlp = nlp
DB_PATH = "db/daily_dialog.sqlite3" 

def db_has_data(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM statement;")
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
    except Exception:
        return False
    

def chatbot_creation():
    chatbot = ChatBot(
        "ChatBotDs",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=f"sqlite:///{DB_PATH}",  
        statement_comparison_function=SpacySimilarity,
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
                "maximum_similarity_threshold": 0.80,
                "statement_comparison_function": "chatterbot.comparisons.spacy_similarity"
            }
        ]
    )
    return chatbot

def chatbot_training(chatbot):
    trainer = ListTrainer(chatbot)

    if not db_has_data(DB_PATH):
        print(" Training chatbot for the first time...")
        dataset = load_dataset("daily_dialog", split="train")

        for dialog in dataset['dialog']:
            if len(dialog) > 1:
                trainer.train(dialog)

        print(" Training finished and saved to DB!")
    else:
        print(" Database already trained, skipping training.")

def chat_looping(chatbot):
    print("\nChatBot is ready! Type 'exit' or 'quit' to stop.\n")
    while True:
        pergunta = input("You: ")
        if pergunta.lower() in ["exit", "quit"]:
            print("Bot: See you later!")
            break
        resposta = chatbot.get_response(pergunta)
        print("Bot:", resposta)


if __name__=='__main__':
    chatbot = chatbot_creation()
    chatbot_training(chatbot)
    chat_looping(chatbot)