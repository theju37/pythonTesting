# Tuple : List and tuple does same thing
# tuple is immutable and list is mutable
# once tuple is created we cannot edit it / Change the beavior
# declare tuple
val = (1, 2, 3, 4)
print(val)  # (1, 2, 3, 4)
print(val[1])  # 2

# Dictionary - key:value pair (Like a hash table )
# declare Dictionary
a = {1: "First date ", "second": 2}
print(a)  # {1: 'First date ', 'second': 2}
print(a[1])  # First date

# create dictinary dynamicaly in run time
dict = {}
dict[1] = "Theju"
dict["LastName"] = "M"
print(dict)  # {1: 'Theju', 'LastName': 'M'}
dict["Husband"] = "Gowtham"
print(dict)  # {1: 'Theju', 'LastName': 'M', 'Husband': 'Gowtham'}
