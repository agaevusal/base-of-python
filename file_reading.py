with open('dataset_24465_4.txt') as f, open('new.txt','w') as w:
    lst = []
    for line in f:
        line = line.splitlines()
        lst.extend(line)
    lst = lst[::-1]
    print(lst)
    content = '\n'.join(lst)
    print(content)
    for i in content:
        w.write(i)