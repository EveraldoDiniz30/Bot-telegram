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

sequencia_simbolos = ["▶️", "⚡"]

while True:

    jogo = random.choice(jogos)

    fuso = ZoneInfo("America/Sao_Paulo")
    hora = datetime.now(fuso).strftime("%H:%M")

    # mensagem 1
    msg1 = f"""
🚨 SINAL DETECTADO

🎮 Jogo: {jogo}

Analisando padrão de entrada...
Prepare-se 👀
"""

    enviar(msg1)

    time.sleep(random.randint(10,20))

    jogadas_normal = random.randint(1,20)
    jogadas_turbo = random.randint(1,20)

    confianca = random.choice(confiancas)

    sequencia = "".join(random.choice(sequencia_simbolos) for _ in range(12))

    # mensagem 2
    msg2 = f"""
NOVA ENTRADA ✅

{jogo}

▶️ Jogadas normal: {jogadas_normal}
⚡ Jogadas turbo: {jogadas_turbo}

💪🏽 Confiança: {confianca[0]} ({confianca[1]})
⏰ Válido até: {hora}

🎰 Sequência: {sequencia}

SÓ FUNCIONA AQUI 👇🏻👇🏻👇🏻
{LINK}
"""

    enviar(msg2)

    time.sleep(random.randint(60,90))

    # 90% win
    resultado = "WIN" if random.random() < 0.9 else "LOSS"

    if resultado == "WIN":
        msg3 = f"""
✅ GREEN CONFIRMADO

{jogo}

Lucro garantido novamente 🔥

Aposte aqui 👇🏻
{LINK}
"""
    else:
        msg3 = f"""
❌ LOSS

{jogo}

Mercado variou dessa vez.

Recupere no próximo sinal 👇🏻
{LINK}
"""

    enviar(msg3)

    # intervalo 8–25 minutos
    tempo = random.randint(480,1500)

    print("Próximo sinal em:", tempo)

    time.sleep(tempo)

