#%pip install transformers
#https://huggingface.co/microsoft/DialoGPT-medium

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import ipywidgets as widgets
from IPython.display import display, clear_output

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("DialoGPT-medium chatbot (type 'quit' to exit)")

chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,    #Input tokenizado que será usado como contexto para gerar o texto
        attention_mask=torch.ones(bot_input_ids.shape, dtype=torch.long), #Indica quais tokens sâo válidos e não padding 
        max_length=1100, #Tamanho máximo da sequência de texto gerada, incluindo tokens de entrada. Um dos motivos pela qual é importante limitar o histórico
        pad_token_id=tokenizer.eos_token_id, #O id do token usado para indicar o fim da sequência, seria o mesmo que o ; no C, indicando o fimd a linha.
        do_sample=True, #Com true gera um texto de forma mais aleatória e variada, com false irá utilizar uma estratégia gulosa, sempre escolhendfo a maior probabilidade.
        top_k=80, #Limita o número de tokens candidatos para gerar cada palavra. Nesse caso o modelo irá gerar a prõxima palavra com base em 80 tokens.
        top_p=0.95, #O modeloe scolhe apenas os tokens cuja soma das probabilidades atingemtop_p, nesse caso 95% de probabilidade cumulativa.
        temperature=0.7 #Controla a aleatoriedade da resposta. Valores próximos de zero, respostas consevadoras e previsíveis, 0,7 xostuam ser um valor mais conservador, enquanto valores ainda mais próximos de 1 geram respostas vistas como "criativas", variadas e talevz incoerentes.
    )
    
    #bot_input_ids + attention_mask: fornece contexto ao modelo.
    #max_length + pad_token_id: controla tamanho e evita erros.
    #do_sample=True + top_k + top_p + temperature: definem estilo e criatividade da resposta.
   

    bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {bot_reply}")
