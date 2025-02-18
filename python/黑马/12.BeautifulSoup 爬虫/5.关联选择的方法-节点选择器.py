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

# 获取p节点的⼦节点
print(soup.p.contents)


# 获取p节点的每⼀个⼦节点
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)


# 获取p节点所有的⼦孙节点
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)