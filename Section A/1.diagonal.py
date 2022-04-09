string=input("enter the string :")
if len(string)%2==0:
    print("Not Possible")
else:
    N=len(string)
    i=N//2
    k=N//2
    cnt=-1
    while i>=0 and k<N:
        j=0
        while j<i:
            print(" ",end="  ")
            j+=1
        print(string[i],end='  ')
        while j<k-1:
            print(" ",end='  ')
            j+=1
        if k!=i:
            print(string[k],end='  ')
        k+=1
        i-=1
        print()
    i=1
    k=N-2
    while i<=N//2 and k>=N//2:
        j=0
        while j<i:
            print(' ',end= '  ')
            j+=1
        print(string[i],end='  ')
        while j<k-1:
            print(' ',end="  ")
            j+=1
        if i!=k:
            print(string[k],end='  ')
        i+=1
        k-=1
        print()
