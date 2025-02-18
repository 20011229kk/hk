from bs4 import BeautifulSoup
html_str = """
<html><head><title>The Dormouse's story</title></head>
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
# 获取a标签的名字
print(soup.a.name)
#获取a标签的属性
print(soup.a.attrs)
#获取a标签的内容
print(soup.a.string)


"""
    节点选择器提取信息的方法：
    1.soup.tag.name
    用来提取节点名称
    2.soup.tag.attrs
    用来提取属性
    3.soup.tag.string
    用来提取内容
"""



