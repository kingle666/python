import requests
from lxml import etree
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E4%BA%91%E8%AE%A1%E7%AE%97?px=default&city=%E4%B8%8A%E6%B5%B7',
    'Cookie': 'user_trace_token=20181015184304-692c4bf4-4e71-4cfd-8906-6219253e0ae8; _ga=GA1.2.1135099826.1539600208; LGUID=20181015184305-18c8e815-d067-11e8-bc15-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221667fc4129f205-01a02c2a87905b-51422e1f-2073600-1667fc412a0a16%22%2C%22%24device_id%22%3A%221667fc4129f205-01a02c2a87905b-51422e1f-2073600-1667fc412a0a16%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; WEBTJ-ID=20181107200156-166ee0cec2f1a7-08894d1a8cf99d-51422e1f-2073600-166ee0cec3019e; _gid=GA1.2.1652335099.1541592116; LGSID=20181107200200-eecf3514-e284-11e8-904d-525400f775ce; JSESSIONID=ABAAABAAAIAACBIAA52CA4F2A47C33B835C6B69502F1912; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539769054,1541592116,1541592121,1541592124; TG-TRACK-CODE=search_code; SEARCH_ID=0f8a30eb9cee465f9b0ae34e39045c16; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541593682; LGRID=20181107202801-91876d0a-e288-11e8-9051-525400f775ce',
    'X-Anit-Forge-Token': "None",
    'X-Requested-With': "XMLHttpRequest"
}

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    data = {
        'first': 'false',
        'pn': 1,
        'kd':'云计算'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']  # 主页ID
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_postion_detail(position_url)
            break
        break
def parse_postion_detail(url):
    positions = []
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    position = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r"[\s/]","",city)
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]", "", work_years)
    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]", "", education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    company_name = html.xpath("//h2[@class='f1']/text()")
    print(company_name)
    position = {
        'name': position,
        'company_name': company_name,
        'salary': salary,
        'city': city,
        'work_years': work_years,
        'education': education,
        'desc': desc
    }
    positions.append(position)
    print(positions)
def main():
    request_list_page()

if __name__ == '__main__':
    main()