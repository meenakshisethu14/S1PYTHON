li1=input("enter the first list")
li2=input("enter the second list")
x=len(li1)
y=len(li2)
if x==y:
    print("The list are of same length")
else:
    print("not same")
s1=0
s2=0
for i in li1:
    i=int(i)
    s1+=i
for j in li2:
    j=int(j)
    s2+=j
if s1==s2:
    print("The sum of both list are same",s1)
else:
    print(f"The sum of both list {s1},{s2} are different")
for i in li1:
    for j in li2:
        if i==j:
            print(f"the element {i} occur in both list")
        else:
            print("There are no common elements in the list")
