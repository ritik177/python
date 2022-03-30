# Python Program to stop special character entry
try:
    str = input("Please Enter Your name : ")
    for ch in str:
        if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            print(ch,end="")
        else:
            raise Exception
            break
except:
    print()
    print("invalid entry")

