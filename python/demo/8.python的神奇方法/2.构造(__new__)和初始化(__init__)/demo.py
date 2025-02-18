#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class User(object):
    def __new__(cls, *args, **kwargs):
        # 打印 __new__方法中的相关信息
        print('调用了 def __new__ 方法')
        print(args)
        # 最后返回父类的方法
        return super(User, cls).__new__(cls)

    def __init__(self, name, age):
        print('调用了 def __init__ 方法')
        self.name = name
        self.age = age


if __name__ == '__main__':
    usr = User('两点水', 23)

#显而易见，__new__方法是在__init__方法之前被调用的，__new__方法的返回值是当前类的一个实例，
# 这个实例会传递给__init__方法中定义的self参数，以便实例可以被正确地初始化。
#简单来说，—__new__方法是用来创建实例的，而__init__方法是用来初始化实例的。