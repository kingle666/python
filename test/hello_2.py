def test():
    # import keyword
    # print(keyword.kwlist)
    # age = float(input("请输入你的年龄: "))
    # if age >= 18:
    #     print("哇哇哇哇哇哇哇")
    # else:
    #     print("走开")
    #
    # if age >=0 and age <=120:
    #     print ("okokokokoko")
    # else:
    #     print ("nononono")
    # print("asda啊")
    # pyth_cord = float(input("请输入你的年龄: "))
    # c_cord = float(input("请输入你的年龄: "))
    # if pyth_cord >60 and c_cord >60:
    #     print("成绩合格")
    # else:
    #     print("不及格")
    # day=input("请输入节日: ")
    # if day == "过年":
    #     print("买年货")
    # elif day == "生日":
    #     print("买蛋糕")
    # else:
    #     print("没事做")
    import random
    player = float(input("请输入要出的拳 石头(1)/剪刀(2)/布(3) : "))
    computer = random.randint(1, 3)
    print("玩家出的拳是 %d - 电脑出的拳是 %d" % (player, computer))
    if (player == 1 and computer == 2) \
            or (player == 2 and computer == 3) \
            or (player == 3 and computer == 1):

        print("玩家胜利")
    elif (player == 2 and computer == 1) \
            or (player == 3 and computer == 2) \
            or (player == 1 and computer == 3):

        print("电脑胜利")
    else:
        print("平局")
