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
    
#重写父类方法
class UserInfo2(UserInfo):
    def __init__(self, name, age, account,sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex

if __name__ == '__main__':
    userInfo2 = UserInfo2('两点水', 23, 347073565,'男')
    #打印所有的值
    print(userInfo2.__dict__)
    print(userInfo2.get_account())
    print(userInfo2.get_name())