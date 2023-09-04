import requests

def send_to_telegram(message):

    apiToken = '6138535917:AAHzvm8z4VgoTCczWCDXMJaX_b8HdV9oGus'
    chatID = '5214657416'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
