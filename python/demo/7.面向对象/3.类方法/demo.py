#1.类方法调用类属性
class Stu():
    name = 'kk'
    
    def test():
        print('my name is:'+Stu.name)

Stu.test()

#2.类方法传参
class Tea():
    name = 'hh'
    @classmethod
    def test(cls,age):
        print('我是'+cls.name)
        print('年龄'+str(age))

Tea.test(18)