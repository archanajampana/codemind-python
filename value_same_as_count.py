n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    x=l.count(i)
    if x==i:
        if i in s:
            pass
        else:
            s.append(i)
print(len(s))
     
        
    
        