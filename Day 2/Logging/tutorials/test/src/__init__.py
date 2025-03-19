from fastapi import FastAPI
import os

from src.utils import get_logger

logger = get_logger(__name__)
logger.info(f"Logger created in {__name__}")

app = FastAPI()
logger.info(f"FastAPI app created in {__name__}")

def create_app():
    return app

@app.get("/")
def read_root():
    return {"Hello": "World"}


