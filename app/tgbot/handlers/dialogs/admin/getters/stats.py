from aiogram_dialog import DialogManager

from infrastructure.database.repositories.user import UserReader


async def get_promo_stats(dialog_manager: DialogManager, user_reader: UserReader, **kwargs):
    stats = await user_reader.get_promo_codes_stats()
    stats_msg = ''
    for promo in stats:
        stats_msg += f'| {promo[0]} - {promo[1]}\n'
    return {
        'stats_msg': stats_msg
    }


async def get_mail_stats(dialog_manager: DialogManager, **kwargs):
    return {
        'mail_count': dialog_manager.current_context().dialog_data['mail_count']
    }
