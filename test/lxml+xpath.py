from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tenxun.html",parser=parser)
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
# trs = html.xpath("//tr[2]")[0]
# print(etree.tostring(trs,encoding='utf-8').decode('utf-8'))
# trs = html.xpath("//div[@class='border clearfix']")
# print(etree.tostring(trs,encoding='utf-8').decode('utf-8'))
# aList = html.xpath("//a/@href")
# for a in aList:
#    print(a)
trs = html.xpath("//tr[position()>1]")
positions = []
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    fullurll = 'http://hr.tencent.com/' + href
    title = tr.xpath("./td[1]//text()")[0]
    category = tr.xpath("./td[0]/text()")[0]
    nums = tr.xpath("./td[3]/text()")[0]
    # address = tr.xpath("./td[4]/text()")[0]
    # pubtime = tr.xpath("./td[5]/text()")[0]

    position = {
        'url': fullurll,
        'title': title,
        'nums': nums,
        'category': category,
        # 'address': address,
        # 'pubtime': pubtime
    }
    positions.append(position)
print(positions)