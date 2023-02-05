from aiogram.fsm.state import StatesGroup, State


class BuyProduct(StatesGroup):
    enter_promo_code = State()
    pay_url = State()
    choose_product = State()
