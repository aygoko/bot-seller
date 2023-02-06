from aiogram.fsm.state import StatesGroup, State


class BuyProduct(StatesGroup):
    choose_product = State()
    enter_promo_code = State()
    pay_url = State()
