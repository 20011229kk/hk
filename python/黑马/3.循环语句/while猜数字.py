import random
num = random.randint(1,100)
count = 0
# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True

while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")
print(f"你总共猜测了{count}次")
