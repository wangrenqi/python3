import urllib.request
import urllib.parse

url = 'http://192.168.56.101/login2'
value = {'nm': 'kee'}
data = urllib.parse.urlencode(value).encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode('utf-8'))


# import urllib.parse
# import urllib.request
# url = 'http://localhost/login.php'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {
# 'act' : 'login',
# 'login[email]' : 'yzhang@i9i8.com',
# 'login[password]' : '123456'
# }
# data = urllib.parse.urlencode(values)
# req = urllib.request.Request(url, data)
# req.add_header('Referer', 'http://www.python.org/')
# response = urllib.request.urlopen(req)
# the_page = response.read()
# print(the_page.decode("utf8"))


# > import urllib
# >>> parmas = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
# >>> f=urllib.urlopen("http://python.org/query",parmas)
# >>> f.read()

# data = urllib.parse.urlencode(value).encode('utf-8')
# # 发送请求，得到服务器给我们的响应
# response = urllib.request.Request(url, data)
# # 通过urllib提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
# urllib.request.urlopen(response)



# data = urllib.parse.urlencode(value)
# data = data.encode('utf-8')
#
# req = urllib.request.Request(url, data)
# with urllib.request.urlopen(req) as response:
#     the_page = response.read().decode('utf-8')
# print(the_page)


# with urllib.request.urlopen(req) as response:
#     the_page = response.read().decode('utf-8')
#     the_page.close()


# def post():
#     page = urllib.request.urlopen(url, data)
#     html = page.read().decode('utf-8')
#     page.close()
#     return html



# url = 'http://192.168.56.101/login'
# def get():
#     page = urllib.request.urlopen(url)
#     html = page.read().decode('utf-8')
#     page.close()
#     return html
# print(get())


# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
