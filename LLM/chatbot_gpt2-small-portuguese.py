#%pip install transformers
#https://huggingface.co/pierreguillou/gpt2-small-portuguese

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("pierreguillou/gpt2-small-portuguese")
model = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese")

print("Chatbot em português (digite 'quit' para sair)")

chat_history_ids = None

while True:
    user_input = input("Você: ")
    if user_input.strip().lower() == "quit":
        print("Bot: Adeus!")
        break

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        attention_mask=torch.ones(bot_input_ids.shape, dtype=torch.long),
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=80,
        top_p=0.95,
        temperature=0.8,
        repetition_penalty=1.2
    )

    bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {bot_reply}")   
