from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean


class Invoice(BaseModel):
    __tablename__ = "invoices"
    __tableargs__ = {"extend_existing": True}

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    paid = Column(Boolean, nullable=False, default=False)
    payment_id = Column(Integer, nullable=True)
