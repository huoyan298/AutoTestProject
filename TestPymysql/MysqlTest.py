# encoding:utf-8


import pymysql
#建立数据库连接
conn = pymysql.connect(
       host = '127.0.0.1',
       user= 'root',
       passwd = '123456',
       database = 'stu',
       port=3306,
       charset='utf8'
)
# 获取游标对象
cursor = conn.cursor()
#conn = pymysql.Connect(host='localhost',user='root',passwd='123456',port=3306,db='stu')
#config ={'host':'127.0.0.1','port':3306,'user':'root','password':'123456','database':'stu','charset':'utf8'}
#connection =pymysql.connect(**config)
#获取游标
#cursor = connection.cursor()
# SQL语句
sql = "select * from stu;"