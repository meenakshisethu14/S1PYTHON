a=input("ENTER A STRING :")
b=a[0]
c=a[-1]
result=c
for i in a[1:-1]:
    result+=i
result+=b
print(result)