class A:
    i=0
    def _init_(self):
        self.change()
    @classmethod
    def change(cls):
        cls.i+=1
obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()
print(f"the number of object created are",{A.i})