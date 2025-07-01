import requests
import os
def sendMessage(message,chatID, token):
    urlSendMessage = f'https://api.telegram.org/bot{token}/sendMessage'

    try:
        response = requests.post(urlSendMessage, json={'chat_id': chatID, 'text': message})
        print("resposta", response.text)
        
    except Exception as e:
        print("deu ruim", e)


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MENSAGEM = 'Anti-concepcional ! :D'


sendMessage(MENSAGEM, CHAT_ID, BOT_TOKEN)
  
