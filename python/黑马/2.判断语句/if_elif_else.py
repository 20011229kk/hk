tall = int(input("请输入你的身高"))
vip = int(input("请输入你的VIP等级（1-5）："))
date = int(input("请告诉我今天几号："))
if tall < 120:
    print("身高小于120cm，可以免费。")
elif vip > 3:
    print("vip级别大于3，可以免费。")
elif date == 1:
    print("今天是1号免费日，可以免费")
else:
     print("不好意思，条件都不满足，需要买票10元。")