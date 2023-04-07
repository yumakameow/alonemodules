# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: Helper

# Description: Helper

# Commands: .gamee | .vid | .pic | .ftg2bot

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

class AloneHelperMod(loader.Module):
    """Helps in search for telegram"""

    strings = {
        "name": "AloneHelper",
        "results": "<emoji document_id=5470177992950946662>👇</emoji>"
    }
    string_ru = {
        "results": "<emoji document_id=5470177992950946662>👇</emoji>"
    }

    async def gameecmd(self, event):
        "<name for game>; Search game"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query('gamee', args)
        await result[0].click(event.to_id)
        await event.edit(self.strings('results'))

    async def vidcmd(self, event):
        "<name for video>; Search Videos"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query('vid', args)
        await result[0].click(event.to_id)
        await event.edit(self.strings('results'))

    async def piccmd(self, event):
        "<name for pic>; Search Pic"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query('pic', args)
        await result[0].click(event.to_id)
        await event.edit(self.strings('results'))

    async def ftg2botcmd(self, event):
        "<modulesname>; Search FTG modules with @ftg2bot"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query('ftg2bot', args)
        await result[0].click(event.to_id)
        await event.edit(self.strings('results'))
