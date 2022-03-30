class vehicle:
  def insert(self,name,company):
    self.name=name
    self.company=company
  def display(self):
    print("name:"+self.name,"\ncompany:"+self.company)
class car(vehicle):
  def insert(self,name,company,model):
    super().insert(name,company)
    self.model=model
  def display(self):
    super().display()
    print("model:"+self.model,"\n")
class bike(vehicle):
  def insert(self,name,company,colour):
    super().insert(name,company)
    self.colour = colour
  def display(self):
    super().display()
    print("colour:"+self.colour)

ob=car()
ob.insert("Q7","2020","BMW")
ob.insert("Honda City","ZX","Honda")
ob.display()

ob1=bike()
ob1.insert("Apache","2017","white")
ob1.insert("ZX-10R","2020","NINJA")
ob1.display()