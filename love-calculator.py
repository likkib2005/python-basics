name_1=input("enter his name:")
name_2=input("enter her name:")
combine_string=name_1+name_2
lower_case_string=combine_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
print(love_score)
if love_score<10 or love_score>90:
    print(f"your love score is {love_score} and your are nice couple")
elif love_score>=40 or love_score>=50:
     print(f"your love score is {love_score} and your are cute couple")
else:
     print(f"your love score is {love_score} and your are sweet couple")
