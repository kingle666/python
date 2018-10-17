import requests
data = {
    'first':'true',
    'pn': '1',
    'kd': '运维工程师'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88?px=default&city=%E4%B8%8A%E6%B5%B7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
response = requests.post('https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88?px=default&city=%E4%B8%8A%E6%B5%B7#filterBox',data=data,headers=headers)
print(type(response.json()))
print(response.json())