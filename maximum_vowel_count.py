n=input()
word_list=n.split()
vowels="aeiouAEIOU"
l=[]
for i in word_list:
    vowel_count=0
    for j in i:
        if j in vowels:
            vowel_count+=1
            l.append(vowel_count)
print(max(set(l)))
            