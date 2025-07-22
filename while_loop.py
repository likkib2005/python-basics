count=1
while count<=5:
    print(count)
    count+=1
list1=[12,34,56,78,90]
while list1:
    print("Hi Likki")
    list1.pop()
count=1
while count<=5:
    print(count)
    count+=1 
else:
    print("in else block")
print("out from block")
count=1
while count<=5:
    print(count)
    count+=1
    if count==3:
        break
else:
    print("in else block")
print("out from block")
number=int(input("enter a number(12 to quit)"))
while number!=12:
    print(number)
    number=("enter a number to quit")
else:
    print("in else block")
total=0
number=int(input("enter a number(0 to quit)"))
while number!=-1:
    total+=number