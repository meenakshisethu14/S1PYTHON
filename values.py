num=input("ENTER THE LIST OF INTEGERS :")
num1=num.split(",")
list=[]
for i in num1:
    i=int(i)
    if(i>100):
        list.append("over")
    else:
        list.append(i)
print(list)