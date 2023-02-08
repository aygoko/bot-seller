from datetime import datetime

from pydantic import parse_obj_as
from sqlalchemy import select, insert
from sqlalchemy import update

from domain.dto.products import ProductDTO
from domain.dto.user import UserDTO
from infrastructure.database.models.invoice import Invoice
from infrastructure.database.models.product import Product
from infrastructure.database.models.promocode import Promocode, UserPromoCode
from infrastructure.database.models.user import User
from infrastructure.database.repositories.repo import SQLAlchemyRepo


class UserRepo(SQLAlchemyRepo):
    async def update_user_if_not_exists(self, user_id: int, full_name: str, registered_at: datetime):
        sql = select(User.user_id).where(User.user_id == user_id)
        result = (await self.session.execute(sql)).first()
        if not result:
            await self.session.execute(
                insert(User).values(user_id=user_id, full_name=full_name, registered_at=registered_at))
            await self.session.commit()

    async def update_balance(self, user_id: int, amount: float):
        await self.session.execute(
            update(User).values(balance=User.balance + amount).where(
                User.user_id == user_id))
        await self.session.commit()

    async def add_invoice(self, user_id: int, amount: float, invoice_hash: str):
        await self.session.execute(
            insert(Invoice).values(user_id=user_id, amount=amount, created_at=datetime.now(),
                                   invoice_hash=invoice_hash))
        await self.session.commit()

    async def change_payment_status(self, event_id: int, status: bool, payment_id: int = None):
        await self.session.execute(
            update(Invoice).values(paid=status, payment_id=payment_id).where(
                Invoice.invoice_id == event_id))
        await self.session.commit()


class UserReader(SQLAlchemyRepo):
    async def get_blocked_users(self):
        query = await self.session.execute(
            select(User).where(User.is_blocked == True)
        )
        result = query.scalars().all()
        return parse_obj_as(list[UserDTO], result)

    async def get_admins(self):
        query = select(User).where(User.is_admin == True)
        result = (await self.session.execute(query))
        admins = result.scalars().all()
        return parse_obj_as(list[UserDTO], admins)

    async def get_user_balance(self, user_id: int):
        query = select(User).where(User.user_id == user_id)
        result = (await self.session.execute(query))
        user = result.scalars().all()
        return parse_obj_as(list[UserDTO], user)

    async def get_all_users(self):
        query = await self.session.execute(select(User))
        return parse_obj_as(list[UserDTO], query.scalars().all())

    async def check_promo_status(self, tg_id: int, promo: str):
        query = select(Promocode).where(Promocode.name == promo)
        result: [Promocode] = (await self.session.execute(query)).first()
        if result:
            # Check if user already used this promo code
            query_check = await self.session.execute(
                select(UserPromoCode).where(UserPromoCode.user_id == tg_id))
            if query_check.first():
                return None
            # Add promo code to user history
            await self.session.execute(
                insert(UserPromoCode).values(user_id=tg_id, promo_code=promo, used_at=datetime.now()))
            return result[0].value
        else:
            return None

    async def get_item_price(self, item_id: int):
        query = await self.session.execute(
            select(Product).where(Product.item_id == item_id))
        result = query.first()
        return result[0].item_price

    async def get_products(self) -> list[ProductDTO]:
        query = await self.session.execute(select(Product))
        return parse_obj_as(list[ProductDTO], query.scalars().all())
