import re
import requests
def parse_page(url):
    headers = {
        'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    respone = requests.get(url,headers)
    # print(respone.text)
    text = respone.text
    contents = re.findall(r'<div\sclass="content">.*<span>(.*?)</span>',text,re.S)
    print(contents)
    duanzi = []
    for content in contents:
        x = re.sub(r'<.*?>','',content)
        duanzi.append(x.strip())
        print('='*50)
def main():
    url = "https://www.qiushibaike.com/text/page/1/"
    for x in range(1,10):
        url = 'https://www.qiushibaike.com/text/page/%s/' % x
        parse_page(url)
if __name__ == '__main__':
    main()