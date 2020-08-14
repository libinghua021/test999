import pymysql
#打开数据库连接
conn = pymysql.connect('localhost', user="root", passwd="test123", db="test999")
print (conn)
print (type(conn))