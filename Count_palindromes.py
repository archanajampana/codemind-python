n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    r=int(str(i)[::-1])
    if r==i:
        c+=1
print(c)