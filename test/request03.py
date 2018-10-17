import requests
proxy = {
    'http': '121.31.194.185:8123'
}
response = requests.get("http://httpbin.org/ip",proxies=proxy)
print (response.text)