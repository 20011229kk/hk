# List列表
name1 = "肖炎"
name2 = "海波东"
name3 =  "熊战"

name = ["肖炎","海波东","熊战"]
print(name1)
print(name2)
print(name3)
print(name)


# 访问list列表中的值
name = ['一点水', '两点水', '三点水', '四点水', '五点水']
print(name)
# 通过索引来访问列表
print(name[2])
# 通过方括号的形式来截取列表中的数据
print(name[1:2])
#通过索引对list进行更新和修改
name[1] = '2点水'
print(name)
#使append对列表进行添加
name.append('六点水')
print(name)
#del删除元素
del name[5]
print(name)



#list运算符
#len计算元素个数
print(len([1,2,3]))
print([1,2,3]+[4,5,6])
print(['HI']*4)
print(3 in [1,2,3])


print("===================================")
#list函数方法
number = [1,2,3,4,5,6]
print(len(number))
print(max(number))
print(min(number))
# 将元组转换为列表
print(list(number))
number.append(7)
print(number)

# 统计某个元素在列表中出现的次数
print(number.count(1))

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
number.extend([8,9,10])
print(number)

# 从列表中找出某个值第一个匹配项的索引位置
print(number.index(1))

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(number.pop())
print(number)
# 移除列表中的一个元素（参数是列表中元素），并且不返回任何值
number.remove(9)
print(number)

# 反向列表中元素
number.reverse()
print(number)

# 对原列表进行排序
number1 = [2,1,4,3,6,5]
number1.sort()
print(number1)