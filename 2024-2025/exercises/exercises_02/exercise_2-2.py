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
