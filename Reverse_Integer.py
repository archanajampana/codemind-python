n=int(input())
sign=1
rev=0
if n<0:
    sign=-1
    n=n*-1
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("%d"%(sign*rev))
    