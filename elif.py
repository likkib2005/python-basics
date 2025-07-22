height=int(input("enter your height:"))
if(height>=3):
    print("you can ride")
    age=int(input("enter your age:"))
    if(age<=5):
        print("pay 50 rupees")
    elif(age<=10):
        print("pay 100 rupees")
    elif(age<=15):
        print("pay 150 rupees")
    elif(age<=20):
        print("pay 200 rupess")
    else:
        print("pay 250 rupees")
else:
    print("bye")