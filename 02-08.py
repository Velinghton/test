import requests

token = "5572048962:AAEnJ4fxPaFHqMiI1SPTimzqC5bsy7AYARM"
root_url = "https://api.telegram.org/bot"
last_message = 0


def get_updates(token):
	
    url = f"{root_url}{token}/getUpdates"
    res = requests.get(url)
    return res.json()

def  send_message(chat_id, message, ):
	url = f"{root_url}{token}/SendMessage"

	response = requests.post(url, json={"chat_id":chat_id, "text": message})
	return response

while  True:
	update = get_updates(token)
	last_mess = update["result"][-1]["message"]["text"]
	chat_id = update["result"][-1]["message"]["chat"]["id"]
	message_id = update["result"][-1]["message"]["message_id"]
	if message_id > last_message:
		send_message(chat_id, last_mess)
		#print(last_mess)
	last_message = message_id	


