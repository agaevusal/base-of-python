class myclass_1(list):
    def append(self,arg):
        list.append(self,arg)
        print(self)
a = myclass_1([1,2,3])
a.append(4)


