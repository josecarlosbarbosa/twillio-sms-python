# Download the helper library from https://www.twilio.com/docs/python/install
import os

from twilio.rest import Client
from dotenv      import load_dotenv

load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

sender_num   = os.getenv('SENDER_NUMBER')
receiver_num = os.getenv('RECEIVER_NUMBER')

base_msg = f'''
        Olá, estou enviando uma mensagem via SMS
        para teste da API Twillio.
            '''

message = client.messages.create(
                              from_=sender_num,
                              to=receiver_num,
                              body=base_msg
                          )

print(message.sid)