import os
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

async def a2tService(c, m):
    if Config.LOG_CHAT & int(Config.LOG_CHAT) is not None:
        user = await c.get_users(int(m.from_user.id))
        try:
            await c.send_message(Config.LOG_CHAT,
                                 Presets.A2T_REPORT.format(
                                     '@' + user.username if user.username else user.first_name))
        except Exception:
            pass

async def t2aService(c, m):
    if Config.LOG_CHAT & int(Config.LOG_CHAT) is not None:
        user = await c.get_users(int(m.from_user.id))
        try:
            await c.send_message(Config.LOG_CHAT,
                                 Presets.T2A_REPORT.format(
                                     '@' + user.username if user.username else user.first_name))
        except Exception:
            pass
