#         (C) ©️ Copyroght 2022-2023
#           https://t.me/VioMods
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# scope: None
# meta developer: @alonemodules
# meta banner: None

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils


@loader.tds
class WikipediaMod(loader.Module):
    strings = {
        "name": "Wikipedia",
        "search": (
            "🙂 <b> Successfuly searched"
            " question for wikipedia!</b>\n"
        )
        
    }
    strings_ru = {
        "search": (
            "<b>🙂 Успешно найдена"
            " ответ!</b>\n"
        )
        
    }

    async def wikicmd(self, message: Message):
        """<вопрос> - поиск в en.m.wikipedia.org"""
        args = utils.get_args_raw(message)
        en = args.replace(" ", "_")
        enwiki = f"https://en.m.wikipedia.org/wiki/{en}"
        await utils.answer(message, self.strings("search") + f'<a href="{enwiki}">Url</a>')

    async def ruwikicmd(self, message: Message):
        """<вопрос> - поиск в ru.m.wikipedia.org"""
        args = utils.get_args_raw(message)
        ru = args.replace(" ", "_")
        ruwiki = f"https://ru.m.wikipedia.org/wiki/{ru}"
        await utils.answer(message, self.strings("search") + f'<a href="{ruwiki}">Url</a>')

    async def uzwikicmd(self, message: Message):
        """<вопрос> - поиск в uz.m.wikipedia.org"""
        args = utils.get_args_raw(message)
        uz = args.replace(" ", "_")
        uzwiki = f"https://uz.m.wikipedia.org/wiki/{uz}"
        await utils.answer(message, self.strings("search") + f'<a href="{uzwiki}">Url</a>')

    async def simplewikicmd(self, message: Message):
        """<вопрос> - поиск в simple.m.wikipedia.org"""
        args = utils.get_args_raw(message)
        simple = args.replace(" ", "_")
        simplewiki = f"https://simple.m.wikipedia.org/wiki/{simple}"
        await utils.answer(message, self.strings("search") + f'<a href="{simplewiki}">Url</a>')
