import requests
import time
import random

TOKEN = "8681180706:AAFsLuGC7uEgazESRF0BMzCVGXZt4boQVss"
CHAT_ID = "@siinaismilionarios"

def enviar_mensagem(texto):

    url = f"https://api.telegram.org/bot8681180706:AAFsLuGC7uEgazESRF0BMzCVGXZt4boQVss/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    requests.post(url, data=payload)


while True:

    hora = time.strftime("%H:%M")

    mensagens = [
        f"🚨 SINAL LIBERADO\nHorário: {hora}\nPrepare entrada",
        f"📊 OPORTUNIDADE DETECTADA\nHorário: {hora}",
        f"⚡ POSSÍVEL ENTRADA\nHorário: {hora}",
        f"🔥 ATENÇÃO PARA O SINAL\nHorário: {hora}"
    ]

    mensagem = random.choice(mensagens)

    enviar_mensagem(mensagem)

    # intervalo aleatório entre 2 e 10 minutos
    tempo_espera = random.randint(120, 600)

    print("Próximo sinal em", tempo_espera, "segundos")

    time.sleep(tempo_espera)