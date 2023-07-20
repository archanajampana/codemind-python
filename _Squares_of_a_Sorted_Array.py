n=int(input())
l=list(map(int,input().split()))
p=[]
l.sort()
for i in l:
    k=i**2
    p.append(k)
p.sort()
print(*p)
    