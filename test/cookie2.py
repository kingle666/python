from urllib import request
from http.cookiejar import MozillaCookieJar
cookiejar = MozillaCookieJar('cookie.txt')
headler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(headler)
resp = opener.open('http://www.baidu.com')
cookiejar.save(ignore_discard=True)