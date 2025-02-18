'''python 的 set 和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
set 和 dict 类似，但是 set 不存储 value 值的。'''

# 1.set的创建
set1 = set([123,456,789])
print(set1)
# 在 dict （字典） 中创建时，有重复的 key ，会被后面的 key-value 值覆盖的，而 重复元素在 set 中自动被过滤的。
set2 = set([123,456,789,123,123])
print(set2)

# 2.set添加元素，可以重复添加 但是没有效果
set2.add(111)
print(set2)

#3.删除元素
set2.remove(123)
print(set2)
