# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Module Name: Text To Voice

# Description: 

# Commands: .ttv

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

import io
import os

import requests
from gtts import gTTS
from pydub import AudioSegment

from .. import loader, utils


def register(cb):
    cb(TextToVoiceMod())


class TextToVoiceMod(loader.Module):
    """Text to speech module"""

    strings = {
        "name": "TTV",
        "no_text": "Error! No args",
        "tts_lang_cfg": "Set your language code for the TTV here.",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "TTS_LANG", "en", lambda m: self.strings("tts_lang_cfg", m)
        )
        self.is_ffmpeg = os.system("ffmpeg -version") == 0

    async def say(self, message, speaker, text, file=".dtts.mp3"):
        reply = await message.get_reply_message()
        if not text:
            if not reply:
                return await utils.answer(message, self.strings["no_text"])
            text = reply.raw_text
        if not text:
            return await utils.answer(message, self.strings["no_text"])
        if message.out:
            await message.delete()
        data = {"text": text}
        if speaker:
            data["speaker"] = speaker

        f = io.BytesIO(
            requests.get("https://station.aimylogic.com/generate", data=data).content
        )
        f.name = file

        if self.is_ffmpeg:
            f, duration = to_voice(f)
        else:
            duration = None

        await message.client.send_file(
            message.chat_id, f, voice_note=True, reply_to=reply, duration=duration
        )

    @loader.unrestricted
    @loader.ratelimit
    async def ttvcmd(self, message):
        """<tex>; use"""
        reply = await message.get_reply_message()
        text = utils.get_args_raw(message.message)

        if not text:
            if message.is_reply:
                text = (await message.get_reply_message()).message
            else:
                return await utils.answer(message, self.strings("no_text", message))

        if message.out:
            await message.delete()

        tts = await utils.run_sync(gTTS, text, lang=self.config["TTS_LANG"])
        voice = io.BytesIO()
        await utils.run_sync(tts.write_to_fp, voice)
        voice.seek(0)
        voice.name = "ttv.mp3"

        if self.is_ffmpeg:
            voice, duration = to_voice(voice)
        else:
            duration = None

        await message.client.send_file(
            message.chat_id, voice, voice_note=True, reply_to=reply, duration=duration
        )


def to_voice(item):
    """Returns audio in opus format and it's duration"""
    item.seek(0)
    item = AudioSegment.from_file(item)
    m = io.BytesIO()
    m.name = "voice.ogg"
    item.split_to_mono()
    dur = len(item) / 1000
    item.export(m, format="ogg", bitrate="64k", codec="libopus")
    m.seek(0)
    return m, dur
