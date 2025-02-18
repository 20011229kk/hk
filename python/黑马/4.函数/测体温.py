def check(num):
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if num < 37.5:
        print("体温正常，请进入")
    else:
        print("体温不正常，请出去")

check(38)