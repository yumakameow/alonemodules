__version__ = (1, 0, 0)

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: Searcher

# Description: Search in Yandex and Google

# Commands: .google | yandex

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

#         (C) ©️ Copyroght 2022-2023
#           https://t.me/VioMods
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# scope: None

# requires: pydub requests gtts hachoir
# meta developer: @alonemodules
# meta banner: None

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils


@loader.tds
class SearcherMod(loader.Module):
    strings = {
        "name": "Searcher",
        "search": (
            "<emoji document_id=5431815452437257407>🐳</emoji><b> Successfuly searched"
            " url</b>\n"
        )
        
    }
    strings_ru = {
        "search": (
            "<emoji document_id=5431815452437257407>🐳</emoji><b> Успешно найдена"
            " ссылка</b>\n"
        )
        
    }

    async def googlecmd(self, message: Message):
        """<текст> - поиск в google.com"""
        args = utils.get_args_raw(message)
        g = args.replace(" ", "%20")
        google = f"https://google.com/search?q={g}"
        await utils.answer(message, self.strings("search") + f'<a href="{google}">Ссылка</a>')

    async def yandexcmd(self, message: Message):
        """<текст> - поиск в yandex.com"""
        args = utils.get_args_raw(message)
        y = args.replace(" ", "%20")
        yandex = f"https://yandex.com/search/?text={y}"
        await utils.answer(message, self.strings("search") + f'<a href="{yandex}">Ссылка</a>')
