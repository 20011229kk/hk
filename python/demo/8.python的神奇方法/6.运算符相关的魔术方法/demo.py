class Number(object):
    def __init__(self, value):
        self.value = value

    '''等于'''
    def __eq__(self, ohther):
        return self.value == ohther.value
    '''不等于'''
    def __ne__(self, ohther):
        return self.value != ohther.value
    '''小于'''
    def __lt__(self, ohther):
        return self.value < ohther.value
    '''大于'''
    def __gt__(self, ohther):
        return self.value > ohther.value
    '''小于等于'''
    def __le__(self, ohther):
        return self.value <= ohther.value
    '''大于等于'''
    def __ge__(self, ohther):
        return self.value >= ohther.value
    
if __name__ == '__main__':
    x = Number(5)
    y = Number(7)
    print(x == y)
    print(x != y)
    print(x < y)
    print(x > y)
    print(x <= y)
    print(x >= y)