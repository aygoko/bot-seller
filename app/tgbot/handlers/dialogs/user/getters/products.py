from aiogram_dialog import DialogManager

from infrastructure.database.repositories.user import UserReader


async def get_products(d: DialogManager, user_reader: UserReader, **kwargs):
    products = await user_reader.get_products()
    return {
        'products': products
    }
