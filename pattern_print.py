n=5
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(n,end=" ")
    for s in range(i+1,n):
        print(n,end=" ")
    print(" ")