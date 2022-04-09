def difference(s):
    l=len(s)                                       #length of the string
    n=l//2
    list1=[]                                        
    list2=[]
    for i in range(n):                                 
        st=ord(s[i+1])-ord(s[i])                #first string character ascii value -second character ascci value
        list1.append(st)                           #add Subtract the value in list              
    for j in range(n,0,-1):
        st1=ord(s[j])-ord(s[j-1])
        list2.append(st1)
        
    if list1==list2:                             # check  list1 == list2 
        print("equal difference")
    else:
        print("unequal difference")

s=input("Enter the string :")                       #input the string
difference(s)                                                