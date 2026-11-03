from db.base import Base
from sqlalchemy import String, UUID, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class Case(Base):
    __tablename__ = "case"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, default="")
    is_limited: Mapped[str] = mapped_column(String, default="")
    price: Mapped[str] = mapped_column(String, default="")
    type: Mapped[str] = mapped_column(String, default="")