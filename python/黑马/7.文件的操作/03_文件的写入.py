import time
f = open("/Users/admin/Desktop/a.txt","w",encoding="UTF-8")
f.write("hello")
f.write("黑马")
#刷新
f.flush()
#关闭
f.close()

