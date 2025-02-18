# 在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。
#1.生成器的创建

# 最简单最简单的方法就是把一个列表生成式的 [] 改成 ()
# -*- coding: UTF-8 -*-
gen= (x * x for x in range(10))
print(gen)

#2.便利生成器的元素
for i in gen:
    print(i)
print('\n----------------------------')

#3.函数的形式 实现生成器
def my_function():
    for i in range(10):
        print(i)
my_function()
# 以上的例子 如果我们需要把它变成生成器 只需要将print(i)变成yield(i)
# -*- coding: UTF-8 -*-
def my_function():
    for i in range(10):
        yield i

print(my_function())