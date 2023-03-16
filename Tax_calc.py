#Exercise 12: Calculate income tax for the given income by adhering to the below rules
#For example, suppose the taxable income is 45000 the income tax payable is
#10000*0% + 10000*10%  + 25000*20% = $6000.

salary = int(input("Enter your Salary: "))
tax_payable = 0
print("Your salary is :", salary)

if salary <= 10000:
    print("Your Payable tax amount is 0")

elif salary <=20000:
    salary = salary - 10000
    tax_payable = salary * 10/100
    print("Your Payable tax amount is: ", tax_payable)

else:
    tax_payable = 0

    tax_payable = 10000 * 10/100

    tax_payable = tax_payable + (salary - 20000) * 20/100
    print("Your Payable tax amount is : ", tax_payable)