import pymysql
conn = pymysql.connect(host='192.168.1.183',user='root',password='123456',database='python',port=3306)
curor = conn.cursor()
sql = """
insert into user(id,username,age,password) value(null,'bbb',20,'123456')
"""
curor.execute(sql)
conn.commit()
conn.close()