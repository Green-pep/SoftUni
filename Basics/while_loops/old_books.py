search_book = input()
checked_books = 0
more_books = input()

while search_book != more_books:
    if more_books == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1
    more_books = input()
if search_book == more_books:
    print(f"You checked {checked_books} books and found it.")