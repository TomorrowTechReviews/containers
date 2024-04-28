from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import ChatCreate, Chat
from ..dependencies import get_db
from .. import crud

router = APIRouter()
# For the sake of simplicity, we are using a hardcoded user ID.
USER_ID = "0d03d19f-d3af-4e76-89b9-11909a39b2c9"


@router.get("/chats", response_model=list[Chat])
def list_chats(db: Session = Depends(get_db)):
    return crud.get_chats_by_user(db=db, user_id=USER_ID)


@router.post("/chats", response_model=Chat)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return crud.create_chat(db=db, chat=chat, user_id=USER_ID)


@router.get("/seed", response_model=str)
def seed_db(db: Session = Depends(get_db)):
    crud.seed_db(db=db)
    return "DB seeded!"
