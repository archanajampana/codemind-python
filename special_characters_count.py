n=input()
c=0
for i in n:
    if not i.isalnum() and not i.isspace():
        c+=1
print(c)