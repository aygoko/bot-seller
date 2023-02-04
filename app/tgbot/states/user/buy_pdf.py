from aiogram.fsm.state import StatesGroup, State


class BuyPDF(StatesGroup):
    enter_promo_code = State()
    pay_url = State()

