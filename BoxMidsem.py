class Box:
    def __init__(self, *side):
        self.side = side


class Cube(Box):

    def display(self):
        x = self.side[0]
        print("The volume of Cube is : {}".format(x*x*x))


obj1 = Cube(8)
obj1.display()
