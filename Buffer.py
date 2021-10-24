class Buffer:
    def __init__(self):
        self.lst_2 = []
        # конструктор без аргументов

    def add(self, *a):
        lst_1 = []
        print('enter size of list: ', end='')
        n = int(input())
        for i in range(n):
            print('enter element of list: ', end='')
            lst_1.append(int(input()))
        self.lst_2.extend(lst_1)
        print(self.lst_2)
        k = len(self.lst_2) // 5
        if k >= 1:
            for i in range(k):
                m = sum(self.lst_2[0:5])
                del self.lst_2[0:5]
                print(m)
    # добавить следующую часть последовательности

    def get_current_part(self):
        print(self.lst_2)
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
buf = Buffer()
buf.add()
buf.get_current_part()