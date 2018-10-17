import requests
from lxml import etree

cookie = {
    'Cookie':'user_trace_token=20181015184304-692c4bf4-4e71-4cfd-8906-6219253e0ae8; _ga=GA1.2.1135099826.1539600208; LGUID=20181015184305-18c8e815-d067-11e8-bc15-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.73712408.1539738633; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221667fc4129f205-01a02c2a87905b-51422e1f-2073600-1667fc412a0a16%22%2C%22%24device_id%22%3A%221667fc4129f205-01a02c2a87905b-51422e1f-2073600-1667fc412a0a16%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAADEAAFI1F6DEB9C84C5A5AADBE0CCBE43481EB7; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539600208,1539738633,1539769054; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539769054; LGSID=20181017173710-3879f572-d1f0-11e8-bb7a-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E8%25BF%2590%25E7%25BB%25B4%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20181017173710-3879f6d3-d1f0-11e8-bb7a-525400f775ce; SEARCH_ID=47902a4acdc34c47977e8eeb46c523f2'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
}
data = {
    'first': False,
    'pn': 1,
    'kd': '运维工程师',
}
def get_job(data):
   # url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    page = requests.post(url=url, cookies=cookie, headers=headers, data=data)
    page.encoding = 'utf-8'
    result = page.json()
    jobs = result['content']['positionResult']['result']
    for job in jobs:
        companyShortName = job['companyShortName']
        positionId = job['positionId']  # 主页ID
        companyFullName = job['companyFullName'] # 公司全名
        companyLabelList = job['companyLabelList'] # 福利待遇
        companySize = job['companySize'] # 公司规模
        industryField = job['industryField']
        createTime = job['createTime'] # 发布时间
        district = job['district'] # 地区
        education = job['education'] # 学历要求
        financeStage = job['financeStage'] # 上市否
        firstType = job['firstType'] # 类型
        secondType = job['secondType'] # 类型
        formatCreateTime = job['formatCreateTime']
        publisherId = job['publisherId'] # 发布人ID
        salary = job['salary'] # 薪资
        workYear = job['workYear'] # 工作年限
        positionName = job['positionName'] #
        jobNature = job['jobNature'] # 全职
        positionAdvantage = job['positionAdvantage'] # 工作福利
        positionLables = job['positionLables'] # 工种
        detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
        response = requests.get(url=detail_url, headers=headers, cookies=cookie)
        response.encoding = 'utf-8'
        tree = etree.HTML(response.text)
        desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')

        print(companyFullName)
        print('%s 拉勾网链接:-> %s' % (companyShortName, detail_url))

        print('职位：%s' % positionName)
        print('职位类型：%s' % firstType)
        print('薪资待遇：%s' % salary)
        print('职位诱惑：%s' % positionAdvantage)
        print('地区：%s' % district)
        print('类型：%s' % jobNature)
        print('工作经验：%s' % workYear)
        print('学历要求：%s' % education)
        print('发布时间：%s' % createTime)
        x = ''
        for label in positionLables:
            x += label + ','
        print('技能标签：%s' % x)
        print('公司类型：%s' % industryField)
        for des in desc:
            print(des)
def url(data):
    for x in range(1,50):
        data['pn'] = x
        get_job(data)

if __name__ == '__main__':
    url(data)