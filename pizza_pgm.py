size=input("what size pizza do you want(s/m/l)?")
bill=0
if size=="S" or size=="s":
    print("small pizza is 100 rupees")
    bill+=100
elif size=="M" or size=="m":
    print("medimum pizza is 250 rupees")
    bill+=200
else:
    print("large pizza is 300 rupees")
    bill+=300
add_pepporni=input("Do you want pepporni(y/n)?")
if add_pepporni=="Y" or add_pepporni=="y":
    if size=="S" or size=="s":
        bill+=30
        print(f"your total bill is {bill}")
    elif size=="M" or size=="m":
        bill+=50
        print(f"your total bill is {bill}")
    else :
        bill+=70
        print(f"your total bill is {bill}")
extra_cheese=input("Do you want extra cheese?(Y/N)")
if extra_cheese=="Y" or extra_cheese=="y":
    bill+=20
print(f"your total bill is {bill}")
print("Thank You!visit again......")

    