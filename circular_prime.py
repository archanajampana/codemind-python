def prime(m):
    c=0
    for i in range(1,m+1):
        if (m%i)==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
num=n
rev=0
while(n):
    r=n%10
    rev=(10*rev)+r
    n//=10
if(prime(num)):
    if(prime(rev)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')