n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    k.append(len(str(i)))
for j in k:
    if j%2==0:
        c+=1
print(c)
    