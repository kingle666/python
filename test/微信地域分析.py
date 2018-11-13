from pyecharts import Map
from wxpy import *
import webbrowser

bot = Bot(cache_path=True)

friends = bot.friends()

mapdic = {}

for f in friends:
    province = f.province

    if f.province in mapdic:
        mapdic[f.province] += 1
    else:
        mapdic[province] = 1

map = Map("低于分析")
map.add("地域分析",mapdic.keys(),mapdic.values(),is_visualmap=True)
map.render("地域.html")

webbrowser.open("地域.html")