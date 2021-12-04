<h1 align="left">
    <a target="_blank">
        Voicebot
        <img src="https://telegra.ph/file/a171e7b883533f40bb083.gif" width="275">
    </a>
</h1>

#### A simple Telegram bot to convert lengthy voice clips to text and vice versa with supporting languages.

<details>
    <summary><b>About</b></summary>
        <p align="left">
            🔰 Voicebot is a simple Telegram bot to convert lengthy voice clips to text and vice versa with supporting
            languages. Send a voice clip to the bot and it will convert it to text even if it is too long. You can also
            send pre-recorded voice to the bot and it will convert it to text.<br><br>
            🔰 Voicebot can also convert text to voice clips. Send text to the bot and it will convert it to the voice
            clip. (Please find the supporting languages in the bot itself)
    <br>
</details>
<details>
  <summary><b>Mandatory Variables</b></summary>
    <p align="left">

    API_HASH    -   Your API Hash from my.telegram.org
    APP_ID      -   Your APP ID from my.telegram.org
    BOT_TOKEN   -   Your bot token from @BotFather
    LOG_CHAT    -   the chat id where you want to send the logs - starting with -100
</>
</details>
<details>
  <summary><b>Bot Commands</b></summary>
    <p align="left">
    
    start - Start the bot
    help - Show this help message
    lang - Change the language
    
</>
</details>
<details>
    <summary><b>Deploy</b></summary>
    <p align="left"></p>
        <b><u>Deploy in VPS:</u></b>
        <ul>
            <li><strong>Open a Linux Terminal and Run the below commands ( Stage: 1 )</strong></li>
            <li><code>git clone https://github.com/m4mallu/voicebot</code></li>
            <li><code>cd voicebot</code></li>
            <li>Create a <code>config.py</code> with the Mandatory variables (Refer sample_config.py) and save it in the bot directory.</li>
            <li><strong>Run the below commands in the same terminal ( Stage: 2 )</strong></li>
            <li><code>virtualenv -p python3 venv</code></li>
            <li><code>. ./venv/bin/activate</code></li>
            <li><code>pip3 install -r requirements.txt</code></li>
            <li><code>python3 bot.py</code></li>
        </ul>
        <b><u>Deploy in Heroku</u></b>
        <ul>
            <li><strong>Click the below button to deploy the bot in Heroku</strong></li>
            <a href="https://heroku.com/deploy?template=https://github.com/m4mallu/voicebot">
            <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
        </a>
        </ul>
</details>
<details>
  <summary><b>Developer</b></summary>
    <p align="left">
        <img alt="GPL3" src ="https://c.tenor.com/10Zdx_RXqgcAAAAC/programming-crazy.gif" width="260px" style="max-width:100%;"/><br>
            <a href="https://t.me/space4renjith"><img src="https://img.shields.io/badge/Renjith-Mangal-orange" height="24">
        </a>&nbsp;
            <a href="https://t.me/rmprojects"><img src="https://img.shields.io/badge/Updates-Channel-orange" height="24">
        </a>
</p>
</details>
<details>
    <summary><b>Donate</b></summary>
    <p align="left"><br>
    <b>Buy me a cup of coffee for the works !</b><br>
    <img src="https://telegra.ph/file/b926b7e8ea84826d81d8a.png" width="260px" style="max-width:100%;"/><br><br>
      <a href="https://www.paypal.me/space4renjith" target="_blank">
        <img src="https://img.shields.io/badge/Donate-Me-blueviolet?style=for-the-badge&logo=paypal">
    </a>
</p>
</details>
<details>
  <summary><b>License</b></summary>
    <p align="left">
    <a href="https://choosealicense.com/licenses/gpl-3.0/">
        <img src="https://img.shields.io/badge/License-GPLv3-blueviolet?style=for-the-badge&logo=gplv3">
    </a>
</p>
</details>
<details>
  <summary><b>Credits</b></summary>
    <p align="left">
      <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://img.shields.io/badge/PYROGRAM-FRAMEWORK-orange" height="32.8">
    </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://pypi.org/project/pydub/">
        <img src="https://img.shields.io/badge/Pydub-Library-orange" height="32.8">
    </a><br>
    <a href="https://pypi.org/project/SpeechRecognition/">
        <img src="https://img.shields.io/badge/Speech-Recognition-orange" height="32.8">
    </a>&nbsp;&nbsp;
    <a href="https://pypi.org/project/gTTS/">
        <img src="https://img.shields.io/badge/Google-Text%20to%20Speech-orange" height="32.8">
    </a>
</p>
</details>