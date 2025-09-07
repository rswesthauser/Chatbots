from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "MeuBotPT",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    read_only=True,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Desculpe, não entendi. Pode reformular?",
            "maximum_similarity_threshold": 0.80
        }
    ]
)

trainer = ListTrainer(chatbot)

trainer.train([
    "Oi", "Olá!",
    "Olá", "Oi!",
    "Oi, tudo bem?", "Tudo ótimo, e você?",
    "Como você está?", "Estou bem, obrigado!",
    "Bom dia", "Bom dia! Como você está?",
    "Boa tarde", "Boa tarde! Tudo bem?",
    "Boa noite", "Boa noite! Como foi seu dia?",

    "Qual é o seu nome?", "Meu nome é MeuBot.",
    "Quem é você?", "Sou o MeuBot, seu assistente virtual.",
    "Você é humano?", "Não, sou um programa de computador.",
    "Você é um robô?", "Sim, sou um robô programado para conversar.",

    "Tchau", "Até logo!",
    "Adeus", "Até mais!",
    "Sair", "Até logo!",
    "Nos vemos", "Até a próxima!",

    "Obrigado", "De nada!",
    "Obrigada", "De nada!",
    "Por favor", "Sim?",
    "Desculpe", "Não tem problema!",
    "Com licença", "Pode passar, sem problemas!",

    "Estou triste", "Sinto muito. Quer conversar sobre isso?",
    "Estou feliz", "Que bom! Fico feliz por você.",
    "Como você se sente?", "Eu não tenho sentimentos, mas estou pronto para ajudar!",
    "Você está bem?", "Estou funcionando perfeitamente!",

    "Que horas são?", "Não sei responder isso ainda.",
    "Qual é a data de hoje?", "Não consigo ver o calendário no momento.",
    "O que você faz?", "Posso conversar com você e responder perguntas simples.",
    "Você pode me ajudar?", "Claro! Pergunte o que quiser.",
    "Você sabe matemática?", "Posso tentar ajudar com cálculos simples.",
    "Qual é a capital do Brasil?", "Brasília é a capital do Brasil.",
    "Quantos estados tem o Brasil?", "O Brasil tem 26 estados e 1 Distrito Federal.",
    "Qual é a maior cidade do Brasil?", "São Paulo é a maior cidade do Brasil.",
    "Qual é o idioma do Brasil?", "O idioma oficial é o português.",
    "Quem descobriu o Brasil?", "Pedro Álvares Cabral em 1500.",

    "Conte uma piada", "Por que o computador foi ao médico? Porque ele estava com vírus!",
    "Você gosta de música?", "Eu gosto de letras de música, mas não consigo ouvir som.",
    "Qual é o animal mais rápido?", "O guepardo é o animal terrestre mais rápido.",
    "Qual é o maior animal?", "A baleia azul é o maior animal do planeta.",
    "Quantos planetas existem no sistema solar?", "Oito planetas: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno.",
    "Quem é Albert Einstein?", "Um físico famoso que desenvolveu a teoria da relatividade.",

    "Como está o clima?", "Não consigo acessar informações do tempo no momento.",
    "Você gosta de comida?", "Não como, mas posso falar sobre receitas.",
    "Qual é a sua cor favorita?", "Não tenho preferências, mas gosto de azul!",
    "Você dorme?", "Não, eu não preciso dormir.",

    "O que é Python?", "Python é uma linguagem de programação popular.",
    "Você conhece Java?", "Sim, Java é outra linguagem de programação muito usada.",
    "O que é inteligência artificial?", "É a simulação da inteligência humana por máquinas.",
    "O que é um robô?", "Um robô é uma máquina programável que realiza tarefas.",

    "Você pode aprender?", "Não durante esta conversa, estou em modo read-only.",
    "Como aprender programação?", "Comece com Python e pratique pequenos projetos.",

    "Qual é a capital da França?", "Paris é a capital da França.",
    "Qual é a moeda do Brasil?", "O real é a moeda do Brasil.",
    "Qual é a moeda dos EUA?", "O dólar é a moeda dos Estados Unidos.",
    "Quem é o presidente do Brasil?", "Isso muda com o tempo, mas atualmente você pode checar na internet.",
])

print("Digite 'sair' para encerrar a conversa.\n")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Bot: Até logo!")
        break
    resposta = chatbot.get_response(pergunta)
    print("Bot:", resposta)
