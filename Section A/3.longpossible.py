n=int(input("enter the number of the string :"))
list1=[]
for i in range(n):
    list1.append(input("Enter the string : "))      #adding the element in list
    
for j in range(n):
    string="".join(sorted(list1[j]))              #using join() + sorted()
    print("string",j+1,":",string[::-1])        #print string