a=input("ENTER A STRING :")
b=a[0]
result=b
for i in a[1:]:
    if (i==b):
        i="$"
        result+=i
    else:
        result+=i
print(result)