n=int(input())
rev=0
sign=1
if n<0:
    sign=-1
    n=-1*n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("%d"%(sign*rev))