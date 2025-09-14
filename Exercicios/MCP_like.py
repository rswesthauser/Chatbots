#!pip install transformers accelerate

from transformers import pipeline

# TODO: carregue o modelo português
#generator = 

#Funções externas (simulação de APIs)
def get_weather(city):
    return f"A previsão para {city} é de 24°C e ensolarado."

def calculate(expression):
    try:
        result = eval(expression)  # cuidado: apenas para demo
        return f"O resultado é {result}"
    except:
        return "Expressão inválida."

#Função MCP-like
def chatbot_with_mcp(user_input):
    print("Implemente a geracao da resposta pela LLm e atambém a logica de decisao para chamar as funcoes externas")
    # TODO: gere resposta com o modelo Hugging Face
    #response = 

    # TODO: implemente a lógica de decisão


# Teste inicial
print(chatbot_with_mcp("Qual a previsão para Porto Alegre?"))
print(chatbot_with_mcp("Calcule 12 * 7"))
print(chatbot_with_mcp("Oi, tudo bem?"))
