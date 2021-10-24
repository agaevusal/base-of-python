class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        self.k = len(self.lst) - 1

    def __next__(self):
        while True:
            if self.i <= self.k:
                if self.lst[self.i] % 2 != 0:
                    self.i += 1
                    return self.lst[self.i - 1]
                else:
                    self.i += 1
                    return 'not even'
        else:
            return 'the end!'


    def __iter__(self):
        return self

x = MyIterator([1,2,3,4,5])
for i in x:
    print(i)
