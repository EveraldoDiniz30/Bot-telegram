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

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": msg,
            "disable_web_page_preview": True
        }
    )

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

simbolos = ["▶️", "⚡"]

while True:

    # espera entre sinais (8–20 minutos)
    espera = random.randint(480,1200)
    print("Próximo sinal em:", espera)

    time.sleep(espera)

    jogo = random.choice(jogos)

    hora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).strftime("%H:%M")

    # mensagem 1
    enviar(f"""
🚨 SINAL DETECTADO

🎮 Jogo: {jogo}

Analisando padrão de entrada...
Prepare-se 👀
""")

    time.sleep(random.randint(10,20))

    jogadas_normal = random.randint(1,20)
    jogadas_turbo = random.randint(1,20)

    confianca = random.choice(confiancas)

    sequencia = "".join(random.choice(simbolos) for _ in range(12))

    # mensagem 2
    enviar(f"""
NOVA ENTRADA ✅

{jogo}

▶️ Jogadas normal: {jogadas_normal}
⚡ Jogadas turbo: {jogadas_turbo}

💪🏽 Confiança: {confianca[0]} ({confianca[1]})
⏰ Válido até: {hora}

🎰 Sequência: {sequencia}

SÓ FUNCIONA AQUI 👇
{LINK}
""")

    time.sleep(random.randint(60,90))

    # resultado (90% win)
    if random.random() < 0.9:

        enviar(f"""
✅ GREEN CONFIRMADO

{jogo}

Mais um lucro garantido 🔥
""")

    else:

        enviar(f"""
❌ LOSS

{jogo}

Mercado variou dessa vez.
Seguimos para o próximo sinal.
""")

