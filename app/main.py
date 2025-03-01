from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.routers import router

load_dotenv()

app = FastAPI()

app.include_router(router)
