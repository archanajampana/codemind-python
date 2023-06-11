n=int(input())
l=list(map(int,input().split()))
for i in l:
    r=int(str(i)[::-1])
    print(r,end=" ")