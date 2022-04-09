n=int(input())

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n,i,-1):
        if i-j==0:
            print(i+1,end=" ")
        
    print()
        