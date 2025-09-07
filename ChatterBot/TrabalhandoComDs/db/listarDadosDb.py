import sqlite3

conn = sqlite3.connect("chatbot_db.sqlite3")
cursor = conn.cursor()

# Ver as primeiras 10 linhas
cursor.execute("SELECT text, in_response_to, conversation FROM statement LIMIT 10")
for row in cursor.fetchall():
    print(row)

# Contar quantas frases foram salvas
cursor.execute("SELECT COUNT(*) FROM statement")
print("Total de frases:", cursor.fetchone()[0])

conn.close()
