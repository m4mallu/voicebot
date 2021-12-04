import os
import shutil
from presets import Presets
from pydub import AudioSegment
import speech_recognition as sr
from asyncio import sleep as slp
from pydub.utils import mediainfo
from pyrogram.types import Message
from pydub.utils import make_chunks
from plugins.cb import language_key
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from support.service import a2tService
from support.buttons import change_language, close_button


@Client.on_message(filters.private & (filters.voice | filters.audio | filters.document))
async def aud2txt(c, m: Message):
    id = m.from_user.id
    if id not in language_key:
        language_key[id] = 'en-US'
    msg = await m.reply(Presets.PROCESSING, quote=True)
    download_path = os.path.join(os.getcwd(), str(m.from_user.id))
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    else:
        for files in os.listdir(download_path):
            try:
                os.remove(os.path.join(download_path, files))
            except Exception:
                pass
    await msg.edit(Presets.DOWNLOADING)
    await m.download(download_path)
    await msg.edit(Presets.CONVERTING)
    #
    if m.document and (str(m.document.file_name).endswith('.wav')):
        for files in os.listdir(download_path):
            try:
                os.rename(os.path.join(download_path, files), os.path.join(download_path, "audio.wav"))
            except Exception:
                await msg.edit(Presets.ERROR_FILE)
                return
    elif m.document and (str(m.document.file_name).endswith('.mp3')):
        for files in os.listdir(download_path):
            try:
                sound = AudioSegment.from_mp3(os.path.join(download_path, files))
                sound.export(os.path.join(download_path, files.replace(".mp3", ".wav")), format="wav")
                os.rename(os.path.join(download_path, files), os.path.join(download_path, "audio.wav"))
            except Exception:
                await msg.edit(Presets.ERROR_FILE)
                return
    elif not m.document:
        for files in os.listdir(download_path):
            try:
                sound = AudioSegment.from_file(os.path.join(download_path, files))
                sound.export(os.path.join(download_path, files.replace(".ogg", ".wav")), format="wav")
                os.rename(os.path.join(download_path, files), os.path.join(download_path, "audio.wav"))
            except Exception:
                await msg.edit(Presets.ERROR_FILE)
                return
    #
    audio_file = os.path.join(download_path, "audio.wav")
    duration = round(float(mediainfo(audio_file)["duration"]))
    #
    recognizer = sr.Recognizer()
    #
    if int(duration) > 14:
        await msg.edit(Presets.LONG_FILE)
        #
        text = chunk_name = str()
        chunk_length = 15 * 1000
        my_audio = AudioSegment.from_file(audio_file, "wav")
        chunks = make_chunks(my_audio, chunk_length)
        for i, chunk in enumerate(chunks):
            chunk_name = "{0}.wav".format(i)
            chunk.export(chunk_name, format="wav")
            with sr.AudioFile(chunk_name) as source:
                audio = recognizer.listen(source)
                try:
                    text = text + recognizer.recognize_google(audio, language=language_key[id])
                    await msg.edit(Presets.CHUNK_TXT.format(i + 1, len(chunks)))
                    os.remove(chunk_name)
                except Exception:
                    pass
        if len(text) == 0:
            await msg.edit(Presets.ERROR_CONVERTING, reply_markup=close_button)
            try:
                os.remove(chunk_name)
            except Exception:
                pass
            return
        else:
            try:
                os.remove(chunk_name)
            except Exception:
                pass
            await msg.edit(Presets.FINISHED)
            await slp(1)
            #
            max_txt_len = 4025
            if len(text) < max_txt_len:
                try:
                    await msg.edit(Presets.DECODED_TEXT.format(text),
                                   reply_markup=change_language,
                                   disable_web_page_preview=True
                                   )
                except Exception:
                    pass
            else:
                await msg.edit(Presets.CHUNK_ERROR, reply_markup=close_button)
                text_parts = [text[i:i + max_txt_len] for i in range(0, len(text), max_txt_len)]
                for part in text_parts:
                    try:
                        await m.reply(Presets.DECODED_TEXT.format(part),
                                      reply_markup=change_language,
                                      disable_web_page_preview=True
                                      )
                    except FloodWait as e:
                        await slp(e.x)
                    await slp(0.5)
                await a2tService(c, m)
    else:
        with sr.AudioFile(audio_file) as source:
            recorded_audio = recognizer.listen(source)
        await msg.edit(Presets.READ_TEXT)
        try:
            text = recognizer.recognize_google(recorded_audio, language=language_key[id])
        except Exception:
            await msg.edit(Presets.ERROR_DECODE)
            return
        await msg.edit(Presets.DECODED_TEXT.format(text),
                       reply_markup=change_language,
                       disable_web_page_preview=True
                       )
        await a2tService(c, m)
    #
    try:
        shutil.rmtree(download_path)
    except Exception:
        pass
