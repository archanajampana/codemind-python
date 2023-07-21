n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(n):
    if l[i]%2==0:
        s.append(l[i])
        if i%2==0:
            c+=1
if len(s)==c:
    print("True")
else:
    print("False")
        