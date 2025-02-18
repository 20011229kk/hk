'''迭代器有两个基本的方法：iter() 和 next(),且字符串，列表或元组对象
都可用于创建迭代器，迭代器对象可以使用常规 for 语句进行遍历，也可以使用 next() 函数来遍历。'''
#1，字符串创建迭代对象
str1 = 'kjllxh'
iter1 = iter(str1)
#2.list对象创建迭代器
list1 = [1,2,3,4,5]
iter2 = iter(list1)
#3.元组创建迭代器
tuple1 = (1,2,3,4,5)
iter3 = iter(tuple1)

#for循环遍历迭代器对象
for x in iter1:
    print(x,end=' ')
print('\n----------------')

#next函数迭代
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break
    