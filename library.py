class Library:
    def __init__(self, list_of_books):
        self.availabe_books = list_of_books

    def display_available_books(self):
        print('Available Books:')
        for book in self.availabe_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.availabe_books:
            print('You have now borrowed', requested_book)
            self.availabe_books.remove(requested_book)
        else:
            print('Sorry, the name of the book is not available on our list')

    def add_book(self, returned_book):
        self.availabe_books.append(returned_book)
        print('Thank you for returning', returned_book)

class Customer:
    def request_books(self):
        print('Enter the name of the book you will like to borrow')
        self.book = input('Name of book: ')
        return self.book

    def return_book(self):
        print('Enter the name of the book you are returning ')
        self.book = input('Name of book: ')
        return self.book

library = Library(['Think and grow rich', 'Who will cry when you die', 'For one more day'])
customer = Customer()
while True:
    print('Enter 1 to display the available books')
    print('Enter 2 to request for a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit')

    user_choice = int(input('Enter a value here: '))
    if user_choice is 1:
        library.display_available_books()
    elif user_choice is 2:
        requested_book = customer.return_book()
        library.lend_book(requested_book)
    elif user_choice is 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice is 4:
        quit()

print(library.display_available_books())
#
