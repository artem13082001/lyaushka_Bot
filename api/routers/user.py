from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends
from uuid import UUID
from db.models.model_user import User
from db.models.model_items import Item


from db.session import get_db

router_user = APIRouter()
class CreateUserRequest(BaseModel):
    name: str


@router_user.get('/get_user_data')
def get_user(user_id: UUID, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return {
        "name": user.name,
        "inventory_items": user.inventory_items,
        "inventory_case": user.inventory_case,
    }

@router_user.post('/create_user')
def create_user(name: str, db: Session=Depends(get_db)):
    u = User(
        name = name
    )
    db.add(u)
    db.commit()
    db.flush()

    return "OK"

@router_user.delete('/delete_user')
def delete_user(user_id: UUID, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=421,
            detail="Пользователь не найден"
        )
    db.delete(user)
    db.commit()
    db.flush()

    return "OK"

@router_user.post('/update_user')
def update_user(user_id: UUID, name: str | None = None, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user.name = name
    db.commit()
    db.flush()
    return "OK"

@router_user.post("/sell_item")
def sell_item(name: str, name_item: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == name).first()
    item = db.query(Item).filter(Item.name == name_item).first()
