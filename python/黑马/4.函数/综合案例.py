#银行存取款以及查询余额操作
money = 50000
name = None
name = input("请输入用户名:")
def qurey(show_head):
    if show_head:
        print(f"{name}，您好，您的余额剩余：{money}元")


def saveing(num):
    global money
    money += num
    print(f"{name}，您好，您存款{num}元成功。")

def get_money(num):
    global money
    money -= num
    print(f"{name}，您好，您取款{num}元成功。")

def main():
    print("-------------主菜单------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")    # 通过\t制表符对齐输出
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

while True:
    key_input = main()
    if key_input == '1':
        qurey(True)
        continue
    if key_input == '2':
        num = int(input("您想要存多少钱？请输入："))
        money += num
        continue
    if key_input == '3':
        num = int(input("您想要取多少钱？请输入："))
        money -= num
        continue
    else:
        print("退出程序")
        break
