import urllib.parse
import urllib.request

value = {'name': '111', 'age': '11', 'id': '11'}
data = urllib.parse.urlencode(value).encode('utf-8')
url = 'http://localhost:8080/student'
# request = urllib.Request(url, data)
request = urllib.request.Request(url, data)
# response = urllib2.urlopen(request)
response = urllib.request.urlopen(request)
print(response.read())
