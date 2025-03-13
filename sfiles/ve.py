def can_add_book(current_weight, book_weight):
    return current_weight + book_weight <= 200

def add_book(remaining_weight, book_weight):
    return remaining_weight - book_weight

def main():
    total_capacity = 200  # Total library capacity
    current_weight = 0  # Total weight of stored books
    book_count = 0  # Number of stored books
    
    while True:
        try:
            book_weight = float(input("Enter the book weight (or a negative number to exit): "))
            if book_weight < 0:
                break
            
            if can_add_book(current_weight, book_weight):
                current_weight = add_book(current_weight, book_weight)
                book_count += 1
                print(f"Book stored. Remaining available weight: {total_capacity - current_weight} kg.")
            else:
                print("Not enough space for this book. Process terminated.")
                break
        except ValueError:
            print("Please enter a valid number.")
    
    if book_count > 0:
        average_weight = current_weight / book_count
    else:
        average_weight = 0
    
    print("\nFinal Report:")
    print(f"Total remaining weight in the library: {total_capacity - current_weight} kg")
    print(f"Total weight of stored books: {current_weight} kg")
    print(f"Total number of books: {book_count}")
    print(f"Average book weight: {average_weight:.2f} kg")

if __name__ == "__main__":
    main()
