class multifilter:
    def judge_half(self, pos, neg):
        if pos >= neg:
            return True
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
    def judge_any(self, pos, neg):
        if pos >= 1:
            return True
            # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(self, pos, neg):
        if neg == 0:
            return True
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge = judge_any):
        self.filtred = set()
        self.judge = judge
        for x in iterable:
            pos = 0
            neg = 0
            for f in funcs:
                if f(x) is True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(self,pos, neg) is True:
                self.filtred.add(x)

    def __iter__(self):
        for i in self.filtred:
            yield i
def mul2(x):
    return x % 2 == 0
def mul3(x):
    return x % 3 == 0
def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))