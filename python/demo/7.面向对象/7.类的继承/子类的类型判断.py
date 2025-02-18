class User1(object):
    pass

class User2(User1):
    pass

class User3(User2):
    pass

if __name__ == '__main__':
    uer1 = User1()
    user2 = User2()
    user3 = User3()
    # isinstance()就可以告诉我们，一个对象是否是某种类型
    print(isinstance(user3,User2))
    print(isinstance(user3,User1))
    print(isinstance(user3,User3))
     # 基本类型也可以用isinstance()判断
    print(isinstance(123,int))
    print(isinstance('123',str))
    print(isinstance([1,2,3],list))
    print(isinstance({'name':'kk','age':18},list))
