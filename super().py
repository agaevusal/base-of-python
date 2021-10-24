class myclass_1:
    def check_even(self,x):
        return x % 2 == 0

class myclass_2(list,myclass_1):
    def append(self,arg):
        super(myclass_2,self).append(arg) #it is correct too
        list.append(self,arg) #it is correct too
        super().append(arg)  #it is correct too
        x = list()
        print(self)


a = myclass_2([1,2,3])
a.append(4)
