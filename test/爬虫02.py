from urllib import request
# url = "http://httpbin.org/ip"
# handler = request.ProxyHandler({"http":"115.218.208.122:9000"})
# opener = request.build_opener(handler)
# # req = request.Request("http://httpbin.org/ip")
# resp = opener.open(url)
# print(resp.read())
#
dapeng_url = "http://www.renren.com/880151247/profile"

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
    'cookie': 'anonymid=jnbglqm6-27xtx8; depovince=GW; jebecookies=00efb27c-4fc3-4329-9466-f21e233c3614|||||; _r01_=1; JSESSIONID=abcSt9pd8nLmS4Kx897zw; ick_login=68ef076c-94af-45a8-a186-c6bc7b9e71e6; hibext_instdsigdipv2=1; jebe_key=acad5f50-1e3b-4c62-b237-087f6fb60522%7C059ce8fbb760b6045ed255b2bb4934ad%7C1539678520794%7C1; t=a6c2605625a993523a32fbac2e5ecb284; societyguester=a6c2605625a993523a32fbac2e5ecb284; id=968372964; xnsid=84081448; ver=7.0; loginfrom=null; wp_fold=0'
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
with open('renren.html','w') as fp:
    fp.write(resp.read().decode('utf-8'))