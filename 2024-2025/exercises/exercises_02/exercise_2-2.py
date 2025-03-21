# 2.2 Μια κατασκευαστική εταιρία πληρώνει τους υπαλλήλους της το βασικό μισθό και 3
# επιδόματα, το οικογενειακό, ένα χρονοεπίδομα και ένα επίδομα θέσης ευθύνης.
# Ο βασικός μισθός προκύπτει από τις ημέρες που εργάζεται κάθε μήνα ο υπάλληλος.
# Το οικογενειακό επίδομα είναι 25€ για κάθε παιδί, το χρονοεπίδομα είναι 30€ για κάθε συμπληρωμένη
# τριετία, ενώ το ημερομίσθιο 35€. Το επίδομα θέσης ευθύνης είναι 100€ αν ο υπάλληλος
# κατέχει θέση προϊσταμένου, διαφορετικά δεν το δικαιούται. Να γράψετε έναν κώδικα που
# για έναν υπάλληλο να διαβάζει τον αριθμό των παιδιών του, τα χρόνια προϋπηρεσίας, τις ημέρες που
# εργάζεται μέσα σε ένα μήνα και το επίδομα θέσης ευθύνης που δικαιούται (100€ ή 0€) εμφανίζοντας αντίστοιχα
# τα μηνύματα “Δώστε αριθμό παιδιών και χρόνια προϋπηρεσίας” και “Δώστε ημέρες εργασίας και επίδομα θέση ευθύνης”
# και να τυπώνει τον συνολικό μισθό του για το συγκεκριμένο μήνα. [2.2]


print("Δώστε αριθμό παιδιών και χρόνια προϋπηρεσίας")
children_count = int(input())
workable_years = int(input())

print("Δώστε ημέρες εργασίας και επίδομα θέσης ευθύνης")
working_days = int(input())
epidoma_thesis_efthinis = float(input())


total_income = children_count * 25  # οικογενειακό επίδομα
total_income += (workable_years // 3) * 30  # προσθήκη χρονοεπιδόματος
total_income += working_days * 35  # προσθήκη εργάσιμων ημερών
total_income += epidoma_thesis_efthinis  # προσθήκη επιδόματος θέσης ευθύνης


print("Total income: ", total_income)
