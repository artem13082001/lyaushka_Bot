import random
from random import randint

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from requests import session
from sqlalchemy.orm import Session
from fastapi import Depends
from starlette import status
from uuid import UUID
from db.models.model_user import User
from db.models.model_case import Case

from sqlalchemy import and_

from db.session import get_db

router_case = APIRouter()
class CaseSchema(BaseModel):
    name: str
    is_limited: str
    price: str
    type: str
cases = ["kilokvak", "prismatic frog", "frog bite", "dark frog", "rattling frog", "lyagushki and nightmares"]
@router_case.post('/get_random_case')
def get_random_case_by_id(name: str, db:Session=Depends(get_db)) -> CaseSchema:
    rc = random.choice(cases)
    case = db.query(Case).filter(Case.name == rc).first()
    user = db.query(User).filter(User.name == name).first()
    user.inventory_case += f",{case.name}"
    db.commit()
    db.flush()
    return CaseSchema(
        name = case.name,
        is_limited = case.is_limited,
        price = case.price,
        type = case.type
    )

items = {
    "kilokvak":[
        "Dual Berettas frog",
        "frogva",
        "Kva-9",
        "KVAK-10",
        "LGSH-08"

    ],
    "prismatic frog": [
        "KAMAS",
        "Kvak-18",
        "MP7",
        "Five-fRogs",
        "AKVA-47"
    ],
    "frog bite": [
        "Kvalimp",
        "Kvak-18",
        "Dual Frog",
        "UMP-8"
    ],
    "dark frog": [
        "AK-47",
        "G3SG1",
        "FAMAS",
        "MAG-7"
    ],
    "rattling frog": [
        "puga",
        "lol",
        "kek"
    ],
    "lyagushki and nightmares": [
        "puga",
        "lol",
        "kek"
    ]



         }

@router_case.post('/krutka_case')
def krutka_case(name: str, case_name: str, db: Session=Depends(get_db)) -> str:
    user = db.query(User).filter(User.name == name).first()
    if case_name not in user.inventory_case:
        return "У вас нет этого кейса"
    list_items = items[case_name]
    name_item = random.choice(list_items)
    user.inventory_items += f",{name_item}"
    user.inventory_case = user.inventory_case.replace(f",{case_name}","")
    db.commit()
    db.flush()
    return name_item