#1.定义类的继承
#继承的好处
#1.可以继承父类的属性和方法
#2.可以自己定义，覆盖父类的属性和方法



#调用父类的方法
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def get_account(self):
        return self.account
    def get_name(self):
        return self.name


class UserInfo2(UserInfo):
    pass


if __name__ == '__main__':
    userInfo2 = UserInfo2('两点水', 23, 347073565)
    print(userInfo2.get_account())
    print(userInfo2.get_name())

        
        