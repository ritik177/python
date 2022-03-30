l={'welcome to my page '}
with open("abc.txt",'w+') as f:
    for item in lra :
        f.write('%s\n' %item)
        print("File written successfully")

        f.close()