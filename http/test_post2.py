import urllib
import urllib.request
import urllib.parse

# url = 'http://localhost:8080/student'
# value = {'name': '111', 'age': '111', 'id': '111'}
# postdata = urllib.parse.urlencode(value).encode('utf-8')
#
# req = urllib.request.Request(url, postdata)
# res = urllib.request.urlopen(req)
# html = res.read().decode('utf-8')
# print(html)


# url = 'http://192.168.56.101/login2'
# value = {'nm': 'kee'}
# data = urllib.parse.urlencode(value).encode('utf-8')
# req = urllib.request.Request(url, data)
# response = urllib.request.urlopen(req)
# the_page = response.read()
#
# print(the_page.decode('utf-8'))


# url = "https://system.netsuite.com/pages/customerlogin.jsp?country=US"
# postdata = urllib.parse.urlencode({'email': 'yicui49@gmail.com', 'password': 'fashlets123', 'Submit': ''})
# postdata = postdata.encode('utf-8')
#
# res = urllib.request.urlopen(url, postdata)
# print(res.status, res.reason)
#
# if (res.status != 200):
#     exit()
#
# print('ok')

url = 'http://localhost:8080/student'
value = {'name': '111', 'age': 111, 'id': 111}
postdata = urllib.parse.urlencode(value).encode('utf-8')

res = urllib.request.urlopen(url, postdata)
print(res.status, res.reason)

if (res.status != 200):
    print('error================')
else:
    print('ok===================')
