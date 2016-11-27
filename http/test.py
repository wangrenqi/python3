import urllib.request
import urllib.parse


# url = 'http://192.168.56.101/login'
url = 'http://localhost:8080/student'
def get():
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    page.close()
    return html
print(get())



# import urllib.request
# import re
#
# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read().decode('utf-8')
#     page.close
#     return html
#
# def get_city(html):
#     reg = r'<title>【(.+?)天气】.+?</title>'
#     get_list = re.findall(reg,html)
#     return get_list[0]
#
# html = getHtml("http://www.weather.com.cn/weather/101010100.shtml")
# print("所在城市:"+get_city(html))