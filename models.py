from past.builtins import raw_input


class Book:
    def __init__(self, book_id=" ", book_name=" ", author_name=" "):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name

    def add(self):
        print("\n \t \t \t Adding Book Record \t \t \t \n")
        self.book_id = raw_input("\t Enter Book ID:")
        self.book_name = raw_input("\t Enter Name of the Book:")
        self.author_name = raw_input("\t Enter Name of the Author:")
        print("\n \t \t \t Book Added \t \t \t")

    def show(self):
        print("\n \t \t Book Number:", self.book_id)
        print("\t \t Book Name:", self.book_name)
        print("\t \t Author Name:", self.author_name)

    def modify(self):
        print("\n \t \t Book ID.: ", self.book_id)
        self.book_name = raw_input("\t \t Enter New Book Name:")
        self.author_name = raw_input("\t \t Enter New Author Name:")
        print("\n \t \t Book Modified")

    def get_book_id(self):
        return self.book_id

    def report_book(self):
        print(self.book_id, self.book_name, self.author_name)


class Reader:
    def __init__(self, reader_id=" ", name=" ", reader_book_id=" ", token=0):
        self.reader_id = reader_id
        self.name = name
        self.reader_book_id = reader_book_id
        self.token = token

    def create(self):
        print("\n \t \t \t Creating Reader Record \t \t \t")
        print()
        self.reader_id = raw_input("\t \t Enter Reader's ID:")
        print()
        self.name = raw_input("\t \t Enter Name of the Reader:")
        self.reader_book_id = " "
        self.token = 0
        print("\t \t \t Reader Record Created \t \t \t \n")
        print("#" * 70)

    def show(self):
        print("\n \t Reader ID:", self.reader_id)
        print("\t Name:", self.name)
        print("\t Reader Book ID:", self.reader_book_id)

    def display(self):
        print()
        print("\t Reader ID is:", self.reader_id)
        print()
        print("\t Name of the Reader is:", self.name)
        if self.token == 1:
            print("\t Book ID is:", self.reader_book_id)

    def modify(self):
        print("\n \t Reader ID:", self.reader_id)
        self.name = raw_input("\t New Reader Name:")
        print("\t \t Reader's Name Modified !!")

    def get_id(self):
        return self.reader_id

    def get_book_id(self):
        return self.reader_book_id

    def get_token(self):
        return self.token

    def set_token(self):
        self.token = 1

    def reset_token(self):
        self.token = 0

    def set_book_id(self, t):
        self.reader_book_id = t

    def report(self):
        print(self.reader_id, self.name, self.token)
