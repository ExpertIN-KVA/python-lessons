# 1.6 Ο Μάκης, ο Τάκης και ο Λάκης έπαιξαν ένα δελτίο στοιχήματος. Αποφάσισαν
# ότι αν κερδίσουν θα μοιραστούν τα κέρδη με βάση τη συμμετοχή τους κατά την πληρωμή του δελτίου.
# Να αναπτυχθεί ο αντίστοιχος κώδικας που θα διαβάζει τα κέρδη που επέφερε το δελτίο
# και το ποσό που πλήρωσε κάθε ένας από τους τρεις και να εμφανίζει το κέρδος που αναλογεί στον καθένα με
# βάση το ποσό με το οποίο συμμετείχαν. [1.9]


makis = float(input("Give the Makis's amount: "))
takis = float(input("Give the Takis's amount: "))
lakis = float(input("Give the Lakis's amount: "))

revenue = float(input("Revenue: "))


print("Makis's revenue: ", makis / revenue * 100)
print("Takis's revenue: ", takis / revenue * 100)
print("Lakis's revenue: ", lakis / revenue * 100)
