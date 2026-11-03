from email.policy import default

from db.base import Base
from sqlalchemy import String, UUID, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="user"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True, default = uuid.uuid4)
    name:Mapped[str]=mapped_column(String(20))
    inventory_items: Mapped[str]=mapped_column(String, default="")
    inventory_case: Mapped[str]=mapped_column(String, default="")
    balance: Mapped[int]=mapped_column(Integer, default=0)
