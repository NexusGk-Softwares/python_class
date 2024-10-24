#using the logical operator 'and'
input1 = input("Enter first value ")
input2 = input("Enter second value ")
input3 = input("Enter third value ")
input4 = input("Enter fourth value ")

if int(input1) > 0 and int(input2) > 0 and int(input3) > 0 and int(input4) > 0:
    print("All values are positive")
else:
    print("At least one of the values is not positive")

