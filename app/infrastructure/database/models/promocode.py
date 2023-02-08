from sqlalchemy import Column, String, DateTime, Integer, ForeignKey

from infrastructure.database.base import Base


class Promocode(Base):
    __tablename__ = 'promocodes'
    __tableargs__ = {'extend_existing': True}

    promocode_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    value = Column(Integer, nullable=False, default=200)
    created_at = Column(DateTime, nullable=False)


class UserPromoCode(Base):
    __tablename__ = 'user_promo_codes'
    __tableargs__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False)
    promo_code = Column(String(255))
    used_at = Column(DateTime)
