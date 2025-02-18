def while_func():
    list = ["传智教育", "黑马程序员", "Python"]
    index = 0
    while index < len(list):
        num = list[index]
        print(f"列表的元素:{num}")
        index += 1

while_func()


def for_func():
    list = [1,2,3,4,5]
    for i in list:
        print(f"list的元素有：{i}")
       

for_func()