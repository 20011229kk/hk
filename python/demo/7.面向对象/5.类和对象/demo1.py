#1.类的实例化
#强调一下 类的实例化和直接使用类是不同的格式
#直接使用
class ClassA():
    var1 = '两点水'

    @classmethod
    def fun1(cls):
        print('var1 值为：' + cls.var1)


ClassA.fun1()
print('-----------------------------')
#实例化
class ClassA(object):
    var1 = 'kk'
#这里没有了classmethod cls变成了self，self可以改成任何你喜欢的字母
    def fun1(self):
        print('var1的值是'+self.var1)
#实例化
a = ClassA()
#实例化之后使用它的方法
a.fun1()
#或者是使用它的属性
print(a.var1)




# 除此之外，在这里，还要强调一个概念，当你把类实例化之后，里面的属性和方法，
# 就不叫类属性和类方法了，改为叫实例属性和实例方法，也可以叫对象属性和对象方法。为什么要这样强调呢？
# 因为一个类是可以创造出多个实例对象出来的。
#实例化
class ClassA(object):
    var1 = 'kk'
#这里没有了classmethod cls变成了self，self可以改成任何你喜欢的字母
    def fun1(self):
        print('var1的值是'+self.var1)
#实例化
a = ClassA()
#实例化之后使用它的方法
a.fun1()
#或者是使用它的属性
print(a.var1)
b = ClassA()
b.fun1()
print(b.var1)