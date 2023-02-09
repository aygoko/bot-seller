import asyncio
import logging

from aiogram import Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from infrastructure.database.repositories.admin import AdminRepo
from infrastructure.database.repositories.bot import BotRepo
from infrastructure.database.repositories.user import UserReader
from tgbot.states.admin.menu import AdminMenu

logger = logging.getLogger(__name__)


async def sending_messages_to_all_users(event: Message, user_reader: UserReader, bot: Bot):
    users = await user_reader.get_all_users()
    for user in users:
        await asyncio.sleep(0.04)
        try:
            await bot.send_message(user.user_id, event.text)
        except TelegramBadRequest as e:
            logger.error('Error while sending message to user {}: {}'.format(user.user_id, e))

    logger.info(f'User {event.from_user.id} sent message to all users')


async def admin_start(event: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AdminMenu.admin_menu, mode=StartMode.RESET_STACK)


async def start_maintenance(event: Message, bot_repo: BotRepo):
    await bot_repo.set_maintenance()
    await event.reply('♻️ Режим обслуживания включен')
    logger.info(f'User {event.from_user.id} turned on maintenance mode')


async def stop_maintenance(event: Message, bot_repo: BotRepo):
    await bot_repo.disable_maintenance()
    await event.reply('✅ Режим обслуживания выключен')
    logger.info(f'User {event.from_user.id} turned off maintenance mode')


async def add_admin(event: Message, command: CommandObject, admin_repo: AdminRepo):
    new_admin = command.args
    try:
        admin_id = int(new_admin)
    except TypeError:
        await event.reply('✏️ Пожалуйста, укажите Telegram ID администратора')
        return
    except ValueError:
        await event.reply('❌ Telegram ID администратора должен быть числом!')
        return
    result = await admin_repo.add_admin(admin_id)
    if result:
        logger.info(f'User {event.from_user.id} added admin {admin_id}')
        await event.reply(f'✅ Пользователь {admin_id} добавлен в список админов')
    else:
        await event.reply(f'❗ Пользователь {admin_id} не найден')
        logger.info(f'User {event.from_user.id} tried to add admin {admin_id}, but he is not found')


async def ban_user(event: Message, command: CommandObject, admin_repo: AdminRepo):
    user_id = command.args
    try:
        user_id = int(user_id)
    except TypeError:
        await event.reply('Пожалуйста, укажите Telegram ID пользователя')
        return
    except ValueError:
        await event.reply('Telegram ID пользователя должен быть числом!')
        return
    result = await admin_repo.ban_user(user_id)
    if result:
        logger.info(f'User {event.from_user.id} banned {user_id}')
        await event.reply(f'🚫 Пользователь {user_id} заблокирован')
    else:
        await event.reply(f'❗ Пользователь {user_id} не найден')
        logger.info(f'User {event.from_user.id} tried to ban {user_id}, but he is not found')


async def get_file_id(event: Message):
    await event.reply(event.document.file_id)


def register_admin_router(router: Router):
    router.message.register(start_maintenance,
                            Command(commands=['maintenance'], commands_prefix='/!'), state='*')
    router.message.register(stop_maintenance,
                            Command(commands=['stop_maintenance'], commands_prefix='/!'), state='*')
    router.message.register(add_admin,
                            Command(commands=['add_admin'], commands_prefix='/!'), state='*')
    router.message.register(ban_user,
                            Command(commands=['ban'], commands_prefix='/!'), state='*')
    router.message.register(admin_start,
                            Command(commands=['admin'], commands_prefix='/!'), state='*')
    router.message.register(get_file_id,
                            content_types=['document'], state='*')
