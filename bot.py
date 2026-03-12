import requests
import time
import random
from datetime import datetime
import pytz

TOKEN = "8681180706:AAFsLuGC7uEgazESRF0BMzCVGXZt4boQVss"
CHAT_ID = "@siinaismilionarios"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# fuso horário Brasil
fuso = pytz.timezone("America/Sao_Paulo")

# jogos disponíveis
jogos = {
    "tigrinho": {
        "nome": "🐯 Fortune Tiger",
        "mensagem": "Padrão agressivo detectado no Tigrinho."
    },
    "ox": {
        "nome": "🐂 Fortune Ox",
        "mensagem": "Sequência positiva detectada no Fortune Ox."
    },
    "dragon": {
        "nome": "🐉 Fortune Dragon",
        "mensagem": "Padrão raro identificado no Dragon."
    },
    "slot": {
        "nome": "🎰 Slot Premium",
        "mensagem": "Volatilidade ideal encontrada no Slot Premium."
    }
}

while True:

    # escolhe um jogo aleatório
    chave_jogo = random.choice(list(jogos.keys()))
    jogo = jogos[chave_jogo]

    hora = datetime.now(fuso).strftime("%H:%M")

    # mensagem 1
    msg1 = f"""
🚨 SINAL ENCONTRADO

🎮 Jogo: {jogo["nome"]}
📊 {jogo["mensagem"]}

Preparando entrada...
"""

    enviar(msg1)

    time.sleep(random.randint(10,20))

    # mensagem 2
    msg2 = f"""
🎯 ENTRADA LIBERADA

🎮 Jogo: {jogo["nome"]}
⏰ Horário: {hora}

💰 Estratégia:
Entrada + 2 gales
"""

    enviar(msg2)

    time.sleep(random.randint(60,90))

    # mensagem 3
    resultado = random.choice(["✅ WIN", "❌ LOSS"])

    msg3 = f"""
{resultado}

🎮 {jogo["nome"]}

Fique atento para o próximo sinal.
"""

    enviar(msg3)

    tempo = random.randint(120,600)

    print("Próximo sinal em:", tempo)

    time.sleep(tempo)
