import csv
def write_csv_demo1():
    headers = ['username', 'Age', 'height']
    values = {
        ('张三', 18, 180),
        ('李四', 20, 175),
        ('王麻子', 22, 182)
    }
    with open('c.csv', 'w', encoding='utf-8', newline='') as fp:
        wrinter = csv.writer(fp)
        wrinter.writerow(headers)
        wrinter.writerows(values)
def write_csv_demo2():
    headers = ['username','age','height']
    values = [
        {'username':'站西安','age':'12','height':'180'},
        {'username': 'lishi ', 'age': '12', 'height': '180'},
        {'username': '哈后', 'age': '12', 'height': '180'}
    ]
    with open('c2.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        writer.writeheader()
        writer.writerows(values)
if __name__ == "__main__":
    write_csv_demo2()