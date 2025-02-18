from bs4 import BeautifulSoup
html_str = """
<html><head><title>Beautiful Soup爬虫</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names
were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_str, 'html.parser')
#抽取title标签
print(soup.title)
# 打印soup.title的类型
print(type(soup.title))

# 抽取a标签
print(soup.a)
# 打印soup.a的类型
print(type(soup.a))


print("--------------------")
# 获取所有的<a>标签
a_tags = soup.find_all('a')

# 打印所有的<a>标签
for a_tag in a_tags:
    print(a_tag)