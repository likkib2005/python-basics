height=int(input("Enter your height:"))
if(height>3):
    print("You can ride")
    age=int(input("enter your age:"))
    if(age<=18):
         print("pay 250 rupees")
    else:
        print("pay 500 rupees")
else:
    print("you cannot ride")
print("Bye")