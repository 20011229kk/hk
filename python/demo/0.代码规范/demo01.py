#简明概述
#1.空行   模块级函数和类定义之间空两行；    类成员函数之间空一行；
class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass   


#2.import语句
# 正确的写法
import os
import sys

# 不推荐的写法
import sys,os

# 正确的写法
from subprocess import Popen, PIPE
#import语句应该放在文件头部，置于模块说明及docstring之后，于全局变量之前；
#import语句应该按照顺序排列，每组之间用一个空行分隔
import os
import sys

import msgpack
import zmq

import foo


#3.空格
#函数的参数列表中，,之后要有空格
# 正确的写法
def complex(real, imag):
    pass

# 不推荐的写法
def complex(real,imag):
    pass
#函数的参数列表中，默认值等号两边不要添加空格
# 正确的写法
def complex(real, imag=0.0):
    pass

# 不推荐的写法
def complex(real, imag = 0.0):
    pass


#4.换行
#第二行缩进到括号的起始处
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
#第二行缩进 4 个空格，适用于起始括号就换行的情形
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
#使用反斜杠\换行，二元运算符+ .等应出现在行末；长字符串也可以用此法换行
session.query(MyTable).\
        filter_by(id=1).\
        one()

print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')

#禁止复合语句，即一行中包含多个语句
# 正确的写法
do_first()
do_second()
do_third()

# 不推荐的写法
do_first();do_second();do_third();