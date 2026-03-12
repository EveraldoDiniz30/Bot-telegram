import requests
import time
import random
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = "8681180706:AAFsLuGC7uEgazESRF0BMzCVGXZt4boQVss"
CHAT_ID = "@siinaismilionarios"

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
🚨 NOVO SINAL DETECTADO

🎮 Jogo: {jogo}

Analisando padrão de entrada...
Prepare-se 👀
"""

    enviar(msg1)

    time.sleep(random.randint(10,20))

    # dados aleatórios do sinal
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

SÓ FUNCIONA AQUI, APOSTE AGORA 👇🏻👇🏻👇🏻
"""

    enviar(msg2)

    time.sleep(random.randint(60,90))

    # resultado 90% win
    resultado = "WIN" if random.random() < 0.9 else "LOSS"

    if resultado == "WIN":
        msg3 = f"""
✅ GREEN CONFIRMADO

{jogo}

Mais um lucro garantido.

Fique atento ao próximo sinal 🔥
"""
    else:
        msg3 = f"""
❌ LOSS

{jogo}

Mercado variou dessa vez.

Seguimos para o próximo sinal.
"""

    enviar(msg3)

    tempo = random.randint(120,600)

    print("Próximo sinal em:", tempo)

    time.sleep(tempo)
