# Part A: House Hunting

# annual_salary = int(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
# total_cost = int(input("Enter the cost of your dream home: "))

# portion_down_payment = 0.25
# total_cost = total_cost * portion_down_payment
# current_savings = 0
# r = 0.04
# month_salary = annual_salary / 12
# month_savings = month_salary * portion_saved

# number_of_months = 0

# while current_savings < total_cost:
#     number_of_months += 1
#     current_savings += current_savings * r / 12
#     current_savings += month_savings
    
# print("Number of months:", number_of_months)



# Part B: Saving, with a raise

# annual_salary = int(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
# total_cost = int(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

# portion_down_payment = 0.25
# total_cost = total_cost * portion_down_payment
# current_savings = 0
# r = 0.04
# month_salary = annual_salary / 12
# month_savings = month_salary * portion_saved

# number_of_months = 0

# while current_savings < total_cost:
#     number_of_months += 1
#     current_savings += current_savings * r / 12
#     current_savings += month_savings
#     if number_of_months > 0 and number_of_months % 6 == 0:
#         annual_salary = annual_salary + (annual_salary * semi_annual_raise)
#         month_salary = annual_salary / 12
#         month_savings = month_salary * portion_saved
    
# print("Number of months:", number_of_months)



# Part C: Finding the right amount to save away

# startingSalary = int(input("Enter the starting salary: "))
# semiAnnualRaise = 0.07
# r = 0.04
# portionDownPayment = 0.25
# costOfHouse = 1000000
# totalCostNeeding = costOfHouse * portionDownPayment
# monthSalary = startingSalary / 12

# epsilon = 100

# low = 0
# high = 10000
# guessRate = float((low + high) / 2)

# numberOfGuess = 0
# number_of_months = 0
# currentSaving = 0


# while number_of_months <= 36:
#     number_of_months += 1
#     currentSaving += currentSaving * r / 12
#     currentSaving += monthSalary * (guessRate / 10000)
    
epsilon = 0.001
low = 1
high = 2
x = high
while abs((x**2 - 3) - 0) >= epsilon :
    if x**2 - 3 - 0 > epsilon:
        high = x
    else:
        low = x
    x = (low + high) / 2
print(x)

