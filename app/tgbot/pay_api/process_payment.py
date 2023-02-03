import logging

from aiogram_dialog import DialogRegistry
from aiohttp.abc import Request

from infrastructure.database.repositories.user import UserRepo

logger = logging.getLogger(__name__)


async def api_process_payment(data, dialog_registry: DialogRegistry, db_pool):
    event_id: int = data['operation_id']
    logger.info(f'Received payment {event_id}')
    payment_amount = float(data['withdraw_amount'])
    payment_date = data['datetime']
    label: str = data['label']
    unaccepted: bool = data['unaccepted']

    if unaccepted == 'true':
        logger.error(f'Payment {event_id} is not accepted')
        return

    async with db_pool.begin() as session:
        repo: UserRepo = UserRepo(session)
        await repo.change_payment_status(event_id, status=True, payment_id=event_id)


async def api_handler(request: Request):
    logger.info('Received payment')
    data = await request.post()
    db_pool = request.app['db_pool']
    dialog_registry = request.app['registry']
    await api_process_payment(data, dialog_registry, db_pool)
