import requests
#respomse = requests.get("http://www.baidu.com")
# print(type(respomse.text))
# print(respomse.text)
# print(type(respomse.content))
# print(respomse.content.decode('utf-8'))
# print(respomse.url)
# print(respomse.encoding)
# print(respomse.status_code)
kw = {'wd': '你好'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
response = requests.get("http://www.baidu.com/s",params=kw,headers=headers)
with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
print(response.url)