n = int(input())
d = {}
d_1 = {}
lst_1 = []
lst_2 = []
for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'add':
        lst_1.append(arg)
        d[namespace] = lst_1
    elif cmd == 'create':
        lst_1 = []
        d[namespace] = []
    elif cmd == 'get':
        for key, value in d.items():
            if arg in value:
                lst_2.append(key)
        if len(lst_2) != 0:
            print(lst_2[len(lst_2) - 1])
        else:
            print(None)

        lst_2 = []

print(d)








