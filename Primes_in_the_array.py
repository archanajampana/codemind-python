def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return -1

n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    x=is_prime(i)
    if x==1:
        s+=1
print(s)
    

    