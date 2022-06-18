from lib2to3.pgen2 import token
import firebase_admin
import os.path
import starlette.responses

from fastapi import FastAPI
from firebase_admin import credentials
from firebase_admin import messaging

from models.fcm_message import FCMMessage
from models.fcm_token import FCMToken

app = FastAPI(title='qTorrentNotifier')
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

@app.get('/', include_in_schema=False)
async def redirect_root():
    return starlette.responses.RedirectResponse('/redoc')

@app.post('/api/v1/registerToken')
async def register_token(fcm_token: FCMToken):
    with open('Token.txt', 'w') as token_file:
        token_file.write(fcm_token.token)
    return 'Done'

@app.post('/api/v1/sendMessage')
async def send_message(fcm_message: FCMMessage):
    with open('Token.txt', 'r') as token_file:
        registration_token = token_file.readline()
        message = messaging.Message(
            notification = messaging.Notification(
                title = fcm_message.title,
                body = fcm_message.body,
            ),
            token = registration_token
        )
        messaging.send(message)
    return 'Done'