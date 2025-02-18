#类的定义
class Student():
    name = 'kk',
    age = 18,
    sex = '男'

    def fun1():
        print('我是 fun1')

    def fun2():
        print('我是 fun1')

    def fun3():
        print('我是 fun1')
    
#类属性和方法的调用
print(Student.name)
print(Student.age)
print(Student.sex)
Student.fun1()