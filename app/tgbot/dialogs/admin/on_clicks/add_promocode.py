import logging
import uuid
from datetime import datetime
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from infrastructure.database.models.promocode import Promocode

logger = logging.getLogger(__name__)


async def add_promocode_to_db(c: CallbackQuery, button: Any, manager: DialogManager, **kwargs):
    # add item to db
    promocode_name: str = manager.current_context().dialog_data["promocode_name"]

    user_id: int = manager.event.from_user.id

    prmocode = Promocode(
        promocode_id=str(uuid.uuid4())[:8],
        created_at=datetime.now()
    )

    logger.info(f"Promocode {promocode_name} added to db by user {user_id}")
    manager.current_context().dialog_data['promocode_id'] = prmocode.promocode_id

    await manager.done()
