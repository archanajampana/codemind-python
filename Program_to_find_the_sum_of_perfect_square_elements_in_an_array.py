import math
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if math.sqrt(i).is_integer():
        k.append(i)
print(sum(k))
        