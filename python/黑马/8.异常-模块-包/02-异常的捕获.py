# #基本捕获语法
# try:
#     num = 1 / 0
# except:
#     print("出现异常了，除数不能为0")
#     num = 1 / 1

# #捕获指定的异常
# try:
#     print(name)
#     num = 1 / 0
# except NameError as e:
#     print("出现了为定义的变量")
#     print(e)

#捕获多个异常
try:
    1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除以0的异常错误")
    print(e)

#捕获所有异常
# try:
#     num = 1 / 0
# except Exception as e:
#     print("出现异常了")
#     num = 1 / 1
# else:
#     print("好高兴，没有异常。")
# finally:
#     print("我是finally，有没有异常我都要执行")
    