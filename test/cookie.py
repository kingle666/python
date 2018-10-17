from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
}
def get_opner():
    cookiejar = CookieJar()
    headler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(headler)
    return opener
def get_header(opener):
    data = {
        'email': '924255352@qq.com',
        'password': '15070640127ling'
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)
def visit_profile(opener):
    dapen_url = "http://www.renren.com/880151247/profile"
    req = request.Request(dapen_url,headers=headers)
    resp = opener.open(req)
    with open('renren.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))
if __name__ == '__main__':
    opener = get_opner()
    get_header(opener)
    visit_profile(opener)