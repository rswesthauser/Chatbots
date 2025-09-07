lang = input("Escolha a língua (pt/en): ").lower()

if lang == "pt":
    from chatbot_pt import chatbot_pt as bot
elif lang == "en":
    from chatbot_en import chatbot_en as bot
else:
    print("Idioma não suportado")
    exit()

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Bot: Até logo!" if lang=="pt" else "Bot: Goodbye!")
        break
    resposta = bot.get_response(pergunta)
    print("Bot:", resposta)
