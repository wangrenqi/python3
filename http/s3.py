html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# print(soup.title)

# print(soup.a)

# print(soup.title.string)

# print(soup.a.parent.name)

# print(soup.find_all('a')[0])

# print(soup.find(id='link3'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())


# soup.title
# <title>The Dormouse's story</title>

# soup.title.name
# u'title'

# soup.title.string
# u'The Dormouse's story'

# soup.title.parent.name
# u'head'

# soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# u'title'

# soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 从文档中找到所有<a>标签的链接:

# for link in soup.find_all('a'):
#     print(link.get('href'))
#     # http://example.com/elsie
#     # http://example.com/lacie
#     # http://example.com/tillie
# 从文档中获取所有文字内容:

# print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...

# alist = soup.find_all('a')
# for a_item in alist:
#     print(a_item)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# for a_item in alist:
#     print(a_item.string)
# Elsie
# Lacie
# Tillie    

