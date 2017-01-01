import requests
from bs4 import BeautifulSoup

resp = requests.get('http://118.89.33.77:8000')
# print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup.prettify())
# print(soup.body.string.strip())

a = soup.title.string
print(a)
