# 1.1 Να γραφεί πρόγραμμα το οποίο θα διαβάζει 4 αριθμούς, θα υπολογίζει το άθροισμα και το μέσο
# όρο τους, θα εμφανίζει το άθροισμα, μετά το μήνυμα ‘Ο μέσος όρος είναι’ ακολουθούμενο από τον
# μέσο όρο των τεσσάρων αριθμών. [1.1]


number1 = int(input("Give me the number 1: "))
number2 = int(input("Give me the number 2: "))
number3 = int(input("Give me the number 3: "))
number4 = int(input("Give me the number 4: "))


total = number1 + number2 + number3 + number4
average = total / 4


print("Total: ", total)
print("Average: ", average)
