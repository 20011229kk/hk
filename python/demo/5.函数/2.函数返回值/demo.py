# -*- coding: UTF-8 -*-

# def sum(num1,num2):
# 	# 两数之和
# 	# 还通过内置函数isinstance()进行数据类型检查，检查调用函数时参数是否是整形和浮点型。如果参数类型不对，会报错，
# 	if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
# 		raise TypeError('参数类型错误')
# 	return num1+num2

# print(sum(0.1,2))

# -*- coding: UTF-8 -*-

def  division ( num1, num2 ):
	# 求商与余数
         a = num1 % num2
         b = (num1-a) / num2
         return b , a

num1 , num2 = division(9,4)
print(num1,num2,sep='\n')
