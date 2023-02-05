from aiogram.fsm.state import StatesGroup, State


class BuySubscription(StatesGroup):
    enter_promo_code = State()
    pay_url = State()
