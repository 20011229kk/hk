# 我们学习了列表（List） 和 元组（tuple） 来表示有序集合。
# 而我们在讲列表（list）的时候，我们用了列表（list） 来存储用户的姓名。
name = ['一点水', '两点水', '三点水', '四点水', '五点水']
# 那么如果我们为了方便联系这些童鞋，要把电话号码也添加进去，该怎么做呢？

# 用 list 可以这样子解决：
name = [['一点水', '131456780001'], ['两点水', '131456780002'], ['三点水', '131456780003']]
# 但是这样很不方便，我们把电话号码记录下来，就是为了有什么事能及时联系上这些童鞋。
# 如果用列表来存储这些，列表越长，我们查找起来耗时就越长。
# 这时候就可以用 dict （字典）来表示了，Python 内置了 字典（dict），dict 全称 dictionary，
# 如果学过 Java ，字典就相当于 JAVA 中的 map，使用键-值（key-value）存储，具有极快的查找速度。
name = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003'}


# 1.字典的创建
dict1 = {'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
dict2={'abc':1234,1234:'abc'}
print(dict1)
print(dict2)
#访问dict  既是通过key查找value
print(dict1['liangdianshui'])


#2.修改dict
# 新增一个键值对
dict1['jack'] = '44444'
print(dict1)
#修改dict
dict1['liangdianshui'] = '000'
print(dict1)

# 3.删除dict
# 通过 del 可以删除 dict （字典）中的某个元素，也能删除 dict （字典）
# 通过调用 clear() 方法可以清除字典中的所有元素
# del dict1['jack']
# print(dict1)

# dict1.clear()
# print(dict1)

# del dict1
# print(dict1)


print("=========================================")
#注意事项
# dict （字典）是不允许一个键创建两次的，但是在创建 dict （字典）的时候如果出现了一个键值赋予了两次，会以最后一次赋予的值为准
dict3 = {'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333','twowater':'444444'}
print(dict3)
print(dict3['twowater'])

#dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
# dict4={'liangdianshui':'111111' ,123:'222222' ,[923,'tom']:'333333','twowater':'444444'}
# print(dict4)


'''和 list 比较，dict 有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢
需要占用大量的内存，内存浪费多
而list相反：
查找和插入的时间随着元素的增加而增加
占用空间小，浪费内存很少'''

print("------------------------------")
#dict的字典和方法
dict4={'liangdianshui':'111111' ,123:'222222' ,(23,'tom'):'333333','twowater':'444444'}
print(len(dict4))
#输出字典可打印的字符串表示
print(str(dict4))
#赋值
dict5 = dict4.copy()
print(dict5)
#以列表返回字典中的所有值
print(dict4.values())
#随机返回并删除字典中的一对键和值
print(dict4.popitem())
#以列表返回可遍历的(键, 值) 元组数组
print(dict4.items())