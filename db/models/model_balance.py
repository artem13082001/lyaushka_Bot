from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

from db.base import Base
from sqlalchemy import String, UUID, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=0.0)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)