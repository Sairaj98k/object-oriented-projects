class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 

    def get_summary(self):
        print(f'''
Title: {self.title}
Author: {self.author}
Year of publication: {self.year}
              ''')


class Library:
    def __init__(self):
        self.books = []
    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        # self.books.remove(book)
        del self.books[book - 1]

    def view_books(self):
        if not self.books:
            print('No books in the library!')
        else:
            for books in self.books:
                books.get_summary()


def main():
    library = Library()

    while True:
        print('''
1. Add book
2. Remove books
3. View books
4. Exit
''')
        user_input = int(input('> '))
        if user_input == 1:
            title = input('Enter the title of the book: ')
            author = input('Enter the auhtor of the book: ')
            year = input('Enter the year of the publication: ')
            book = Book(title, author, year)
            library.add_books(book)

        elif user_input == 2:
            library.view_books()
            user_input = int(input('>'))
            library.remove_books(user_input)

        elif user_input == 3:
            library.view_books()
            
        elif user_input == 4:
            break

main()