class Book:
    aval_books = {}

    def add_book(self, title, author):
        self.aval_books[title] = author

    def show_books(self):
        if len(self.aval_books.items()) > 0:
            print("Available Books:")
            for title, author in self.aval_books.items():
                print(f"'{title}' by '{author}'")
        else:
            print("no books available")


class Member(Book):
    issued_book = {}

    def issue_book(self, bookname):
        if bookname in super().aval_books.keys():
            self.issued_book[bookname] = super().aval_books.pop(bookname)
            print(f"'{bookname}' has been issued")
            print(self.issued_book)
        else:
            print(f"'{bookname}' is not available at the moment")

    def return_book(self, bookname):
        if bookname in self.issued_book.keys():
            super().aval_books[bookname] = self.issued_book.pop(bookname)
            print(f"{bookname} has been returned")
        else:
            print(f"'{bookname}' is not belong to this library")



m = Member()
m.add_book("python", "Henry")
m.add_book("java", "Jack")
m.add_book("javascript", "James")
m.add_book("ruby", "Chris")
m.add_book("html", "Tony")
m.add_book("css", "Tim")

m.show_books()

m.issue_book("python")
m.show_books()

m.issue_book("Jaava")
m.show_books()


m.return_book("python")
m.show_books()



