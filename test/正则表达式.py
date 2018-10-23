import re
# text = '13254654215'
# req = re.match('1[34587]\d{9}',text)
# print(req.group())
# text = 'qweqweqr@163.com'
# req = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(req.group())
# text = 'https://www.baidu.com/baidu?wd=sadad&tn=monline_4_dg&ie=utf-8'
# req = re.match('(http|https|ftp)://[^\s]+',text)
# print(req.group())
text = '12345646332216546X'
print(len(text))
req = re.match('\d{17}[\dxX]]', text)
print(req.group())