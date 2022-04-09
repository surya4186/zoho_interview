s=input("Enter the string :")         #input the string
s=s.split(" ")                        #split the word in empty space
list1=[]                              #list
for i in range(len(s)):                   #loop range string lenth
    if s[i] not in list1:                  #the if condition string first-last word check list1
        list1.append(s[i])                   #add the string in list
for i in list1:                                
    print(i,end=" ")                            #print the list