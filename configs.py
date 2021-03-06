# (c) @Friend_A_Kousei

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "17945796"))
    API_HASH = os.environ.get("API_HASH", "4a05481a5da2d66f801acffc4ca5ee4b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5098785902:AAFmvndi6bs_cop5XcT_1_xsHCpzGG6t_iQ")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Minamotosakura")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 0))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1813305809"))
    CAPTION = ""
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001618521535"))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://sakura:sakura@cluster0.futdd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "True"))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT ="""
Hi!! 
I'm Sakura Minamoto😊♥️ A Simple File Rename Bot With Permenant Thumbnail Support💯.

__For More Details Check Help__📜
"""
    HELP_TEXT = """**Follow these Steps For Using Me..**
 
➠ Configure the Settings before using me.....
➠ Send a photo to set it as your custom thumbnail..... 
➠ Send any File or media you want to rename..... 
➠ That's it, and rest is mine work..... 

📝 Available Commands 📝
- /start - Start the Bot
- /help - How to Use
- /about - About Me
- /settings - Configure Settings 
- /showthumb & /delthumb - For Thumbnail

__⭕️Note: Multitasking supported, but only do two tasks at once, or the bot may crash..__
"""
    ABOUT_TEXT = """
📌 A Telegram Bot Can Help You For Renaming File/Video/Audio With Permenant Thumbnail Support💯 Made By A Weeb.       

📝**Language:** [Python3](https://www.python.org)

📚**Library:** [Pyrogram](https://docs.pyrogram.org)

📡**Hosted On:** [Heorku](https://heroku.com)

👨‍💻**Dev:** [Kousei](https://t.me/Kousei_Assistantbot)
"""
    PROGRESS = """
**📊Progress:** {0}%

**✅Done:** {1} **Of** {2}

**🚀Speed:** {3}/s

**⏳ETA:** {4}
"""
