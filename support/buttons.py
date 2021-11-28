from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

close = [
        [
            InlineKeyboardButton("❌ Close", callback_data="close")
        ]
        ]

change = [
         [
                InlineKeyboardButton("❌ Close", callback_data="close"),
                InlineKeyboardButton("🏁 Lang", callback_data="change_lang")
         ]
         ]

language = [
           [
                InlineKeyboardButton("🇮🇳  മലയാളം", callback_data="ml"),
                InlineKeyboardButton("🇮🇳  తెలుగు", callback_data="te"),
                InlineKeyboardButton("🇮🇳  ಕನ್ನಡ", callback_data="kn")
           ],
           [
                InlineKeyboardButton("🇮🇳  हिंदी", callback_data="hi"),
                InlineKeyboardButton("🇮🇳  தமிழ்", callback_data="ta"),
                InlineKeyboardButton("🇸🇦  ارابيچ", callback_data="ar")
           ],
           [
                InlineKeyboardButton("🇺🇸 English", callback_data="en"),
                InlineKeyboardButton("🇷🇺 Русский", callback_data="ru"),
                InlineKeyboardButton("🇪🇸 Español", callback_data="es")
           ],
           [
                InlineKeyboardButton("🇨🇳  中文", callback_data="zh"),
                InlineKeyboardButton("🇫🇷  Français", callback_data="fr"),
                InlineKeyboardButton("🇮🇹  Italiano", callback_data="it")
           ],
           [
                InlineKeyboardButton("🇩🇪  Deutsch", callback_data="de"),
                InlineKeyboardButton("🇫🇷  Português", callback_data="pt"),
                InlineKeyboardButton("🇮🇹  Ελληνικά", callback_data="el")
           ],
           [
                InlineKeyboardButton("❌ Close", callback_data="close")
           ]
           ]

lang4voice = [
             [
                    InlineKeyboardButton("🇺🇸 English", callback_data="en_voice"),
                    InlineKeyboardButton("🇮🇳 English", callback_data="en-IN_voice")
             ],
             [
                    InlineKeyboardButton("🇫🇷  Français", callback_data="fr_voice"),
                    InlineKeyboardButton("🇨🇳  中文", callback_data="zh_voice")
             ],
             [
                    InlineKeyboardButton("🇫🇷  Português", callback_data="pt_voice"),
                    InlineKeyboardButton("🇪🇸 Español", callback_data="es_voice")
             ]
             ]

close_button = InlineKeyboardMarkup(close)
change_language = InlineKeyboardMarkup(change)
language_button = InlineKeyboardMarkup(language)
lang4voice_button = InlineKeyboardMarkup(lang4voice)
