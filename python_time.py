import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)
x = LoggableList([1,2,34,5])
x.append(3)