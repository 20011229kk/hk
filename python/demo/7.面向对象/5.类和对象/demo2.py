#如果类属性变了，实例属性会不会跟着变化？
class ClassA(object):
    var1 = 'kk'

    def fun1(self):
        print('var1的值是'+self.var1)

a = ClassA()
print(a.var1)

ClassA.var1 = 'hh'
print(a.var1)
#从程序来看，值变了 这很好理解，因为我们的实例对象就是根据类来复制出来的，类属性改变了，实例对象的属性也会跟着改变。
#如果反过来 是改变实例属性的值，类属性的值会跟着变化嘛

class ClassB(object):
    var2 = 'kjl'

    def fun2(self):
        print('var2的值是'+self.var2)

b = ClassB()
print(b.var2)

b.var2 = 'lxh'
print(b.var2)

print(ClassB.var2)

#显而易见，改变实例属性是不会影响类属性的变化的