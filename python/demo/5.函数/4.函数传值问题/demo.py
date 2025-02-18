# -*- coding: UTF-8 -*-
def chagne_number( b ):
    b = 1000

b = 1
chagne_number(b)
print( b )
'''为什么打印的值是1，
   在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象。

'''
print("===========================")
def chagne_number1( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b = 1000
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = 1
chagne_number1( b )
print( '最后输出 b 的值：{}' .format( b )  )

#下面的例子是可以更改的List
# -*- coding: UTF-8 -*-

def chagne_list( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b.append(1000)
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = [1,2,3,4,5]
chagne_list( b )
print( '最后输出 b 的值：{}' .format( b )  )