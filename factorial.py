def Fact(n):
    if n == 0 or n == 1 :
        return 1
    return Fact(n-1)*n

print(Fact(5))