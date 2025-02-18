#1.反向迭代
list1 = [1,2,3,4,5]
for num in reversed(list1):
    print(num,end=' ')
print('\n')



# -*- coding: UTF-8 -*-

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
    	# Forward iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
    	# Reverse iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr,end=' ')
print('\n')
for rr in Countdown(30):
    print(rr,end=' ')
print('\n')