def pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print()
n=int (input("enter a number :"))
print(pyramid(n))