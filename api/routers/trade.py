from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from starlette import status
from uuid import UUID
from db.models.model_user import User
from pydantic import BaseModel
from typing import List

from sqlalchemy import and_

from db.session import get_db

router_trade = APIRouter()

class TradeItem(BaseModel):
    item_id: str
    quantity: int

class CreateTradeRequest(BaseModel):
    user_id: str
    counterparty_id: str
    offer_items: List[TradeItem]  # что игрок A отдаёт
    request_items: List[TradeItem]  # что игрок A хочет получить

class TradeResponse(BaseModel):
    trade_id: str
    status: str

@router_trade.post("/trades", response_model=TradeResponse, status_code=status.HTTP_201_CREATED)
def accept_trade(trade_id: str, accepter_id: str, db: Session = Depends(get_db)):
    try:
        # Атомарно меняем предметы:
        # 1. Списываем offer_items у A, начисляем B
        # 2. Списываем request_items у B, начисляем A
        #
        # for item in trade.offer_items:
        #     decrease_inventory(db, trade.user_id, item["item_id"], item["quantity"])
        #     increase_inventory(db, trade.counterparty_id, item["item_id"], item["quantity"])
        #
        # for item in trade.request_items:
        #     decrease_inventory(db, trade.counterparty_id, item["item_id"], item["quantity"])
        #     increase_inventory(db, trade.user_id, item["item_id"], item["quantity"])

        # trade.status = "accepted"
        # db.commit()
        pass
    except Exception:
        # db.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при обмене")

    return TradeResponse(trade_id=trade_id, status="accepted")
