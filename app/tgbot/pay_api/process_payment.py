import logging

from aiogram import Bot
from aiogram_dialog import DialogRegistry
from aiohttp import web
from aiohttp.abc import Request

from domain.dto.invoice import InvoiceDTO
from domain.dto.products import ProductDTO
from infrastructure.database.repositories.user import UserRepo, UserReader
from tgbot.handlers.dialogs.common import update_menu

logger = logging.getLogger(__name__)


async def api_process_payment(data, dialog_registry: DialogRegistry, db_pool, bot: Bot):
    event_id: str = data['operation_id']
    if data.get('test_notification', None) == 'true':
        logger.info(f'Payment {event_id} is test')
        return
    logger.info(f'Received payment {event_id}')
    label: str = data.get('label', None)
    unaccepted: bool = data.get('unaccepted', None)
    withdraw_amount: int = data.get('withdraw_amount', None)
    if unaccepted == 'true':
        logger.error(f'Payment {event_id} is not accepted')
        return {
            'status': 400,
        }
    async with db_pool.begin() as session:
        user_reader: UserReader = UserReader(session)
        invoice_obj: InvoiceDTO = await user_reader.get_invoice(label)
    if withdraw_amount != invoice_obj.amount:
        logger.error(f'Payment {event_id} amount is not equal to invoice amount')
        return bot.send_message(chat_id=invoice_obj.user_id,
                                text=f'Ошибка оплаты. Свяжитесь с администратором. \n'
                                     f'ID оплаты: <code>{event_id}</code>')
    async with db_pool.begin() as session:
        repo: UserRepo = UserRepo(session)
        await repo.change_payment_status(event_id, status=True, payment_id=event_id)
    if invoice_obj is None:
        logger.error(f'Invoice {label} not found')
        return {
            'status': 404,
        }
    user_id = invoice_obj.user_id
    product_id = invoice_obj.product_id

    async with db_pool.begin() as session:
        user_reader: UserReader = UserReader(session)
        product_obj: ProductDTO = await user_reader.get_product(product_id)
    product_type = product_obj.product_type
    if product_type == 'link':
        await bot.send_message(chat_id=user_id, text=f'<b>Вечная подписка</b>\n{product_obj.product_content}')
    elif product_type == 'doc':
        await bot.send_document(chat_id=user_id, document=product_obj.product_content)
    await update_menu(user_id, dialog_registry, bot)
    return {
        'status': 200
    }


async def api_handler(request: Request):
    logger.info('Received payment')
    data = await request.post()
    logger.info(data)
    db_pool = request.app['db_pool']
    dialog_registry = request.app['registry']
    bot = request.app['bot']
    await api_process_payment(data, dialog_registry, db_pool, bot)
    return web.json_response(status=200)
