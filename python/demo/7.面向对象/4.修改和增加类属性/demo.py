class Stu():
    var1 = 'kk'

    @classmethod
    def test(cls):
        print('原来的val1值为：'+cls.var1)
        cls.var1 = input('请输入修改后的值')
        print('修改后的值为：'+cls.var1)
        cls.var2 = input('新增的属性var2，请为他赋值')
        print('修改后的var2值为'+cls.var2)

Stu.test()

