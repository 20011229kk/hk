f = open("/Users/admin/Desktop/a.txt","a",encoding="UTF-8")
# # write写入
f.write("黑马程序员")
# # flush刷新
f.flush()
# # close关闭
f.close()

f = open("/Users/admin/Desktop/a.txt","a",encoding="UTF-8")
# write写入、flush刷新
f.write("\n月薪过万")
# close关闭
f.close()

