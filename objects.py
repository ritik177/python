class A:
    count = 0
    def _init_(self):
        A.count+=1
    def show (self):
        print(self.count)


a = A()
b = A()
c = A()
a.show()