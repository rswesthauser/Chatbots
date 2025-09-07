#%pip install --upgrade pip setuptools wheel
#%pip install git+https://github.com/gunthercox/ChatterBot.git
#%pip install spacy
#!python -m spacy download pt_core_news_sm

import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import html
import logging
import sqlite3
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.comparisons import SpacySimilarity
from chatterbot.comparisons import JaccardSimilarity
logging.basicConfig(level=logging.INFO)

nlp = spacy.load("pt_core_news_md")
DB = "SUPORTE_TECNICO.sqlite3"

acoes = {
      "abrir_ticket": abrir_ticket,
      "pesquisar_ordem_servico": pesquisar_ordem_servico,
      "listar_tickets": mostrar_tickets
  }

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            problema TEXT
        )
    """)
    conn.commit()
    conn.close()


def salvar_ticket(marca, problema):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (marca, problema) VALUES (?, ?)", (marca, problema))
    conn.commit()
    conn.close()
    print(f"Ticket salvo no banco com sucesso!")



def listar_tickets():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT id, marca, problema FROM tickets")
    rows = cursor.fetchall()
    conn.close()
    return rows


def clean_whitespace(text: str) -> str:
    return ' '.join(text.split()).replace('\t', ' ')


def unescape_html(text: str) -> str:
    return html.unescape(text)


def convert_to_ascii(text: str) -> str:
    return text.encode("ascii", "ignore").decode()


def aplicar_preprocessors(frase: str) -> str:
    frase = clean_whitespace(frase)
    frase = unescape_html(frase)
    frase = convert_to_ascii(frase)
    return frase


def mostrar_tickets(user_input=None):
    tickets = listar_tickets()
    if not tickets:
        print("Nenhum ticket encontrado.")
    else:
        print("\nLista de Tickets:")
        for t in tickets:
            print(f"   #{t[0]} - Marca: {t[1]} | Problema: {t[2]}")
        print("")


def abrir_ticket(descricao):
    descricao_nlp = nlp(descricao)

    marca = [ent.text for ent in descricao_nlp.ents if ent.label_ in ["ORG", "PRODUCT"]]
    if not marca:
        for token in descricao_nlp:
            if token.text.lower() in ["dell", "lenovo", "asus", "acer", "hp", "positivo", "apple"]:
                marca = [token.text]
                
    defeito = descricao
    if marca:
        for m in marca:
            defeito = defeito.replace(m, "").strip()

    marca_final = marca[0] if marca else "Não informada"
    salvar_ticket(marca_final, defeito)

    print("\n Ticket aberto com sucesso!")
    print(f"Marca: {marca[0] if marca else 'Não informada'}")
    print(f"Problema: {defeito}\n")


def pesquisar_ordem_servico():
    print("Pesquisando OS")


def criacao_chatbot():
  chatbot = ChatBot(
      "SuporteNotebook",
      statement_comparison_function=LevenshteinDistance,
      logic_adapters=[
          {
              "import_path": "chatterbot.logic.BestMatch",
              "default_response": "Me desculpe, não consegui entender.",
              "maximum_similarity_threshold": 0.95
          }
      ],
      read_only=True
  )
  return chatbot


def treinamento_chatbot(chatbot):
  trainer = ListTrainer(chatbot)

  trainer.train([
      "Oi", "Olá! Bem-vindo ao suporte de notebooks.",
      "Olá", "Oi! Como posso ajudá-lo hoje?",

      "Quero abrir um ticket", "abrir_ticket", "Claro! Qual é o problema do seu notebook?",
      "Meu notebook não liga", "Ticket aberto: seu problema foi registrado. Nosso time entrará em contato.",
      "Tela preta", "Ticket aberto: problema registrado. Aguarde nosso retorno.",

      "Qual o status do meu ticket?", "Seu ticket está em análise pelo suporte técnico.",
      "Consultar ticket", "O status do seu ticket é: em análise.",
      "Consultar ordem de serviço", "pesquisar_ordem_servico"

      "Fechar ticket", "Ticket encerrado. Obrigado por usar nosso suporte!",

      "Obrigado", "De nada! Estamos aqui para ajudar.",
      "Valeu", "Por nada! Fico feliz em ajudar.",

      "Quero listar os tickets", "listar_tickets",
      "listar ticket", "listar_tickets",
      "Quero ver todos os tickets do sistema", "listar_tickets"
  ])


#Pipeline
def processar_entrada(user_input, chatbot):
    print("\n Entrada original:", repr(user_input))

    #lematização e remoção de stopwords
    user_input_nlp = nlp(user_input)
    tokens_limpos = [token.lemma_.lower() for token in user_input_nlp if not token.is_stop]
    frase_spacy = " ".join(tokens_limpos)
    print("Depois do spaCy:", frase_spacy)

    #preprocessadores
    frase_clean = aplicar_preprocessors(frase_spacy)
    print("Depois dos preprocessors:", frase_clean)

    #resposta
    response = chatbot.get_response(frase_clean)
    print("Resposta do bot:", response)

    #resposta ou ação
    response_no_nlp = chatbot.get_response(user_input)
    if str(response_no_nlp) in acoes:
        acoes[str(response_no_nlp)](user_input)
    elif str(response) in acoes:
        acoes[str(response_no_nlp)](user_input)
    else:
        print("Resposta no nlp bot:", response_no_nlp)


def looping_conversa():
  chatbot = criacao_chatbot()
  treinamento_chatbot(chatbot)
  init_db()
  print("Digite 'sair' para encerrar.\n")
  while True:
      user_input = input("Você: ")
      if user_input.lower() in ["sair", "exit"]:
          break
      processar_entrada(user_input, chatbot)

looping_conversa()
#Teste "Quero abrir um ticket para meu notebook Lenovo que não carrega"
#      "Quero abrir um ticket para meu notebook DELL com a tela quebrada"
#      "Quero abrir um ticket para meu notebook CCE que explodiu"
#      "quero listar os tickets"