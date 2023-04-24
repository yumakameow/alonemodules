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
class InlineRulesMod(loader.Module):
    """Inline Rules for your chat. Set in <code>.config</code>"""

    strings = {
        "name": "InlineNote",
        "ruleserror": "<b>😑 No args</b>",
        "clicks": "View",
        "ruless": "<b>☁️ Chat rules.</b>",
        "rulesupd": "<b>🙂 Rules updated!</b>",
 
    }

    strings_ru = {
        "ruleserror": "<b>😑 Нету аргументов.</b>",
        "clicks": "Посмотреть",
        "ruless": "<b>☁️ Правила чата./b>",
        "rulesupd": "<b>🙂 Заметки обновлены!</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "rules", "🤒 Rules not set", lambda: "☁️ Правила чата."
        )

    @loader.unrestricted
    async def irulescmd(self, message: Message) -> None:
        """View inline rules"""
        await self.inline.form(
            text=self.strings("ruless"),
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
        if self.config["rules"] != 0:
            await call.answer(self.config["rules"], show_alert=True)
        else:
            await call.answer(self.strings("ruleserror"), show_alert=True)
