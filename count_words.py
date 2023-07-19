n=input()
c=0
words_list=n.split()
for i in words_list:
    
   
    
    if i[0] in "aeiouAEIOU" and i[-1] not in "aeiouAEIOU":
        
        c+=1
print(c)
         
    
   
       