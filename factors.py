def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input("enter a number"))
x=fact(n)
print(x)