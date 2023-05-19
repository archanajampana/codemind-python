n=int(input())
l=list(map(int,input().split()))
s=0
t=0
for i in range(n):
    if i%2==0:
        s+=l[i]
    else:
        t+=l[i]
print("%d"%(s-t))
        