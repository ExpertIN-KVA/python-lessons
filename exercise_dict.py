# Ένα οχηματαγωγό πλοίο μεταφέρει μόνο φορτηγά και λεωφορεία και η χρέωση κάθε μεταφοράς προκύπτει με τον παρακάτω τρόπο:
# •	Υπολογίζεται το μήκος του οχήματος (π.χ. 3.4 μέτρα), έπειτα στρογγυλοποιείται στον πλησιέστερο ακέραιο (π.χ. 3 μέτρα) και η χρέωση είναι 5€ ανά μέτρο για τα οχήματα τύπου “Φορτηγό” και 4€ ανά μέτρο για τα “Λεωφορεία”.
# •	Αν ο οδηγός επιλέξει τη θέση “Σαλόνι”, πληρώνει ένα εισιτήριο αξίας 15€, ενώ αν επιλέξει θέση τύπου “Κατάστρωμα” πληρώνει 10€.
# •	Υπολογίζεται το άθροισμα των παραπάνω χρεώσεων.
# •	Αν η τελική χρέωση ξεπεράσει τα 50€ τότε υπάρχει μια έκπτωση 10% στο υπερβαίνων ποσό.
# •	Στο τελικό ποσό προστίθεται ΦΠΑ 24%
# Να γραφεί πρόγραμμα που να υλοποιεί την παραπάνω λογική για την έκδοση ενός εισιτηρίου και του κόστους του. [3.6]

# Η ασκηση να τροποποιηθει και να ζηταει τα στοιχεια για καθε οδηγο μεχρι ο χρηστης να πει οτι δεν θελει να συνεχισει την καταχωριση δεδομενων (μπορεις να βαλεις μια ερωτηση και να σου λεει οτι θελει ή οχι να συνεχισει την εισαγωγη των δεδομενων).

# Επισης, στο τελος της εισαγωγης των δεδομενων να εμφανιζει για καθε ενα απο τα εισιτηρια που δημιουργηθηκαν τα στοιχεια:
# - Τυπος οχηματος
# - Μηκος οχηματος
# - Κοστος για το οχημα
# - Θεση οδηγου
# - Κοστος θεσης οδηγου
# - Συνολο (πριν την εκπτωση και το φπα)
# - Ποσο εκπτωσης
# - Φπα
# - Τελικο ποσο (μετα την εκπτωση και το φπα)

# Αυτα θελουμε να εμφανιζονται στην παρακατω μορφη:
# 1. <τυπος οχηματος> - <μηκος οχηματος> - <κοστος οχηματος> - <θεση οδηγου> - <κοστος θεσης οδηγου> - <συνολο> - <εκπτωση> - <φπα> - <συνολο μετα την εκπτωση και τον φπα>


data = []
while True:
    data.append({})
    last_index = len(data) - 1

    data[last_index]["vehicle_length"] = float(input("Δώσε το μήκος του οχήματος: "))
    while True:
        data[last_index]["vehicle_type"] = input(
            "Δώσε τύπο οχήματος (Λεωφορείο/Φορτηγό): "
        )
        if (
            data[last_index]["vehicle_type"] == "Φορτηγό"
            or data[last_index]["vehicle_type"] == "Λεωφορείο"
        ):
            break

    while True:
        data[last_index]["driver_seat"] = input(
            "Δώσε θέση οδηγού (Σαλόνι/Κατάστρωμα): "
        )
        if (
            data[last_index]["driver_seat"] == "Σαλόνι"
            or data[last_index]["driver_seat"] == "Κατάστρωμα"
        ):
            break

    data[last_index]["vehicle_length"] = round(data[last_index]["vehicle_length"], 0)

    if data[last_index]["vehicle_type"] == "Φορτηγό":
        data[last_index]["cost_for_vehicle"] = data[last_index]["vehicle_length"] * 5
    else:
        data[last_index]["cost_for_vehicle"] = data[last_index]["vehicle_length"] * 4

    data[last_index]["total"] = data[last_index]["cost_for_vehicle"]

    if data[last_index]["driver_seat"] == "Σαλόνι":
        data[last_index]["cost_for_seat"] = 15
    else:
        data[last_index]["cost_for_seat"] = 10

    data[last_index]["total"] = (
        data[last_index]["total"] + data[last_index]["cost_for_seat"]
    )

    data[last_index]["total_discount_fpa"] = data[last_index]["total"]
    if data[last_index]["total"] > 50:
        data[last_index]["discount"] = (data[last_index]["total"] - 50) * 0.1
        data[last_index]["total_discount_fpa"] = (
            data[last_index]["total"] - data[last_index]["discount"]
        )

    data[last_index]["fpa"] = data[last_index]["total_discount_fpa"] * 0.24
    data[last_index]["total_discount_fpa"] = (
        data[last_index]["total_discount_fpa"] + data[last_index]["fpa"]
    )

    continue_answer = ""
    while True:
        continue_answer = input("Continue? (Yes/No): ")
        if continue_answer == "Yes" or continue_answer == "No":
            break

    if continue_answer == "No":
        break


print("\nTotal tickets cutted")
for i in range(0, len(data)):
    print(
        str(i + 1)
        + ". "
        + data[i]["vehicle_type"]
        + " - "
        + str(data[i]["vehicle_length"])
        + " - "
        + str(data[i]["cost_for_vehicle"])
        + " - "
        + data[i]["driver_seat"]
        + " - "
        + str(data[i]["cost_for_seat"])
        + " - "
        + str(data[i]["total"])
        + " - "
        + str(data[i]["discount"])
        + " - "
        + str(data[i]["fpa"])
        + " - "
        + str(data[i]["total_discount_fpa"])
    )
