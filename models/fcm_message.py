from pydantic import BaseModel

class FCMMessage(BaseModel):
    title: str
    body: str