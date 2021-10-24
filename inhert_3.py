class A:
    def __init__(self):
        val = 0
        self.val = 0
class B(A):
    def add(self, k):
        self.val += k
    def multi(self,k):
        self.add(k)

class C(B):
    def add(self, k):
        self.val+= k
        print(self.val)

x = C()
