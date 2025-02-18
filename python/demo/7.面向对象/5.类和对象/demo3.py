#类方法和实例方法
#类方法改变，实例方法会不会改变
class ClassA(object):
    var1 = 'hh'

    def fun1(self):
        print('小明今天放学要去看电影')

a = ClassA()
a.fun1()

def NewFun1(self):
    print('小明不去了')
ClassA.fun1 = NewFun1

a.fun1()


print('--------------------------------')
#相反 实例方法改变，类方法会不会改变
# class ClassB(object):
#     var2 = 'kk'

#     def fun2(self):
#         print('小明今天要去踢足球')

# b = ClassB()
# b.fun2()

# def NewFunB(self):
#     print('小明决定不去了')

# b.fun2 = NewFunB
# ClassB.fun2()

'''运行报错 
Traceback (most recent call last):
  File "/Users/python/demo/7.面向对象/5.类和对象/demo3.py", line 34, in <module>
    ClassB.fun2()
TypeError: fun2() missing 1 required positional argument: 'self'很显然我们是不能改变实例化方法的'''