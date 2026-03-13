import requests
import time
import random
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = "8681180706:AAFsLuGC7uEgazESRF0BMzCVGXZt4boQVss"
CHAT_ID = "@siinaismilionarios"
LINK = "https://bit.ly/47BFiyX"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

jogos = [
    "🐯 Fortune Tiger",
    "🐉 Fortune Dragon",
    "🐂 Fortune Ox",
    "🎰 Slot Premium"
]

confiancas = [
    ("🔥", "fraco"),
    ("🔥🔥", "mediano"),
    ("🔥🔥🔥🔥", "forte"),
    ("🔥🔥🔥🔥🔥", "muito forte")
]

simbolos = ["▶️","⚡"]

while True:

    # intervalo entre sinais
    espera = random.randint(480,1200)  # 8 a 20 minutos
    print("Próximo sinal em:", espera)

    time.sleep(espera)

    jogo = random.choice(jogos)

    hora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).strftime("%H:%M")

    enviar(f"""
🚨 SINAL DETECTADO

🎮 Jogo: {jogo}

Preparando entrada...
""")

    time.sleep(random.randint(10,20))

    normal = random.randint(1,20)
    turbo = random.randint(1,20)

    confianca = random.choice(confiancas)

    sequencia = "".join(random.choice(simbolos) for _ in range(12))

    enviar(f"""
NOVA ENTRADA ✅

{jogo}

▶️ Jogadas normal: {normal}
⚡ Jogadas turbo: {turbo}

💪🏽 Confiança: {confianca[0]} ({confianca[1]})
⏰ Válido até: {hora}

🎰 Sequência: {sequencia}

SÓ FUNCIONA AQUI 👇
{LINK}
""")

    time.sleep(random.randint(60,90))

    if random.random() < 0.9:
        enviar(f"""
✅ GREEN CONFIRMADO

{jogo}

Mais um lucro garantido.

Aposte aqui 👇
{LINK}
""")
    else:
        enviar(f"""
❌ LOSS

{jogo}

Mercado variou dessa vez.
Seguimos para o próximo sinal.
""")
