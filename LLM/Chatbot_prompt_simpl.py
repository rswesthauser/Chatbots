#%pip install transformers
#https://huggingface.co/tiiuae/falcon-7b-instruct


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

print("Falcon 7B Instruct chatbot in English (type 'quit' to exit)")

chat_history = []
max_history = 3

#system_instruction = "You are a virtual assistant that always responds in English, clearly and politely.\n" #Prompt engineering (prefix instruction)

system_instruction = ( #Prefix instruction + few-shot examples
    "You are a helpful assistant. Always respond in English, clearly, politely, and in a few sentences.\n"
    "Example interactions:\n"
    "User: Hello\n"
    "Bot: Hi! How can I help you today?\n"
    "User: What is the capital of France?\n"
    "Bot: The capital of France is Paris.\n"
)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    chat_history.append(f"User: {user_input}\nBot:")

    if len(chat_history) > 3:  #Limita o histórico
        chat_history = chat_history[-3:]

    prompt = system_instruction + "\n".join(chat_history) #Monta o prompt completo

    input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

    # Geração da resposta
    chat_history_ids = model.generate(
        input_ids,
        max_new_tokens=150,  #limita tamanho da resposta
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decodifica apenas a nova parte
    bot_reply = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()
    print(f"Bot: {bot_reply}")

    # Adiciona a resposta ao histórico
    chat_history[-1] += f" {bot_reply}"