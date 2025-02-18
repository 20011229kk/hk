#同时迭代多个序列   使用zip函数
names = ['kk','hh']
ages = [11,12]
for name,age in zip(names,ages):
    print(name,age)

# 利用 zip() 函数，我们还可把一个 key 列表和一个 value 列表生成一个 dict （字典）,如下：
dict1 = dict(zip(names,ages))
print(dict1)

#### 这里提一下， zip() 是可以接受多于两个的序列的参数，不仅仅是两个。