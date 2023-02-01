from aiogram.fsm.state import State, StatesGroup


class Changes(StatesGroup):
    changes = State()
    choose_text = State()

