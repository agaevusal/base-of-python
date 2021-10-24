s = ''
with open('dataset_3363_3.txt') as text:
    for x in text:
        s += x
    print(s)
lst_1 = s.split()
print(lst_1)
k = 0
d = {}
for i in range(len(lst_1) - 1, -1, -1):
    for j in range(len(lst_1)):
        if lst_1[i].lower() == lst_1[j].lower():
            k += 1
        d[lst_1[i]] = k
    k = 0
print(d)
lst_2 = []
lst_3 = []
for value in d.values():
    lst_2.append(value)
k = max(lst_2)
print(lst_2)
print(k)
for key, value in d.items():
    if value == k:
        lst_3.append(key)
print(lst_3)

lst_4 = []
for i in range(len(lst_3)):
    lst_4.append(lst_3[i].lower())
print(lst_4)
print(min(lst_4), end= ' ')
print(k)