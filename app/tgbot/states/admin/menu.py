from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()
    enter_message = State()
    send_message_to_all = State()