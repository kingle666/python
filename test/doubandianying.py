import requests
from lxml import etree
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
    'Referer': 'https://movie.douban.com/cinema/nowplaying/shanghai/'
}
url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
response = requests.get(url,headers=headers)
text = response.text



html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }
    movies.append(movie)
print(movies)