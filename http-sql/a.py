import urllib.request
import re
import pymysql
import sys
print(sys.getdefaultencoding())

url = 'http://www.weather.com.cn/weather/101010100.shtml'

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    page.close()
    return html

def getCity(html):
    key = r'<title>【(.+?)天气】.+?</title>'
    res = re.findall(key, html)
    return res[0]

html = getHtml(url)
city = getCity(html)
print(city)
#
# db = pymysql.connect('localhost', 'root', 'forever367', 'testdb')
# cursor = db.cursor()
# print('%s' % city)

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='forever367', db='testdb',charset='utf8')
# port=3306不用加引号！! charset='utf8'加上！！
cursor = db.cursor()
print('1')

sql = '''INSERT INTO weather(city) VALUES('%s')''' % (city)

# city要加括号！ (city)!
try:
    cursor.execute(sql)
    print('2')
    db.commit()
    print('3')
except:
    print('exception')
    db.rollback()
db.close()
print('done')

