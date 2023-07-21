n=int(input())
a=0
b=1
count=2

if n==1:
    print(a,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    while count<n:
        c=a+b
        print(c,end=" ")
        count+=1
        a=b
        b=c
    