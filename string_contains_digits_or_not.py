n=int(input())
for i in range(n):
    a=input()
    c=0
    for j in a:
        if j.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")