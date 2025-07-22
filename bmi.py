weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"your bmi is {bmi} and you have normal weight")
elif bmi<25:
    print(f"yur bmi is {bmi} and you are overweight")
elif bmi<30:
    print(f"your bmi is {bmi} and you are  obesity")
else:
    print(f"you bmi is {bmi} and you are over obese")
    