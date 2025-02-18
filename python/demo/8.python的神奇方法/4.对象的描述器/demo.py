class User(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __get__(self,obj,objtype):
        print('获取name的值')
        return self.name
    
    def __set__(self,obj,value):
        print('设置name的值')
        self.name = value

class MyClass(object):
    x = User('kk',18)
    y = 10


if __name__ == '__main__':
    m = MyClass()
    print(m.x)
    print('\n')

    m.x = '三点水'
    print(m.x)

    print('\n')

    print(m.x)

    print('\n')

    print(m.y)