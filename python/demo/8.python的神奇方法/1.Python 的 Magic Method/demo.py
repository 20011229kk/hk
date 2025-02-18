#在 Python 中，所有以 "__" 双下划线包起来的方法，都统称为"魔术方法"。比如我们接触最多的 __init__ 。
# 我们可以使用 Python 内置的方法 dir() 来列出类中所有的魔术方法

class User(object):
    pass

if __name__ == '__main__':
    print(dir(User()))