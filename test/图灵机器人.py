from wxpy import *

bot = Bot(cache_path=True)
friend = bot.friends().search("")[0]