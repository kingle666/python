import json
persons = [
    {
       'username': "张三",
        'Age': "12",
        'country': "中国"
    },
    {
        'username': '你好a',
        'age': 20,
        'country': '中国'
    }
]
# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)
with open('persion.json', 'w', encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons, fp, ensure_ascii=False)