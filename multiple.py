height=int(input("what is your height?"))
bill=0
if(height>=3):
    print("you can ride")
    age=int(input("enter your age:"))
    if(age<15):
        print("pay 250 rupees")
        bill=250
    elif(age>=20):
        print("pay 300 rupees")
        bill=300
    elif(age>=50):
        print("pay 450 rupees")
        bill=450
    else:
        print("pay 500 rupees")
        bill=500
    want_photo=input("Do you want to take photo?(y/n)")
    if want_photo=="Y" or want_photo=="y":
        bill+=50
        print(f"Total bill is {bill}")   
        
else:
    print("you can't ride")
