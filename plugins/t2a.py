import os
from presets import Presets
from gtts import gTTS as Convert
from asyncio import sleep as slp
from pyrogram import Client, filters
from support.service import t2aService
from support.buttons import lang4voice_button
from pyrogram.types import CallbackQuery, Message


@Client.on_message(filters.private & filters.text)
async def text_in(c, m: Message):
    if not str(m.text).startswith('/'):
        await m.reply(Presets.TEXT_TO_VOICE,
                      quote=True,
                      reply_markup=lang4voice_button
                      )


@Client.on_callback_query(filters.regex(r'^en_voice$'))
async def english_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='en')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.delete()
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass


@Client.on_callback_query(filters.regex(r'^en-IN_voice$'))
async def english_IN_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='en', tld='co.in')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await cb.message.delete()
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass


@Client.on_callback_query(filters.regex(r'^fr_voice$'))
async def french_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='fr')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await cb.message.delete()
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass


@Client.on_callback_query(filters.regex(r'^zh_voice$'))
async def chinese_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='zh')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await cb.message.delete()
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass


@Client.on_callback_query(filters.regex(r'^pt_voice$'))
async def portuguese_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='pt')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await cb.message.delete()
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass

@Client.on_callback_query(filters.regex(r'^es_voice$'))
async def spanish_voice(c, cb: CallbackQuery):
    text = cb.message.reply_to_message.text
    title = str(text)[:8] if len(text) > 8 else text
    await cb.message.edit_text(Presets.CONV_TO_VOICE)
    await slp(1)
    tts = Convert(text=text, lang='es')
    await cb.message.edit_text(Presets.GEN_VOICE)
    await slp(1)
    voice = tts.save(title + '.mp3')
    await cb.message.edit_text(Presets.VOICE_UPLOADED)
    await slp(1)
    await cb.message.reply_voice(voice=title + '.mp3', caption=Presets.VOICE_CAPTION)
    await cb.message.delete()
    await t2aService(c, cb)
    try:
        os.remove(title + '.mp3')
    except Exception:
        pass
