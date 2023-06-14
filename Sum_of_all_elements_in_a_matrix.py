r,c=map(int,input().split())
m=[]
s=0
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for j in m:
    for k in j:
        s+=k
print(s)
        