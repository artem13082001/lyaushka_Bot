from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
from uuid import UUID
from db.models.model_user import User
from db.models.model_items import Item
from db.session import get_db

router_balance = APIRouter()
class CreateUserRequest(BaseModel):
    name: str

# balance_router.py
from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from db.models.model_user import User

router = APIRouter(prefix="/balance")

@router.get("/get_balance")
def get_balance(name: str):
    # name здесь — это Telegram ID из запроса
    db: Session = next(get_db())
    user = db.query(User).filter(User.tg_id == name).first()
    if not user:
        return {"balance": 0.0}
    return {"balance": float(user.balance)}
