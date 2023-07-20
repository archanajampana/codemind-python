a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    y=abs(i)
    if len(str(y))==b:
        c+=1
print(c)
    