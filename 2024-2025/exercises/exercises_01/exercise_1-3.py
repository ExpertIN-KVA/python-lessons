# 1.3 Να γίνει πρόγραμμα που να διαβάζει το κόστος ενός προϊόντος και να εμφανίζει: [1.4]
#   1. Ποια θα είναι η τελική τιμή αν μας γίνει έκπτωση 30%
#   2. Ποια θα είναι η τελική τιμή αν μετά την έκπτωση προστεθεί 24% ΦΠΑ


product_price = float(input("Product price: "))


# Ποια θα είναι η τελική τιμή αν μας γίνει έκπτωση 30%
final30 = product_price * 0.7
print("Final after 30% discount", final30)

# Ποια θα είναι η τελική τιμή αν μετά την προστεθεί 24% ΦΠΑ
finalWithFpa = final30 * 1.24
print("Final price after FPA addition: ", finalWithFpa)
