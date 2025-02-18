#1，for循环迭代字符串
for char in 'kjllxh':
    print(char , end = ' ')
print('\n')

#迭代list
list1 = [1,2,3,4,5]
for i in list1:
    print(i , end = ' ')
print('\n')

#迭代dict
#迭代key
dict1 = {'name':'kk','age':12,'sex':'男'}
for key in dict1:
    print(key , end= ' ')
print('\n')
#迭代value
for value in dict1.values():
    print(value,end= ' ')
print('\n')

#通过key迭代value
for key,value in dict1.items():
    print(key,value,end=' ')
print('\n')

