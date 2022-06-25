# Part A: House Hunting

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
total_cost = total_cost * portion_down_payment
current_savings = 0
r = 0.04
month_salary = annual_salary / 12
month_savings = month_salary * portion_saved

number_of_months = 0

while current_savings < total_cost:
    number_of_months += 1
    current_savings += current_savings * r / 12
    current_savings += month_savings
    
print("Number of months:", number_of_months)