n=int(input())
l=list(map(int,input().split()))
s=set(l)
k=[]
for i in s:
    if i%2==0:
        k.append(i)
print(sum(k))