n=int(input())
s=0
t=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2==0:
        s+=l[i]
    else:
        t+=l[i]
print("%d"%abs(t-s))
        