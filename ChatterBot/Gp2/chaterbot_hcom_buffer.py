from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

print("Starting application...")

print("Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

print("Model and tokenizer loaded.")

chat_history = []

def generate_response(user_input):
    chat_history.append(f"User: {user_input}")
    prompt = "\n".join(chat_history) + "\nBot:"

    tokenizer.pad_token = tokenizer.eos_token
    inputs = tokenizer.encode(
        prompt,
        return_tensors="pt",
        padding=True,         
        truncation=True,       
    )
    attention_mask = (inputs != tokenizer.pad_token_id).long()

    outputs = model.generate(
        inputs,
        max_length=200,
        do_sample=True,
        temperature=0.9,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    bot_reply = response.split("Bot:")[-1].strip()
    chat_history.append(f"Bot: {bot_reply}")
    return bot_reply

if __name__ == '__main__':
    print("Starting interactive mode...")
    while True:
        user_input = input("Você: ")
        resposta = generate_response(user_input)
        print("Bot:", resposta)
