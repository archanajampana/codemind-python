n=input()
k=[]
for i in n:
    if i in "aeiouAEIOU":
        if i in k:
            pass
        else:
            k.append(i)
if k==0:
    print(-1)
else:
    print(*k)
        