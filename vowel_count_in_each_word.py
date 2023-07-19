n=input()
words=n.split()
vowels='aeiouAEIOU'

for i in words:
    vowel_count=0
    for j in i:
        if j in vowels:
            vowel_count+=1
    print(vowel_count,end=" ")
    