# This allows a user to input his salary
salary=float(input('Please enter your gross salary: '))

if salary <= 600000:
    print('Your salary is non-taxable')
if salary >= 650000:
    print("Your salary is taxable with a discount ")
    net_salary=salary*0.3
    print(f"Your net salary is {net_salary}")
if salary == 10000:
    print('This is transport number')