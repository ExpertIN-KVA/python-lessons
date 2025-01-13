kilometers = int(input("Δώσε τα χιλιόμετρα του αυτοκινήτου: "))

next_service_category = (kilometers // 10000 + 1) * 10000

print(
    "Το επόμενο service θα γίνει σε "
    + next_service_category
    - kilometers
    + " χιλιόμετρα"
)


category = "Μεγάλο"
if next_service_category % 20000 != 0:
    category = "Μικρό"

print("Το επόμενο service θα είναι '" + category + "'")
