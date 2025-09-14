#!pip install transformers accelerate

from transformers import pipeline

generator = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")

def get_weather(city): #Função externa simulada (como se fosse uma API). Podemos imaginar isso como sendo uma API interna que apenas a LLM irá acessar.
    return f"A previsão para {city} é de 24°C e ensolarado."

def chatbot_with_mcp(user_input): #Função que simula MCP: decide se chama ferramenta ou não
    response = generator(user_input, max_new_tokens=50, do_sample=True, temperature=0.7)[0]["generated_text"]

    if "previsão" in user_input.lower():
        if "para" in user_input:
            city = user_input.split("para")[-1].strip().replace("?", "")
        else:
            city = "sua cidade"
        tool_result = get_weather(city)
        return f"(Ferramenta via MCP) {tool_result}"
    else:
        return f"(LLM) {response}"

print(chatbot_with_mcp("Qual a previsão para Porto Alegre?"))
print(chatbot_with_mcp("Me conte uma piada"))
print(chatbot_with_mcp("Oi, tudo bem?"))