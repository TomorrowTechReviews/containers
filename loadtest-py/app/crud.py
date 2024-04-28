from sqlalchemy.orm import Session
from sqlalchemy import text
from uuid import UUID
from .models import Chat, ChatMessage
from .schemas import ChatCreate, ChatMessageCreate

# For the sake of simplicity, we are using a hardcoded user ID.
USER_ID = "0d03d19f-d3af-4e76-89b9-11909a39b2c9"


def get_chat(db: Session, chat_id: int):
    return db.query(Chat).filter(Chat.id == chat_id).first()


def get_chats_by_user(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return (
        db.query(Chat).filter(Chat.user_id == user_id).offset(skip).limit(limit).all()
    )


def create_chat(db: Session, chat: ChatCreate, user_id: str):
    db_chat = Chat(title=chat.title, user_id=user_id)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def create_chat_message(
    db: Session, chat_message: ChatMessageCreate, chat_id: UUID, user_id: str
):
    db_message = ChatMessage(
        chat_id=chat_id,
        message=chat_message.message,
        role=chat_message.role,
        user_id=user_id,
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def seed_db(db: Session):
    chat_data = [
        {"title": f"Sample Chat {i}", "user_id": USER_ID} for i in range(100000)
    ]
    db.bulk_insert_mappings(Chat, chat_data)
    chat_ids = db.execute(text("SELECT id FROM chats")).fetchall()

    message_data = [
        {
            "chat_id": chat_id[0],
            "message": "Hello, this is a test message.",
            "role": "user",
            "user_id": USER_ID,
        }
        for chat_id in chat_ids
    ]
    db.bulk_insert_mappings(ChatMessage, message_data)
    db.commit()
