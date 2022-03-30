import os 
os.mkdir("abc")
try:
    if os.path.exists("xyz.txt"):
        f =open("xyz.txt",a)
        f.write("hello world")

    else:
        f =open("xyz.txt",a)
        f.write("hello world")
except:    
      print ("Exception")