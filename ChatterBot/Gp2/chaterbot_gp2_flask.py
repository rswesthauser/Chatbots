from transformers import GPT2LMHeadModel, GPT2Tokenizer

print("Starting application...")

app = Flask(__name__)

print("Loading model and tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained("openai-community/gpt2")
model = GPT2LMHeadModel.from_pretrained("openai-community/gpt2")

print("Model and tokenizer loaded.")

chat_history = []

def generate_response(prompt):
    print(f"Generating response for prompt: {prompt}")
    inputs = tokenizer.encode(prompt, return_tensors="pt") #https://huggingface.co/docs/transformers/main_classes/tokenizer
    outputs = model.generate(
        inputs, 
        max_length=100,  
        num_beams=5,    
        early_stopping=True,
        no_repeat_ngram_size=2,  
        temperature=0.7,  
        top_k=50,         
        top_p=0.95        
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated response: {response}")
    return response

while True:
    user_input = input("Você: ")
    response = generate_response(user_input)
    print("Bot:", resporesponsesta)
