from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters
from support.buttons import language_button

@Client.on_message(filters.private & filters.command(['start', 'lang']))
async def start_bot(c, m: Message):
    await m.reply(Presets.WELCOME.format(m.from_user.first_name),
                  reply_markup=language_button,
                  disable_web_page_preview=True
                  )

@Client.on_message(filters.private & filters.command('help'))
async def help_bot(c, m: Message):
    me = await c.get_me()
    await m.reply(Presets.HELP.format(me.username),
                  quote=True,
                  disable_web_page_preview=True
                  )
