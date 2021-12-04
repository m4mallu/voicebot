class Presets(object):
    WELCOME = "<b>Hello.. {}</b>\n\n<i>I'm a simple voice bot. Send me any voice or text to see the magic." \
              " For more about me, try</i> /help .\n\n<b>Credits:</b><a href='https://github.com/m4mallu'>" \
              "<b> M4mallu</b></a>"
    HELP = "<b><u>Summary:</u></b>\n<i>This bot can translate your voice to text in various languages. It also " \
           "supports text to speech in various languages too. This bot can also be able to translate long voice " \
           "clips to text.\n\n<b><u>Usage:</u></b>\n🔰 To translate your voice to text, simply select the language " \
           "from the <a href='t.me/{}?start=start'>list</a> and say something. Or forward any voice clips directly " \
           "to the bot. If you have not opted any of the languages, the bot will assign English-US as the default " \
           "language for translation.\n\n🔰 Send a text message to the bot. Select the required language to translate " \
           "it. You'll receive the voice clip for the corresponding text.</i>\n\n<b>®️Credits:</b><a " \
           "href='https://github.com/m4mallu'><b> M4mallu</b></a> "
    PROCESSING = "<i>Processing..</i>"
    CHANGE_LANG_TXT = "<i>Please select the required language.</i>"
    DOWNLOADING = "<i>Downloading your voice..</i>"
    CONVERTING = "<i>Converting your voice..</i>"
    CHUNK_ERROR = "<b>Some unknown errors happened while converting your voice. Anyways, I'll send you the completed " \
                  "texts. Inconvenience is regretted.</b> 🥵"
    ERROR_CONVERTING = "<i>Error converting your voice..</i>"
    ERROR_FILE = "<b>Error!</b>\n\n<i>This audio cannot be able to convert</i>"
    LONG_FILE = "🧐 <b><u>Hmm.. Lengthy audio</u></b>\n\n<i>Let's try to convert it..</i>"
    CHUNK_TXT = "<i>Generating the texts from Audio: {}</i>"
    FINISHED = "<i>Finished Extracting !</i>"
    READ_TEXT = "<i>Recognizing the text... </i>"
    DECODED_TEXT = "<b><u>Decoded text:</u></b>\n<i>--Tap the text to copy--</i>\n\n<code>{}</code>\n\n" \
                   "<b>Credits:</b><a href='https://github.com/m4mallu'><b> M4Mallu</b></a>"
    DECODED_LONG_TEXT = "<b><u>Decoded text:</u></b>\n\n<code>{}</code>\n\n" \
                        "<b>Credits:</b><a href='https://github.com/m4mallu'><b> M4Mallu</b></a>"
    ERROR_DECODE = "<b>Error!</b>\n\n<i>This audio cannot be able to decode</i>"
    LANGUAGE_SELECT_MSG = "Selected Language: {}"
    TEXT_TO_VOICE = "<b>Select the accent to convert:</b>"
    CONV_TO_VOICE = "<i>Converting your text to voice..</i>"
    GEN_VOICE = "<i>Generating the voice..</i>"
    VOICE_UPLOADED = "<i>Uploading the voice..Plz wait</i>"
    VOICE_CAPTION = "<b>Credits:</b><a href='https://github.com/m4mallu'><b> M4Mallu</b></a>"
    A2T_REPORT = "<b><u>Intimation:</u></b>\n\n<i>Audio to Text conversion</i>\nby: {}"
    T2A_REPORT = "<b><u>Intimation:</u></b>\n\n<i>Text to Audio conversion</i>\nby: {}"
