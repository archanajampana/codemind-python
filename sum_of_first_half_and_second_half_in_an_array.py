n=int(input())
l=list(map(int,input().split()))
x=len(l)
a=x//2
s=0
r=0
k=[]
p=[]
for i in range(1,a+1):
    k.append(i)
print(sum(k))
for j in range(a+1,x+1):
    p.append(j)
print(sum(p))

