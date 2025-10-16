n=int(input("enter the limit :"))
names=[]
count=0
for x in range (n):
    x=input("enter a name")
    names.append(x)
for i in names:
    for j in i:
        if"a"in j.lower():
            count+=1

print("The occurence of a is",count)