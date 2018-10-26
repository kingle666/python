import pymysql
conn = pymysql.connect(host='172.16.1.52',user='root',password='123456',database='mysql',port=3306)
curor = conn.cursor()
sql = """
select user,host from user
"""
curor.execute(sql)
results = curor.fetchmany(2)
for result in results:
    print(result)
conn.close()