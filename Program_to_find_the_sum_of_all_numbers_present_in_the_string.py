n=input()
s=0
for i in n:
    if i.isdigit()==True:
        x=int(i)
        s=s+x
print(s)