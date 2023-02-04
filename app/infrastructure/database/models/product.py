from sqlalchemy import Integer, Column, String

from infrastructure.database.base import Base


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    product_price = Column(Integer, nullable=False)
