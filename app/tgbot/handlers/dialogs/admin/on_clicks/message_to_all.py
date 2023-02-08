import asyncio
import logging

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.manager.protocols import ManagedDialogAdapterProto

from domain import UserDTO
from infrastructure.database.repositories.user import UserReader

logger = logging.getLogger(__name__)


async def sending_messages_to_all_users(m: Message, dialog: ManagedDialogAdapterProto, manager: DialogManager,
                                        **kwargs):
    manager.show_mode = ShowMode.SEND
    repo: UserReader = manager.data.get('user_reader')
    users: list[UserDTO] = await repo.get_all_users()
    for user in users:
        await asyncio.sleep(0.04)
        try:
            await m.send_copy(user.user_id)
        except TelegramBadRequest as e:
            logger.error('Error while sending message to user {}: {}'.format(user.user_id, e))

    logger.info(f'User {m.from_user.id} sent message to all users')
