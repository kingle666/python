import urllib.request, urllib.parse
import re

pattern = re.compile(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>')


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("user-agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html

def page_counts(start_page_num, end_page_num):
    all_page_list = []
    for i in range(start_page_num, end_page_num + 1):
        cur_page_html = open_url("http://www.budejie.com/text/%s" % i)
        one_page_list = re.findall(pattern, cur_page_html)
        for item in one_page_list:
            all_page_list.append(item)
    return all_page_list

def save(start_page_num, end_page_num):
    with open("a.txt", "w", encoding="utf-8") as f:
        for item in page_counts(start_page_num, end_page_num):
            if r'<br />' in item:
                new_item = re.sub(r'<br />', "\n", item)
                f.write(new_item)
            else:
                new_item = item + "\n"
                f.write(new_item)

save(1, 1)