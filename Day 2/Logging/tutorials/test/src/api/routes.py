from src import logger

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}

