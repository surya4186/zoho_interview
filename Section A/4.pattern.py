N=int(input("Enter the number: "))
M=2*N-1
lowest=0
highest=M-1
value=N
matrix=[[0 for i in range(M)]for j in range(M)]
for i in range(N):
    for j in range(lowest,highest+1):
        matrix[i][j]=value
    for j in range(lowest+1,highest+1):
        matrix[j][i]=value
    for j in range(lowest+1,highest+1):
        matrix[highest][j]=value
    for j in range(lowest+1,highest):
        matrix[j][highest]=value
    
    lowest=lowest+1
    highest=highest-1
    value=value-1
for i in range(M):
    for j in range(M):
        print(matrix[i][j],end=" ")
    print()