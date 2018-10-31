import requests
from lxml import etree
from urllib import request
import os
import re
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers)
    text = reponse.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?\.\/\"<>:？！，!]','',alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        filename = re.sub(r'!dta', '', filename)
        request.urlretrieve(img_url,'image2/'+filename)
        print (filename + "完成")
def main():
    os.mkdir("image2")
    for x in range(1,200):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)
if __name__ == '__main__':
    main()