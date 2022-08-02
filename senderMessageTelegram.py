import requests
from fuelCost import fuelCost


def senderMessageTelegram(token, message):
    r = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    chatId = r.json()['result'][0]['message']['chat']['id']
    requests.get(
        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={message}")


senderMessageTelegram(
    '389265589:AAGZlad75Rfi1Mvw3vcrT6ksnJvj_rJq01g', fuelCost())
