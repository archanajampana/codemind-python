a=input()
b=input()
for i in a:
    if b in a:
        print("True")
        print(a.index(b))
        break
    else:
        print("False")
        break
