import random
a=random.randint(1,3)
print(a)
b=random.randrange(1,3)
print(b)
a=random.random()
print(a)
l=[2,4,5,90,-5,12,3454]
a=random.choice(l)
print(a)
import random
a=random.uniform(1,3)
print(a)
import random
l=[34,65,43,21,34,43]
random.shuffle(l)
print(l)
import random
side=random.randint(0,1)
if side==0:
    print("tails")
else:
    print("head")