# Python data type : 1)Numeric 2)String 3)List 4)Tuple 5)dictionary
c = 100 + 3j
print("The type of variable having value", c, " is ", type(c))

a = 100
print("The type of variable having value", a, " is ", type(a))

# List - Array with mix of different datatypes
values = [1, 2, "Rahul", 4, 5]
print(values) #[1, 2, 'Rahul', 4, 5]

print(values[0]) #1

# get the last value in list
print(values[-1])  # 5

#get values between mentioned index
print(values[1:3]) # 2 , Rahul

#insert values in list
values.insert(3,"shetty")
print(values) #[1, 2, 'Rahul', 'shetty', 4, 5]

#insert value at end of list
values.append("ENd")
print(values) # [1, 2, 'Rahul', 'shetty', 4, 5, 'ENd']

#update value in given index in list
values[2]="RAHUL"
print(values) # [1, 2, 'RAHUL', 'shetty', 4, 5, 'ENd']
#delete value in list
del values[0]
print(values) #[2, 'RAHUL', 'shetty', 4, 5, 'ENd']
