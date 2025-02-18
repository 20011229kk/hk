"""
演示特殊字面量：None
"""
# #无return语句的返回值
# def say_hi():
#     print("你好")

# result = say_hi()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
# print("===========================")
# # 主动返回None的函数
# def say_hi2():
#     print("你好")
#     return None

# result = say_hi2()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

def check_age(age):
    if age > 18:
        return 'SUCCESS'
    else:
        return None
result = check_age(19)
if not result:
    print("未成年人，禁止入内")
