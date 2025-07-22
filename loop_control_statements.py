count=1
while count<=5:
    print(count)
    count+=1
    if count==3:
        break
        print("loop terminated")
print("out from loop")
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("hi")
print("out from loop")
list1=["hi","hello","welcome"]
names=["likki","narasimha","rithik"]
for i in list1:
    for name in names:
        print(i,name)
        if i=="welcome" and name=="likki":
            break
    print("out from inner loop")
print("out from outer loop")
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hi")
print("out from loop")for i in range(1,11):
    if i==6:
        continue
    print(i)
for i in range(0,6):
    def func():
        pass