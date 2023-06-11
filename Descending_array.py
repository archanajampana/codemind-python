n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
r=k[::-1]
if(r==l):
    print("yes")
else:
    print("no")