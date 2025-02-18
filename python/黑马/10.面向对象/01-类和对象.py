class Clock:
    id = None
    price = None


    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

#构建两个闹钟对象 并让其工作
clock1 = Clock()
clock1.id = 1
clock1.price = 99.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()