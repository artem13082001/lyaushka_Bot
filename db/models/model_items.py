from db.base import Base
from sqlalchemy import String, UUID, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class Item(Base):
    __tablename__ = "item"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True, default = uuid.uuid4)
    name: Mapped[str] = mapped_column(String, default="")
    rarity: Mapped[str] = mapped_column(String, default="")
    is_limited: Mapped[str] = mapped_column(String, default="")
    price: Mapped[int] = mapped_column(Integer, default="")
    from_case: Mapped[str] = mapped_column(String, default="")
    type: Mapped[str] = mapped_column(String, default="")