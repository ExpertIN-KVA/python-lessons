# <= 10.000 --> 20%
# <= 15.000 --> 49%
# > 15.000  --> 65%


# income = float(input("Income:"))


# if income <= 10000:
#     print(str(income * 0.2))
# elif income <= 15000:
#     print(str(income * 0.49))
# else:
#     print(str(income * 0.65))


# 0 - 10.000      --> 20%
# 10.001 - 15.000 --> 49%
# 15.001 - ...    --> 65%

income = float(input("Income:"))
tax = 0

if income <= 10000:
    tax = income * 0.2
elif income <= 15000:
    tax = 10000 * 0.2 + (income - 10000) * 0.49
else:
    tax = 10000 * 0.2 + 5000 * 0.49 + (income - 15000) * 0.65


print(tax)
