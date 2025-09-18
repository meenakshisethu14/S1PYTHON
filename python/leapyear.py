current_year=int(input("ENTER THE CURRENT YEAR :"))
finalyear=int(input("ENTER FINAL YEAR"))
for x in range (current_year,finalyear+1):
    if(x % 4==0 and x % 100 !=0)or(x % 400 == 0):
        print(x)