def main():
    all_amount = 0
    max_difference = -1
    max_difference_name = ""


    for i in range(1,1001):
        company_name = input("Give me the company name: ")
        company_sum = 0

        max = -1
        min = -1

        company_sum, amount_of_damage, max, min = four_years(company_sum, max, min)
        
        company_sum = company_sum - max - min
        company_amount = (company_sum / 2) * 0.55

        print(company_name)
        print(company_sum)

        all_amount += company_amount

        if max - min > max_difference:
            max_difference = max - min
            max_difference_name = company_name

    print(all_amount)
    print(max_difference)
    print(max_difference_name)



def four_years(company_sum, max, min):
    for j in range(0,4):
        amount_of_damage = float(input("Give me the amount of damage: "))
        company_sum += amount_of_damage
        amount_of_damage = if_for_max(amount_of_damage, max)
        if amount_of_damage  < min or j == 0:
            min = amount_of_damage
        return company_sum, amount_of_damage, max, min

def if_for_max(amount_of_damage, max):
    if amount_of_damage > max:
        max = amount_of_damage
        return amount_of_damage

if __name__ == "__main__":
    main()