# Making a BMI calculator

# User info
user_name = input("Enter your name: ").upper()
user_weight_type = input("Select weight units(i.e 'kg' for Kilogram and 'lb' for Pound): ").lower()
user_weight = float(input("Enter your weight: "))
user_height_type = input("Select unit of height(i.e. 'm' for meter and 'cm' for centimeter): ").lower()
user_height = float(input("Enter your height: "))


# Unit conversions

if user_weight_type == "lb":
    converted_weight = (user_weight * 0.453)
else:
    converted_weight = user_weight

if user_height_type == "cm":
    converted_height = user_height/100
else:
    converted_height = user_height

# User BMI

user_bmi = (converted_weight)/(converted_height **2)

# user_category

if user_bmi < 18.5:
    user_category = "Under Weight"

if 18.5 < user_bmi and user_bmi < 25:
    user_category = "Healthy"

if user_bmi > 25 and user_bmi < 30:
    user_category = "Overweight"

if user_bmi > 30 and user_bmi < 35:
    user_category = "Obese"

print(f"Hello {user_name}! Your BMI is {user_bmi} and you fall under catogary of '{user_category}'.")
