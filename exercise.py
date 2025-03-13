num_list = []
sum = 0
p = 1
zigoi = 0
peritoi = 0

while True:
    num = int(input("Give me a number: "))
    if num == -1:
        break

    num_list.append(num)


for number in num_list:
    sum = sum + number
    p = p * number
    if number % 2 == 0:
        zigoi += 1
    else:
        peritoi += 1

print("Το άθροισμα των στοιχείων της λίστας είναι ίσο με", sum)
print("Το γινόμενο των στοιχείων της λίστας είναι ίσο με", p)
print("Οι ζυγοί της λίστας είναι", zigoi)
print("Οι περιττοί της λίστας είναι", peritoi)
