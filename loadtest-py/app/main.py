from fastapi import FastAPI
from . import models
from .database import engine
from .routers import chats

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(prefix="/v1", router=chats.router)

@app.get("/health")
async def root():
    return "OK"
