n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    x=abs(i)
    y=len(str(x))
    k.append(y)
print(*k)
    