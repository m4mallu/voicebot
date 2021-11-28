from presets import Presets
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from support.buttons import language_button

language_key = {}


@Client.on_callback_query(filters.regex(r'^close$'))
async def close_button(c, cb: CallbackQuery):
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^change_lang$'))
async def change_language_button(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.reply_text(Presets.CHANGE_LANG_TXT, reply_markup=language_button)


@Client.on_callback_query(filters.regex(r'^en$'))
async def english_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'en-US'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇺🇸 English"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^ru$'))
async def russian_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'ru-RU'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇷🇺 Русский"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^es$'))
async def spanish_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'es-ES'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇪🇸 Español"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^zh$'))
async def chinese_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'zh'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇨🇳  中文"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^fr$'))
async def french_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'fr-FR'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇫🇷  Français"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^it$'))
async def italian_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'it-IT'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇹  Italiano"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^de$'))
async def german_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'de-DE'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇩🇪  Deutsch"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^pt$'))
async def portuguese_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'pt-PT'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇫🇷  Português"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^el$'))
async def greek_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'el-GR'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇹  Ελληνικά"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^ml$'))
async def malayalam_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'ml-IN'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇳  മലയാളം"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^te$'))
async def telugu_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'te-IN'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇳  తెలుగు"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^kn$'))
async def kannada_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'kn-IN'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇳  ಕನ್ನಡ"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^hi$'))
async def hindi_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'hi-IN'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇳  हिंदी"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^ta$'))
async def tamil_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'ta-IN'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇮🇳  தமிழ்"), True)
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^ar$'))
async def arabic_button(c, cb: CallbackQuery):
    id = cb.from_user.id
    language_key[id] = 'ar-AE'
    await cb.answer(Presets.LANGUAGE_SELECT_MSG.format("🇸🇦  ارابيچ"), True)
    await cb.message.delete()
