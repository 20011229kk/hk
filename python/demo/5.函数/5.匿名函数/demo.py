#使用lambda表达式
# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda sum1, sum2: sum1 + sum2
print(sum(1,2))

'''
注意：尽管 lambda 表达式允许你定义简单函数，但是它的使用是有限制的。 
你只能指定单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。
'''

# -*- coding: UTF-8 -*-

num2 = 100
sum1 = lambda num1 : num1 + num2 

num2 = 10000
sum2 = lambda num1 : num1 + num2 

print( sum1( 1 ) )
print( sum2( 1 ) )

#你会认为输出的是101和100001
#结果输出是：100001，10001