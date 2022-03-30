class Employee:
    count =0
    def _init_(self,name,des,salary):
        self.name =name 
        self.des =des
        self.salary=salary
        Employee.count =Employee.count+1

    def displaycount (self):
          print("The number of Employee in the organigation are :", self.count)


    def displayEmp(self):
         print ("The name of Employee is:",self.name )
         print("Desination of employee :",self.des)
         print("salary of Employee: ",self.salary)

e1= Employee ( "Mahesh","Manager",250000)
e2= Employee ("Rahul","Team leader",300000)

e1.displaycount() 

print("Employee ditails is:")

e1.displayEmp()   
e2.displayEmp()   
