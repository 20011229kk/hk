#演示使用多个变量，接收多个返回值
def tesr_return():
    return 1,"hello",True

x,y,z = tesr_return()
print(x)
print(y)
print(z)