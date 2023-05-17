n=int(input())
s=0
p=1
while(n):
    x=n%10
    s+=x
    p*=x
    n=n//10
if s==p:
    print("Spy Number");
else:
    print("Not Spy Number");