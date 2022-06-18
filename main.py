import firebase_admin
import starlette.responses

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from firebase_admin import credentials
from firebase_admin import messaging

app = FastAPI(title='qTorrentNotifier')
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

@app.get('/', include_in_schema=False)
async def redirect_root():
    return starlette.responses.RedirectResponse('/redoc')

@app.get('/api/v1/registerToken')
async def register_token(token: str):
    with open('Token.txt', 'w') as token_file:
        token_file.write(token)
    return PlainTextResponse('Done')

@app.get('/api/v1/sendMessage')
async def send_message(title: str, body: str):
    with open('Token.txt', 'r') as token_file:
        registration_token = token_file.readline()
        message = messaging.Message(
            notification = messaging.Notification(
                title = title,
                body = body,
            ),
            token = registration_token
        )
        messaging.send(message)
    return PlainTextResponse('Done')