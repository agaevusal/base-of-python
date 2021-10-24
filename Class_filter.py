class Filter:
    def __init__(self, lst, *funcs):
        pass

    def judge(self):
        if False not in self.lst_2:
            return 'ok'
        else:
            return 'not ok'

def f_2(x):
    if x % 2 == 0:
        return True
    else:
        return False

def f_3(x):
    if x % 3 == 0:
        return True
    else:
        return False


lst = [i for i in range(5)]


