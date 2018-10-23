import requests
import re
def parse_page(url):
    headers = {
        'USer-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    respose = requests.get(url,headers)
    text = (respose.text)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynsties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p class="source".*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    wenben = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    peoms = []
    for conter in wenben:
        x = re.sub(r'<.*?>',"",conter)
        peoms.append(x.strip())
    poem2 = []
    for calue in zip(titles,dynsties,authors,wenben):
        titles,dynsties,authors,wenben = calue
        poem = {
            '标题':titles,
            '朝代':dynsties,
            '作者':authors,
            '文本':wenben
        }
        poem2.append(poem)
    for poem in poem2:
        print(poem)
        print('*'*40)

def main():
    #url = 'https://www.gushiwen.org/default_1.aspx'
    for x in range(1,10):
        url = "https://www.gushiwen.org/default_%s.aspx" % x
        x 
        parse_page(url)

if __name__ == "__main__":
    main()


