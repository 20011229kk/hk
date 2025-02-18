'''之前在学习list的创建时，需要手动一个一个的将元素写进到list中，这样的话元素多了就会很麻烦
我们可以向下面这样写'''
# -*- coding: UTF-8 -*-

list1=list ( range (1,31) )
print(list1,'\n----------------------')

#之前打印九九乘法表时，很麻烦，现在一句话就可以打印出来
# print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))


#下面来了解list生成式的创建语法
# [expr for iter_var in iterable] 
# [expr for iter_var in iterable if cond_expr]

list1 = [x * x for x in range(1,11)]
print(list1)

list2 = [x * x for x in range(1,11) if x % 2 ==0]
print(list2)

