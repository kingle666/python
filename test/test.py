# print("hello world")
# print("hello")
# number = list(range(5,30,5))
# print(number[2])
# words = ["hello","world","spame","eggs"]
# counter = 0
# max_index = len(words) - 1
# while counter <= max_index:
#     word = words[counter]
#     print(word + "!")
# #     counter = counter + 1
# for word in words:
#     print(word + "!")
# for i in range(10):
#     print("hello")
# print("*", end="---")
# print("*")
# for i in range(10):
#     test = "*" * i
#     print(test)
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         #num = col * row
#         print("%d * %d = %d " % (col,row,col * row), end="\t")
#         col += 1
#     print("")
#     row += 1

# dic = {"name": "张三","age": 8,"gendder": "男"}
# for key in dic:
#     print(key+ ":",dic[key])

# import wxpy
#
# wxpy.Bot(cache_path=True)
# wxpy.embed()

# from wxpy import *
# bot = Bot(cache_path=True)
# fren = bot.friends()
# groups = bot.groups().search("嘿嘿群")[0]
# _self = fren[2]
#
# print(groups)

# 指定好友自动回复
#性别分析
# from pyecharts import *
# # from wxpy import *
# # import webbrowser
#
# bot = Bot(cache_path=True)
# friends = bot.friends()
# male = 0
# fmale = 0
# other = 0
# #通过迭代器
# print("nums: ", friends.__len__())
# for f in friends:
#     if f.sex == 1:
#         male += 1
#     elif f.sex == 2:
#         fmale += 1
#     else:
#         other += 1
# #设置闪图对象
# pie = Pie("统计分析")
# pie.add("性别统计",["男性", "女性", "其他"],[male,fmale,other])
# pie.render("性别分析.html")
#
# webbrowser.open("性别分析.html")
#
# friend = bot.friends().search("13")[0]
# @bot.register()
# def friend_reply(msg):
#     name = msg.sender.name
#     print(name + ":" + msg.text)
#     print(msg.sender.name,friend.name)
#     if name == friend.name:
#         return "呵呵"
# @bot.register(chats=bot.groups().search("嘿嘿群")[0])
# def gropu_replay(msg):
#     return "呵呵"
#
# embed()