n=int(input())
l=list(map(int,input().split()))
s=sum(l)
x=s//n
k=[]
for i in l:
    if i>=x:
        k.append(i)
print(len(k))
    