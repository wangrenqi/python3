import pymysql
import sys

print(sys.version)
print(sys.getdefaultencoding())

db = pymysql.connect(host="localhost", user="root", passwd="forever367", db="testdb", charset="utf8")
# 一定要加charset='utf8'

cursor = db.cursor()

# str = '上海'
# print(str.encode())
# str1 = str.encode().decode('utf-8')

sql = '''INSERT INTO weather(city) VALUES('%s')''' % ('啊啊')

try:
    cursor.execute(sql)
    db.commit()
except:
    print('excption')
    db.rollback()

db.close()
