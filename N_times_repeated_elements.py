n=int(input())
l=list(map(int,input().split()))
a=int(input())
s=[]
for i in l:
    x=l.count(i)
    if x==a:
        if i in s:
            pass
        else:
            s.append(i)
if len(s)==0:
    print(-1)
else:
    print(*s)
    