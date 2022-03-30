s = input("Enter your string :")
n = ['0','1','2','3','4','5','6','7','8','9']
l = ''
for i in range ( 0, len(s)):
    if s[i] not in n:
        l  += s[i]ll

print("String without number :"+l)