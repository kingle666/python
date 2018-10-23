import json
# json_str = [
#     {
#        'username': "张三",
#         'Age': "12",
#         'country': "中国"
#     },
#     {
#         'username': '你好a',
#         'age': 20,
#         'country': '中国'
#     }
# ]
# persons = json.loads(json_str)
# for person in persons:
#     print(person)
with open('persion.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)