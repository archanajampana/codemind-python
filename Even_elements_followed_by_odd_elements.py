n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        p.append(i)
a=k+p
print(*a)
        