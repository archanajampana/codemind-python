n=input()
words_list=n.split()
l=[]
for i in words_list:
    x=max(i)
    y=min(i)
    l.append(y)
    l.append(x)
print(*l)
    