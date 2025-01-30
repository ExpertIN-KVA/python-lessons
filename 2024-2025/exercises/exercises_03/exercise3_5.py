total_help = 0
max_diff = -1
max_diff_cn = ""

for i in range(0, 1000):

    company_name = input("Company name: ")

    maximum = -1
    minimum = -1
    total_years = 0
    for j in range(0, 4):
        year = float(input("Give me for year " + str(j + 1) + ": "))

        if year > maximum:
            maximum = year

        if minimum > year or j == 0:
            minimum = year

        total_years += year

    total_years -= maximum + minimum

    help_amount = total_years / 2 * 0.55
    total_help += help_amount

    diff = maximum - minimum
    if max_diff < diff:
        max_diff = diff
        max_diff_cn = company_name

    print("Company name: " + company_name + " - " + str(help_amount))


print("Total help: " + str(total_help))
print("Company with maximum help: " + max_diff_cn)
