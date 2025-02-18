f = open("/Users/admin/Desktop/a.txt","r",encoding="UTF-8")
# 方式1：读取全部内容，通过字符串count方法统计a单词数量
# content = f.read()
# count = content.count("a")
# print(f"a在文件中出现了:{count}次")

# 方式2：读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "a":
            count += 1
# 判断单词出现次数并累计
print(f"a出现的次数是：{count}")
# 关闭文件
f.close()