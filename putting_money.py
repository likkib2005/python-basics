row_1=['🦚','🦚','🦚']
row_2=['🦚','🦚','🦚']
row_3=['🦚','🦚','🦚']
nested_list=[row_1,row_2,row_3]
position=input("enter the position you want to put money:")
row_number=int(position[0])
column_number=int(position[1])
row_selected=nested_list[row_number-1]
row_selected[column_number-1]="Likki"
print(f"{row_1} \n {row_2}\n {row_3}") 
