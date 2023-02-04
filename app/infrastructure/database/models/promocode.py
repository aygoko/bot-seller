from sqlalchemy import Column, String, DateTime, Boolean, Integer

from infrastructure.database.base import Base


class Promocode(Base):
    __tablename__ = 'promocodes'
    __tableargs__ = {'extend_existing': True}

    promocode_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    value = Column(Integer, nullable=False, default=200)
    created_at = Column(DateTime, nullable=False)

