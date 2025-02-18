#什么是初始化函数：当你创建一个函数的时候，函数会自动被调用
class ClassA(object):
    def __init__(self):
        print('实力化成功')

a = ClassA()
print('-----------------------------')
# 构造函数（初始化函数）格式如下
# def __init__(self,[...):
#初始化参数一样是可以传递参数的
class ClassB(object):
    def __init__(self,str):
        print('实力化成功')
        print(str)
a = ClassB('小明')