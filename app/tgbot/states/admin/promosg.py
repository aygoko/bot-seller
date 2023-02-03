from aiogram.fsm.state import State, StatesGroup


class PromoSG(StatesGroup):
    stats = State()
    enter_name = State()
    created = State()

