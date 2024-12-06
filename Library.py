from uuid import uuid4

class Book:
    def __init__(self, title, author, year):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_status(self):
        return self.status


    def __str__(self):
        return f'ID:{self.id}, Title:{self.title}, Author:{self.author}, Year:{self.year}, Status:{self.status}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def set_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        return new_book


    def list_of_books(self):
        if not self.books:
            return "В библиотеке нет книг."
        return '\n'.join(str(book) for book in self.books)


    def search_book_title(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return "Книга не найдена."


    def search_book_author(self, author):
        for book in self.books:
            if book.get_author().lower() == author.lower():
                return book
        return "Книга не найдена."

    def search_book_year(self, year):
        for book in self.books:
            if book.get_year() == year:
                return book
        return "Книга не найдена."


    def delete(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                self.books.remove(book)
                return f'Книга с ID:{book_id} успешно удалена.'
        return "Книга не найдена."


    def change_status(self, book_id, new_status):
        if new_status not in ['в наличии', 'выдана']:
            return 'Неверный статус.'
        for book in self.books:
            if book.get_id() == book_id:
                book.status = new_status
                return f'Статус книги с ID {book_id} изменен на {new_status}.'
        return "Книга не найдена."


library = Library('P DIDDY')


while True:
    print(
        'Welcome to Library\nMENU: Books\n1) List\n2) Search books by title\n3) Search books by author\n4) Search books by year\n5) Add book\n6) Delete book\n7) Change status')
    user_input = input('Enter action: ').strip().lower()

    if user_input == '1' or user_input == 'list':
        print(library.list_of_books())

    elif user_input == '2' or user_input == 'search books by title':
        search_title = input('Enter title: ').strip()
        result = library.search_book_title(search_title)
        print(result)

    elif user_input == '3' or user_input == 'search books by author':
        search_author = input('Enter author: ').strip()
        result = library.search_book_author(search_author)
        print(result)

    elif user_input == '4' or user_input == 'search books by year':
        try:
            search_year = int(input('Enter year: ').strip())
            result = library.search_book_year(search_year)
            print(result)
        except ValueError:
            print("Please enter a valid year.")

    elif user_input == '5' or user_input == 'add book':
        user_add_title = input('Enter title: ').strip()
        user_add_author = input('Enter author: ').strip()
        try:
            user_add_year = int(input('Enter year: ').strip())
            library.set_book(user_add_title, user_add_author, user_add_year)
            print(f'Книга Title: {user_add_title}, Author: {user_add_author}, Year: {user_add_year} успешно добавлена')
        except ValueError:
            print("Пожалуйста введите правильный год.")

    elif user_input == '6' or user_input == 'delete book':
        user_delete = input('Enter book ID: ').strip()
        print(library.delete(user_delete))

    elif user_input == '7' or user_input == 'change status':
        book_id_to_change = input('Enter book ID to change status: ').strip()
        new_status = input('Enter new status ("в наличии" or "выдана"): ').strip()
        print(library.change_status(book_id_to_change, new_status))

    else:
        print('Неправильный ввод, пожалуйста повторите попытку')