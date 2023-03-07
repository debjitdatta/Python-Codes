height = float(input("Enter your height (in m): "))
weight = float(input("Enter your weight (in kg): "))

BMI = weight/(height*height)
print("Your Body Mass Index (BMI) is : ", BMI)
# If your BMI is less than 18.5, it falls within the underweight range.
# If your BMI is 18.5 to <25, it falls within the healthy weight range.
# If your BMI is 25.0 to <30, it falls within the overweight range.
# If your BMI is 30.0 or higher, it falls within the obesity range.

if BMI<18.5:
    print("You're Underweight")
elif BMI>18.5 and BMI<25:
    print("Great! You're Healthy")
elif BMI>25 and BMI<30:
    print("You're overweight")
elif BMI>30:
    print("Your BMI falls within the obesity range")
else:
    print("Kindly add the valid input")
