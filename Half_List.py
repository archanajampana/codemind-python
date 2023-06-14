n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
x=len(l)
n=len(l)//2
for i in range(n):
    k.append(l[i])
for j in range(n,x):
    p.append(l[j])
    y=p[::-1]
z=y+k
print(*z)