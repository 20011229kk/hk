import requests
from bs4 import BeautifulSoup
 
def fetch_data(url):
    """从指定 URL 抓取数据"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
 
    titles = [title.get_text() for title in soup.find_all('h2')]  # 假设标题在 <h2> 标签中
    print("抓取到的标题:")
    for title in titles:
        print(title)
 
# 使用示例
fetch_data('https://blog.csdn.net/qq_36807888/article/details/144149384?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog.none-task-blog-hot-11-144149384-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog.none-task-blog-hot-11-144149384-null-null.nonecase')
