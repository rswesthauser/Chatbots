#%pip install transformers
#https://huggingface.co/microsoft/DialoGPT-small

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

print("DialoGPT-small chatbot (type 'quit' to exit)")

chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        attention_mask=torch.ones(bot_input_ids.shape, dtype=torch.long),  
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,        
        top_k=50,              
        top_p=0.95,            
        temperature=0.7       
    )

    bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {bot_reply}")
