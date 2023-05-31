n=int(input())
c=n
rev=0
while(c>0):
    r=c%10
    c=c//10
    rev=rev*10+r
   
if rev==n:
    print("True")
else:
    print("False")