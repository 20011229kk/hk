'''tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。 也就是说元组（tuple）是不可变的，那么不可变是指什么意思呢？
元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
那么为什么要有 tuple 呢？
那是因为 tuple 是不可变的，所以代码更安全。
所以建议能用 tuple 代替 list 就尽量用 tuple 。'''

#元组的创建
tuple1=('两点水','twowter','liangdianshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456
#创建空元组
tuple3=()
# 元组中只包含一个元素时，需要在元素后面添加逗号
# 如果不加逗号，创建出来的就不是 元组（tuple），而是指 123 这个数了。
tuple4=(123,)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)



#元组的访问
print(tuple1[1])
#元组拼接
list = [111,222]
tuple0 = ('kk','jj','ll',list)
print(tuple0)
print(tuple0[3][0])

#删除元组   tuple 元组中的元素值是不允许删除的，但我们可以使用 del 语句来删除整个元组
# del tuple1
# print(tuple1)

#元组的内置函数
print(len(tuple0))
#返回元组的最大值
tuple5 = (1,2,3,4,5)
print(max(tuple5))
#返回最小值
print(min(tuple5))
#将列表转换为元组
list = [1,2,3,4,5,6,7,8]
print(tuple(list))