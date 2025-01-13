vehicle_length = float(
    input("Δώσε το μήκος του οχήματος (σε δεκαδικό ή ακέραιο αριθμό): ")
)
vehicle_type = input("Τύπος οχήματος (Φορτηγό/Λεωφορείο): ")
driver_seat = input("Θέση οδηγού (Σαλόνι/Κατάστρωμα): ")

vehicle_length = round(vehicle_length, 0)

total = 0

if vehicle_type == "Φορτηγό":
    total = vehicle_length * 5
else:
    total = vehicle_length * 4

if driver_seat == "Σαλόνι":
    total += 15
else:
    total += 10


if total > 50:
    total *= 0.9


print("Total: " + total)
