# Фейк модуль не для канала



import logging
import random
import time
from asyncio import sleep
from random import choice, randint

from telethon.tl.functions.channels import JoinChannelRequest

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(Yumahost())


class Yumahost(loader.Module):
    """Управлением с @yumahost"""

    strings = {"name": "Yumahost"}

    async def yumahostcmd(self, message):
        """Используй .yumahost <дни>."""
        text = utils.get_args_raw(message)
        if not text:
            for pinj in ["🙃 <code>Выдаю подписку...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)

            named_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", named_tuple)

            await message.edit(
                "<emoji document_id=5431449001532594346>⚡️</emoji> <b>Скорость отклика"
                " Telegram:</b>"
                f" <code>{random.randint(10, 1999)}.{random.randint(10, 99)}</code>"
                " <b>ms</b>\n<emoji document_id=5445284980978621387>🚀</emoji>"
                f" <b>Прошло с последней перезагрузки: {time_string}</b>"
            )
            return
        else:
            for pinj in ["🙂 <code>Выдаю подписку...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)

            named_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", named_tuple)

            pinj = (
                f"🥰 <b>Участнику успешно выданно <code>YumaHost</code>, На <code>{text}</code>дней.</b>"
            )

            await message.edit(pinj)
