a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
common=list(set(l1).intersection(l2))

print(len(common))