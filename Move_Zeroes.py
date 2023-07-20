n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0:
        l.remove(0)
        l.append(0)
print(*l)