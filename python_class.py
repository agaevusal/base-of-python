class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)


        # операция сложения

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)
        # операция вычитания

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)
        pass
        # операция умножения

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)
        # операция целочисленного деления
a = ExtendedStack()

