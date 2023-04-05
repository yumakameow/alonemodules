# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: SearchModules

# Description: Search modules via @ftg2bot

# Commands: .smod

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

#         (C) ©️ Copyroght 2022-2023
#           https://t.me/AloneModules
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# meta banner: #banner
# meta developer: @alonemodules
# scope: #scope

from .. import loader, utils
from telethon.tl.types import Message
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events

class SearchModulesMod(loader.Module):
    """Search Modules via @ftg2bot"""

    strings = {
        "name": "SearchModules",
        "results": "<emoji document_id=5470177992950946662>👇</emoji> <b>Results</b>"
    }
    string_ru = {
        "results": "<emoji document_id=5470177992950946662>👇</emoji> <b>Результаты</b>"
    }

    async def smodcmd(self, event):
        "<module name>"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query('ftg2bot', args)
        await result[0].click(event.to_id)
        await event.edit(self.strings('results'))
