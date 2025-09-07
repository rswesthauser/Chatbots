from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.logic import LogicAdapter 
from chatterbot.conversation import Statement
from transformers import pipeline

self.generator = pipeline(
    "text-generation",
    model="distilgpt2",
    device=-1,
    pad_token_id=50256 #Definir o pad_token_id explicitamente
)

class HuggingFaceAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters=None):
        prompt = input_statement.text

        output = self.generator(
            input_statement.text,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7
        )[0]['generated_text']

        response_statement = Statement(text=output)
        response_statement.confidence = 0.9

        return response_statement

chatbot = ChatBot(
    "HuggingFaceBot",
    logic_adapters=[{
        "import_path": "__main__.HuggingFaceAdapter"
    }]
)

print("🤖 Bot pronto! Pergunte algo:")

while True:
    user_input = input("Você: ")
    resposta = chatbot.get_response(user_input)
    print("Bot:", resposta)
