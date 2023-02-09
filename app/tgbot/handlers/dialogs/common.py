from aiogram import Bot
from aiogram.types import CallbackQuery, User, Chat
from aiogram_dialog import DialogManager, ShowMode, DialogRegistry, DEFAULT_STACK_ID, StartMode
from aiogram_dialog.manager.bg_manager import BgManager

from tgbot.states.user.menu import UserMenu


async def enable_send_mode(
        event: CallbackQuery, button, dialog_manager: DialogManager, **kwargs
):
    dialog_manager.show_mode = ShowMode.SEND


async def get_result(dialog_manager: DialogManager, **kwargs):
    return {
        "result": dialog_manager.current_context().dialog_data["result"],
    }


def when_not(key: str):
    def f(data, whenable, manager):
        return not data.get(key)

    return f


async def update_menu(user_id: int, registry: DialogRegistry, bot: Bot):
    user_params = await bot.get_chat(user_id)
    bgm = BgManager(
        user=User(id=user_id, first_name=user_params.first_name, is_bot=False),
        chat=Chat(id=user_id, type=user_params.type),
        bot=bot,
        registry=registry,
        intent_id=None,
        stack_id=DEFAULT_STACK_ID)
    await bgm.start(UserMenu.main_menu, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND)
