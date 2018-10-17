
# resp = request.urlopen('http://www.baidu.com')
# print(resp.getcode())
# request.urlretrieve('https://ss0.bdstatic.com/-0U0b8Sm1A5BphGlnYG/kmarketingadslogo/935fa2084da61d91adc5eeb161d3e42b_259_194.jpg','1.jpg')

# data = {'name':'爬虫时评','great':'hello world','age':'18'}
# result = parse.urlencode(data)
# print(result)
# url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=SE_Pclogo_6ysd4c7a&wd=zabbix%20%E8%87%AA%E5%8A%A8%E6%B3%A8%E5%86%8C&oq=%25E4%25BB%258A%25E6%2597%25A5%25E6%2596%25B0%25E9%25B2%259C%25E4%25BA%258B&rsv_pq=8e279f9e0000c396&rsv_t=eb27xOaCdD%2FUttjaKwbP2u5Fq7PwP8mCXsden3cHuNvWkzjn7KCXNr8NO1miFHZY6rkoEk%2FZaRja&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_sug1=2&rsv_sug7=101&rsv_sug2=1&rsp=1&rsv_sug9=es_0_1&inputT=1413&rsv_sug4=1883&rsv_sug=9'
# params = {"wd":"王炸"}
# qs = parse.urlparse(url)
# qs = parse.urlsplit(url)
# print(qs)
# print('scheme:',qs.scheme)
# print('netloc:',qs.netloc)
# print('path:',qs.path)
# print('query:',qs.query)
# print('fragment:',qs.fragment)

# url = url + "?" + qs
# resp = request.urlopen(url)
# request.urlretrieve(url,'baidu.html')
# print(qs)
# qwe = parse.parse_qs(qs)
# print(qwe)
from urllib import request
from urllib import parse
from urllib import request
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# resp = request.urlopen(url)
# print(resp.read())
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=sug&suginput=python'
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
reps = request.urlopen(req)
print(reps.read().decode('utf-8'))