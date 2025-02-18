# -*- coding: UTF-8 -*-

def print_user_info( name , age , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return
# 调用 print_user_info 函数

print_user_info( '两点水' , 18 , '女')
#sex不传值的时候 就用默认值
print_user_info( '三点水' , 25 )
print("==========================")


# 一般情况下，我们需要给函数传参的时候，是要按顺序来的，如果不对应顺序，就会传错值。
# 不过在 Python 中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。
def user(name , age , sex='男'):
    print('姓名:{}'.format(name),end='')
    print('年龄:{}' .format(age),end='')
    print('性别:{}' .format(sex))
    return

user('kk',11,'女')
user(23,'不知','hh')



#不定长参数
'''有些时候，我们在设计函数的时候，我们有时候无法确定传入的参数个数。
那么我们就可以使用不定长参数。
Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号 * 。
如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。'''
def user_info(name , age , sex , * hobby):
    print('名字:{}'.format(name),end='')
    print('年龄:{}'.format(age),end='')
    print('性别:{}'.format(sex),end='')
    print('爱好:{}'.format(hobby))

user_info('kk', 22, '男', '踢足球','听歌')


#只接受关键字参数
'''关键字参数使用起来简单，不容易参数出错，那么有些时候，我们定义的函数希望某些参数强制使用关键字参数传递，这时候该怎么办呢？
将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果'''
def student(name , * , age , sex):
    print('名字:{}'.format(name),end='')
    print('年龄:{}'.format(age),end='')
    print('性别:{}'.format(sex))
    return

student(name='ll',age=12,sex='男')
# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
# student('dd',12,'女')
student('kkkk',age=23,sex='男')