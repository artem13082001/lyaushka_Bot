
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from db.models.model_user import User
from db.models.model_case import Case
from db.session import get_db

router_shop = APIRouter(prefix="/shop", tags=["shop"])


