n=int(input())
l=list(map(int,input().split()))
x=sum(l)
a=x//n
k=[]
for i in l:
    if i<=a:
        k.append(i)
print(len(k))
