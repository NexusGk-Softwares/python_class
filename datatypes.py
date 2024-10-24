    #NexusGK___PYTHON___DATA__STRUCTURES
#lists
employees = ["John Doe", "Jane Smith", "Michael Johnson"]
print(employees)

#accessing elements
print(employees[0])  # prints "John Doe"
print(employees[1])  # prints "Jane Smith"

#modifying elements 
employees[0] = "Jane Doe"
print(employees)  # prints ["Jane Doe", "Jane Smith", "Michael Johnson"]

#adding elements
employees.append("David Brown")
print(employees)  # prints ["Jane Doe", "Jane Smith", "Michael Johnson", "David Brown"]

#removing elements
employees.remove("Jane Smith")
print(employees)  # prints ["Jane Doe", "Michael Johnson", "David Brown"]

#length of the list
print(len(employees))  # prints 3

#iterating over a list  
for employee in employees:
    print(employee)
    
#slicing a list    
print(employees[1:3])  # prints ["Michael Johnson", "David Brown"]
print(employees[:2])  # prints ["Jane Doe", "Michael Johnson"]
print(employees[2:])  # prints ["David Brown"]

#concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # prints [1, 2, 3, 4, 5, 6]

#nested lists
nested_list = [["apple", "banana"], ["orange", "grape"]]
print(nested_list[0][1])  # prints "banana"
print(nested_list[1][1])  # prints "grape"

