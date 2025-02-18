#演示局部变量
# def test1():
#     num = 100
#     print(num)

# test1

#全局变量
# num = 200
# def test2():
#     print(f"test2:{num}")
# def test3():
#     print(f"test3:{num}")

# test2()
# test3()
# print(num)

#在函数内修改全局变量
# num = 200
# def test():
#     print(f"test:{num}")
# def test1():
#     num = 500
#     print(f"test1:{num}")

# test()
# test1()
# print(num)

# global关键字，在函数内声明变量为全局变量
num = 200
def test1():
    print(f"test1: {num}")
def test2():
    global num      # 设置内部定义的变量为全局变量
    num = 500
    print(f"test2: {num}")

test1()
test2()
print(num)