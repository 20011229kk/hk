#多态的概念
# 多态的概念其实不难理解，它是指对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。
class User(object):
    def __init__(self,name):
        self.name = name

    def printUser(self):
        print('hello'+self.name)


class VipUser(User):
    def printUser(self):
        print('hello vip'+self.name)

class SuperUser(User):
    def printUser(self):
        print('hello super'+self.name) 

def printUserInfo(user):
    user.printUser()

if __name__ == '__main__':
    vipUser = VipUser('两点水')
    printUserInfo(vipUser)
    superUser = SuperUser('kk')
    printUserInfo(superUser)
    
