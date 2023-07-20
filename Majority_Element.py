n=int(input())
l=list(map(int,input().split()))
a=n//2
k=[]
for i in l:
    if l.count(i)>a:
        print(i)
        break