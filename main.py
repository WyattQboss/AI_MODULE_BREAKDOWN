import csv

f = open('test.csv','w', newline="")
tup1 = ("test text", 25)
tup2 = ("car payment", 8000)
writer = csv.writer(f)
writer.writerow(tup1)
writer.writerow(tup2)
f.close()
two_D_array = [["dsfds","adsf"],["fadsfa","adsfdas"]]

f = open('test.csv','r')
Lines = f.readlines()
for i in Lines:
    print(i)
    two_D_array.append(i)

print(Lines)

print(two_D_array)





'''
R_Expenses = [9,8,5,7,1,2,3,4,5,6,7,6,5,4,5,6,7,6,5,4,3,4,5,6,7,5,555,56,6,5,4,3,3,5,6,7]

user_input = input("please update your repeating expenses")

for change in R_Expenses:
    R_Expenses.append(user_input)
print (R_Expenses)
'''