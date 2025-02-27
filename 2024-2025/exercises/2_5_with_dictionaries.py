# 2.5 Ένα οχηματαγωγό πλοίο μεταφέρει μόνο φορτηγά και λεωφορεία και η χρέωση κάθε μεταφοράς προκύπτει με τον παρακάτω τρόπο:

#     - Υπολογίζεται το μήκος του οχήματος (π.χ. 3.4 μέτρα), έπειτα στρογγυλοποιείται στον πλησιέστερο ακέραιο (π.χ. 3 μέτρα)
#       και η χρέωση είναι 5€ ανά μέτρο για τα οχήματα τύπου “Φορτηγό” και 4€ ανά μέτρο για τα “Λεωφορεία”.
#     - Αν ο οδηγός επιλέξει τη θέση “Σαλόνι”, πληρώνει ένα εισιτήριο αξίας 15€, ενώ αν επιλέξει θέση τύπου “Κατάστρωμα” πληρώνει 10€.
#     - Υπολογίζεται το άθροισμα των παραπάνω χρεώσεων.
#     - Αν η τελική χρέωση ξεπεράσει τα 50€ τότε υπάρχει μια έκπτωση 10% στο υπερβαίνων ποσό.
#     - Στο τελικό ποσό προστίθεται ΦΠΑ 24%

# Να γραφεί πρόγραμμα που να υλοποιεί την παραπάνω λογική για την έκδοση ενός εισιτηρίου και του κόστους του. [3.6]


data = []
while True:
    data.append({})
    last_index = len(data) - 1

    data[last_index]["vehicle_length"] = float(
        input("Δώσε το μήκος του οχήματος (σε δεκαδικό ή ακέραιο αριθμό): ")
    )
    data[last_index]["vehicle_type"] = input("Τύπος οχήματος (Φορτηγό/Λεωφορείο): ")
    data[last_index]["driver_seat"] = input("Θέση οδηγού (Σαλόνι/Κατάστρωμα): ")

    data[last_index]["vehicle_length"] = round(data[last_index]["vehicle_length"], 0)

    if data[last_index]["vehicle_type"] == "Φορτηγό":
        data[last_index]["cost_for_vehicle"] = data[last_index]["vehicle_length"] * 5
    else:
        data[last_index]["cost_for_vehicle"] = data[last_index]["vehicle_length"] * 4

    data[last_index]["total"] = data[last_index]["cost_for_vehicle"]

    if data[last_index]["driver_seat"] == "Σαλόνι":
        data[last_index]["driver_seat_cost"] = 15
        data[last_index]["total"] += 15
    else:
        data[last_index]["driver_seat_cost"] = 10
        data[last_index]["total"] += 10

    data[last_index]["discount"] = 0
    if data[last_index]["total"] > 50:
        data[last_index]["discount"] = data[last_index]["total"] * 0.1
        data[last_index]["total_after_disc_fpa"] = (
            data[last_index]["total"] - data[last_index]["discount"]
        )

    data[last_index]["fpa"] = data[last_index]["total_after_disc_fpa"] * 0.24
    data[last_index]["total_after_disc_fpa"] = (
        data[last_index]["total_after_disc_fpa"] + data[last_index]["fpa"]
    )
    print("Total: " + data[last_index]["total_after_disc_fpa"])

    continue_answer = input("Do you want to continue? (yes/no): ")
    if continue_answer == "no":
        break


print()
print("Tickets sold:")
for i in range(0, len(data)):
    print(
        str(i)
        + ". "
        + data[i]["vehicle_type"]
        + " - "
        + data[i]["vehicle_length"]
        + " - "
        + data[i]["cost_for_vehicle"]
        + " - "
        + data[i]["driver_seat"]
        + " - "
        + data[i]["driver_cost_seat"]
        + " - "
        + data[i]["total"]
        + " - "
        + data[i]["discount"]
        + " - "
        + data[i]["fpa"]
        + " - "
        + data[i]["total_after_disc_fpa"]
    )
