monthly_payment = int(input("Δώστε την ακέραια μισθοδοσία του υπαλλήλου: "))

print("50€: ", monthly_payment // 50)
print("20€: ", monthly_payment % 50 // 20)
print("10€: ", monthly_payment % 50 % 20 // 10)
print("5€: ", monthly_payment % 50 % 20 % 10 // 5)
print("1€: ", monthly_payment % 50 % 20 % 10 % 5)
