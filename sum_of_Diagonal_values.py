n,m=map(int,input().split())
n1=[]
for i in range(n):
    l=list(map(int,input().split()))
    n1.append(l)
s1=0
s2=0
for i in range(len(n1)):
    for j in range(len(n1)):
        if i==j:
            s1=s1+n1[i][j]
        elif i==len(n1)-j-1:
            s2=s2+n1[i][j]
print(s2+s1)