# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: PyVerison

# Description: View version for python

# Commands: .pyversion

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

#         (C) ©️ Copyroght 2022-2023
#           https://t.me/AloneModules
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# meta banner: #banner
# meta developer: @alonemodules
# scope: #scope

import contextlib
import sys
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class PyVersionMod(loader.Module):
    """Check The Python Version"""

    strings = {
        "name": "PyVersion",
        "loading": (
            "<code>Loading...</code>"
        ),
        "pythonver": (
            "<emoji document_id=5409076727341130651>🐍</emoji> <b>Python version - {python}</b>"
        ),
    }
    
    @loader.command(ru_doc="Показать информацию o python")
    async def pyversion(self, message: Message):
        """Python Version"""
        message = await utils.answer(message, self.strings("loading"))

        inf = {}
        
        with contextlib.suppress(Exception):
            inf["python"] = (
                f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            )
        await utils.answer(message, self.strings("pythonver").format(**inf))
