def even(n):
        if n%2==0:
            return True
        else:
            return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    x=even(i)
    if x==True:
        c+=1
if c==len(l):
    print("True")
else:
    print("False")