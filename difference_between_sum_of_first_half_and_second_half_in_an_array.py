n=int(input())
l=list(map(int,input().split()))
x=len(l)
s=0
r=0
k=[]
p=[]
a=x//2
for i in range(a+1,x+1):
    k.append(i)
    s=sum(k)
for j in range(1,a+1):
    p.append(j)
    r=sum(p)
print(s-r)