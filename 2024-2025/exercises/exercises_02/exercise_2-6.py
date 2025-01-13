incomes = float(input("Incomes: "))
review = int(input("Review points: "))

prim = 0
if review > 95:
    prim = incomes * 0.2
elif review > 90:
    prim = incomes * 0.15
elif review > 80:
    prim = incomes * 0.1

print("Prim (in eur): " + prim)
print("Total incomes (in eur): " + prim + incomes)
