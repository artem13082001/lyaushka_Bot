from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from db.models.model_user import User
from db.session import get_db
router_inventory = APIRouter(prefix="/inventory", tags=["inventory"])

@router_inventory.post("/add")
def add_item(
    user_id: UUID,
    item_name: str,
    quantity: int = 1,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    user.inventory_items += f",{item_name}" * quantity

    db.commit()
    db.flush()

    return "OK"

@router_inventory.get("/get_inventory_cases")
def get_inventory_cases(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == name).first()

    inv_c = user.inventory_case

    return inv_c

@router_inventory.get("/get_inventory_items")
def get_inventory_items(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == name).first()

    inv_c = user.inventory_items

    return inv_c
