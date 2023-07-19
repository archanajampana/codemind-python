#level 34
n=input()
l=n.lower()
s=l.split()
k="".join(s)
a=[]
for i in k:
    if i not in a :
        a.append(i)
        
print(len(a))