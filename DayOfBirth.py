from datetime import datetime
date = int(input("Enter date : "))
m = int(input("Enter month : "))
y = int(input("Enter year : "))
x = datetime(y, m, date)
d = x.strftime("%A")
print("The Day of Birth is", d)


# from datetime import datetime 
# date = int ( input ("Enter date :"))
# month= int(input("Enter month :"))
# y = int (input("Enter year:"))
# x = datetime(y,month,date)
# d = x.strftime("%M")
# print("The day of birth is ",d )

# from datetime import datetime
# date = int (input("Enter date :"))
# month = int(input( "Enter month :"))
# year  = int( input("Enter year :"))
# x = datetime(date,month,year)
# d = x.strftime("%A")
# print ("The day of birth  is ", d)