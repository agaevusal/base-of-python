class Myclass:

    def judge_half(self,pos,neg):
        if pos >= neg:
            return True

    def __init__(self, iterable, *funcs,judge = judge_half):
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
            if self.judge_half(pos, neg) is True:
                self.filtred.add(x)

    def __iter__(self):
        for i in self.filtred:
            yield i

def f_2(x):
    return x % 3 == 0
def f_3(x):
    return x % 5 == 0
iterable = [i for i in range(13)]

print(list(Myclass(iterable,f_2,f_3,judge=Myclass.judge_half)))
