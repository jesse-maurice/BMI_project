weight = input("What is your weight? ")
height = input("What is your height? ")
bmi_weight = int(weight)
bmi_height = float(height)
bmi_total = round(bmi_weight / bmi_height ** 2)
print(f"Your BMI is {bmi_total}. ")
