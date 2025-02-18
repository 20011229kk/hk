# 既然一个在创建的时候，会调用构造函数，那么理所当然，这个当一个类销毁的时候，就会调用析构函数。
# 析构函数语法如下：
# def __del__(self,[...):
class ClassA(object):
    def __init__(self,name):
        self.name = name
        print('创建了'+self.name)
    def __del__(self):
        print('被销会'+self.name)
    
a = ClassA('对象')
del a