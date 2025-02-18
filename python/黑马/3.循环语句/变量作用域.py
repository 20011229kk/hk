i = 0
for i in range(5):
    print(i)
#这里将会打印i的最终值4
print(i)

#通过for循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()