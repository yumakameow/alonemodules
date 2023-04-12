#         (C) ©️ Copyroght 2022-2023
#           https://t.me/AloneModules
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# meta banner: #banner
# meta developer: @alonemodules
# scope: #scope

import asyncio
import io
import logging
import time

from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class InlineNoteMod(loader.Module):
    """🙃 Inline Note for your notes. Set notes for .config"""

    strings = {
        "name": "InlineNote",
        "noteserr": "<b>😑 No args</b>",
        "clicks": "❤️ View ❤️",
        "notess": "<b>😼 Information for your notes.</b>",
        "noteupd": "<b>🙂 Notes updated!</b>",
 
    }

    strings_ru = {
        "noteserr": "<b>😑 Вы не ввели заметку</b>",
        "clicks": "❤️ Посмотреть ❤️",
        "notess": "<b>😼 Информация о ваших <u>заметках</u></b>",
        "noteupd": "<b>🙂 Заметки обновлены!</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "notes", "🤒 Notes not set", lambda: "😼 Information for your notes."
        )

    @loader.unrestricted
    async def inotescmd(self, message: Message) -> None:
        """View your inline notes. Set notes for .config"""
        await self.inline.form(
            text=self.strings("notess"),
            message=message,
            disable_security=True,
            reply_markup=[
                [
                    {
                        "text": self.strings("clicks"),
                        "callback": self.inline__callAnswer,
                    }
                ]
            ],
        )

    async def inline__callAnswer(self, call) -> None:
        if self.config["notes"] != 0:
            await call.answer(self.config["notes"], show_alert=True)
        else:
            await call.answer(self.strings("noteserr"), show_alert=True)
