# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__
class Student:
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("纠结伦","33","2221112211")
print(f"我的名字叫{stu.name},今年{stu.age}岁,电话号码是{stu.tel}")