#类属性的访问控制
# 一般情况下，我们会使用 __private_attrs 两个下划线开头，声明该属性为私有
# 不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

class UserInfo(object):
    def __init__(self,name,age,account):
        #可以公开访问的属性
        self.name = name
        #私有属性
        self._age = age
        #这里是两个下划线，在创建这个类的时候，是不可以直接访问到两个下划线的属性的
        self.__account = account

    def get_account(self):
        return self.__account
    
    
if __name__ == '__main__':
    userInfo = UserInfo('两点水',23,347073565)
    print(userInfo.__dict__)
    # 打印构造函数中的属性
    print(userInfo.get_account())
     # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)



#类的专有方法
# __init__ : 构造方法，在生成对象时调用
# __del__ : 析构方法，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
# __str__: 打印对象
# __contains__: 定义in的行为
# __iter__: 迭代器
# __doc__: 获取文档信息



#__add__加运算的例子，数字相加
class Sum(object):
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return Sum(self.a + other.a)
    def __sub__(self,other):
        return Sum(self.a - other.a)
    
    def __str__(self):
        return 'Sum:%d' % self.a

if __name__ == '__main__':
    sum1 = Sum(1)
    sum2 = Sum(2)
    print(sum1 + sum2)
    print(sum1 - sum2)

    


