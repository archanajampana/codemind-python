n=int(input())
s=n**2
k=(str(n)[::-1])
h=int(k,10)
x=(h**2)
y=(str(x)[::-1])
p=int(y,10)
if p==s:
    print("True")
else:
    print("False")