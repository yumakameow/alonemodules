# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: Valutes

# Description: Converter Valutes

# Commands: .valute

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

#         (C) ©️ Copyroght 2022-2023
#           https://t.me/VioMods
#
#        Licensed under the GNU AGPLv3
#   https://www.gnu.org/licenses/agpl-3.0.htm

# meta developer: @alonemodules
# meta banner: None

import asyncio
import logging
from requests import get
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class ValutesMod(loader.Module):
	"""Converter Valute"""
	strings = {"name": "Valute"}

	@loader.unrestricted
	async def valutecmd(self, message):
		""".valute <valute; none>"""
		valutes = get("https://www.cbr-xml-daily.ru/daily_json.js").json()
		names = valutes["Valute"].keys()
		args = utils.get_args(message)
		req = []
		
		if args:
			for val in args:
				val = val.upper()
				if val in names:
					req.append(val)
			valutes["Valute"] = {val: valutes["Valute"][val] for val in req}
			
		text = []
		temp = "<b>{}</b>\n{} <code>{}</code>: {}₽ ({}{}₽)"
		for val in valutes["Valute"].values():
			name = val["Name"]
			code = val["CharCode"]
			nom = int(val["Nominal"])
			now = round(float(val["Value"]), 3)
			pre = round(float(val["Previous"]), 3)
			way = "🔹" if now == pre else "📈" if now < pre else "📈"
			text.append(temp.format(name, nom, code, now, way, pre))
		if not text:
			return await utils.answer(message, "<emoji document_id=5373001317042101552>📈</emoji> <b>Запрос неверен - ответ пуст или валюта указанно неверно!</b>")
		await utils.answer(message, "\n".join(text))
