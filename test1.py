#to calculate the BMI
weight = float(input("Enter your weight in kilograms: "))
height =  float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
#It divides the weight (in kilograms) by the square of the height (in meters).
print("Your BMI is:", bmi) 
