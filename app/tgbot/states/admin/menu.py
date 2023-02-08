from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()
    enter_message = State()
    mail_result = State()
