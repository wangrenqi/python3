import urllib.request
import re

url = 'http://www.weather.com.cn/weather/101010100.shtml'


def getHtml(url):
    page = urllib.request.urlopen(url)

    html = page.read().decode('utf-8')

    page.close()

    return html

def getCity(html):
    key = r'<title>【(.+?)天气】.+?</title>'
    res = re.findall(key,html)
    return res[0]
html = getHtml(url)
print(getCity(html))
