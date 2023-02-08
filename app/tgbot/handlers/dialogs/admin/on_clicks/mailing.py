import asyncio
import logging

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.manager.protocols import ManagedDialogAdapterProto

from domain import UserDTO
from infrastructure.database.repositories.user import UserReader
from tgbot.states.admin.menu import AdminMenu

logger = logging.getLogger(__name__)


async def start_mailing(m: Message, dialog: ManagedDialogAdapterProto, manager: DialogManager,
                        **kwargs):
    manager.show_mode = ShowMode.SEND
    repo: UserReader = manager.data.get('user_reader')
    users: list[UserDTO] = await repo.get_all_users()
    count = 0
    for user in users:
        await asyncio.sleep(0.04)
        try:
            await m.send_copy(user.user_id)
            count += 1
        except TelegramBadRequest as e:
            logger.error('Error while sending message to user {}: {}'.format(user.user_id, e))
    manager.current_context().dialog_data['mail_count'] = count
    logger.info(f'User {m.from_user.id} sent message to all users')
    await manager.switch_to(AdminMenu.mail_result)
