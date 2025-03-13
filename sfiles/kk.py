
def can_add_book(current_weight, book_weight, max_weight):
    return current_weight + book_weight <= max_weight
def add_book(remaining_weight, book_weight):
    return remaining_weight - book_weight
def store_books():
    max_weight = 200
    total_weight = 0
    number_of_books = 0
    total_weight_of_books = 0
    while True:
        weight = input("Δώσε το βάρος του βιβλίου σε κιλά (ή γράψε 'end' για να σταματήσεις): ")

        if weight.lower() == 'end':
             break
        try:
            weight = float(weight)
            if weight < 0:
                print("Τα κιλά θα πρέπει να είναι θετικός αριθμός.")
                continue
        except ValueError:
            print("Δώσε ένα έγκυρο νούμερο για τα κιλά.")
            continue
        if can_add_book(total_weight, weight, max_weight):
            total_weight += weight
            total_weight_of_books += weight
            number_of_books += 1
            max_weight = add_book(max_weight, weight)
            print("Το βιβλίο προστέθηκε. Το συνολικό βάρος είναι", total_weight, "κιλά.")
        else:
            print("Το βιβλίο δεν προστέθηκε στην βιβλιοθήκη γιατί ξεπέρασε το όριο των 200 κιλών.")
            break
    if number_of_books > 0:
        average_weight = total_weight_of_books / number_of_books
    else:
        average_weight = 0

    print("\nΗ διαδικασία ολοκληρώθηκε.")
    print("Τα απομείνοντα κιλά στην βιβλιοθήκη είναι", max_weight, "κιλά.")
    print("Το συνολικό βάρος των βιβλίων στη βιβλιοθήκη είναι", total_weight_of_books, "κιλά.")
    print("TΟ αριθμός των βιβλίων είναι", number_of_books)
    print("Ο μέσος όρος των κιλών του βιβλίου στη βιβλιοθήκη είναι", average_weight, "κιλά.")
store_books()   