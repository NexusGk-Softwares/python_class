
withdrawal_amount =  float(input("Enter the amount you want to withdraw: "))
total_amount = withdrawal_amount
if withdrawal_amount > 10000:
    total_amount += withdrawal_amount * 0.10
elif  withdrawal_amount > 5000:
    total_amount += withdrawal_amount * 0.05
print("Total amount dispenced:  ", total_amount)
