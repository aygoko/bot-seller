from sqlalchemy import Column, String, DateTime, Boolean

from infrastructure.database.base import Base


class Promocode(Base):
    __tablename__ = 'promocodes'
    __tableargs__ = {'extend_existing': True}

    promocode_id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

