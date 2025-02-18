import random
num = random.randint(1,10)

guess_num = int(input("输入你要猜测的数字："))
if guess_num == num:
    print("恭喜你，第一次就猜中了！")
elif guess_num > num:
    print("猜大了")
else:
    print("猜小了")

guess_num = int(input("再次输入你要猜测的数字："))
if guess_num == num:
    print("恭喜你，第二次就猜中了！")
elif guess_num > num:
    print("猜大了")
else:
    print("猜小了")

guess_num = int(input("第三次输入你要猜测的数字："))
if guess_num == num:
    print("恭喜你，第三次就猜中了！")
else:
    print("机会用完了")
