n=int(input())
l=list(map(int,input().split()))
a=list(set(l))
a.sort()
for i in a:
    if len(a)>=3:
        print(a[-3])
        break
    else:
        print(a[-1])
        break
        
    
