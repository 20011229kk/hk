"""
演示函数作为参数传递
"""
#定义一个函数，在接受另一个函数作为传入参数
def test(compute):
    result = compute(1,2)
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果：{result}")

def compute(x,y):
    return x + y

test(compute)