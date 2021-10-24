class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
    def can_add(self, v):
        if (self.capacity - self.current) // v > 0:
            return True
        return False
        # True, if we can add v coins, otherwise False
    def add(self, v):
        self.current += v
        print(self.current)
        #  add v coins to money
print('enter capacity: ', end = '')
a = MoneyBox(int(input()))
while True:
    print('enter coin: ',end='')
    v = int(input())
    if a.can_add(v) is True:
        a.add(v)
    else:
        print('Moneybox is filled')
        break
