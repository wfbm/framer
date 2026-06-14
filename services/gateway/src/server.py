from fastapi import Request, FastAPI
from .api_v1 import webhook

app = FastAPI()

app.include_router(webhook.router)
