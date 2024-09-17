import json, random
from googletrans import Translator
from twilio.rest import Client

traduttore = Translator()

def load_quotes():
    with open('citazioni.json', 'r', encoding='utf-8') as file:
        citazioni = json.load(file)
    return citazioni

citazioni = load_quotes()
random_quote = random.choice(citazioni)

def traduci_citazione(citazione):
    traduzione = traduttore.translate(citazione['quote'], src='en', dest='it')
    return traduzione.text

tradotta = traduci_citazione(random_quote)
print(tradotta)

account_sid = "ACf0a79eeb7e2a133f483c3e0bed5514e5"
auth_token = "#inserisci il tuo token"
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=tradotta,
  to='whatsapp:+393533641788'
)

print(message.sid)

recovery_code = "JUK7LYMM28FYH7G63FV5KWFE"
