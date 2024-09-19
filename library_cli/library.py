class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_loaned = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.loaned_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print("Book already exists.")
        else:
            self.books[isbn] = Book(title, author, isbn)
            print("Book added successfully.")

    def update_book(self, isbn, title=None, author=None):
        if isbn in self.books:
            if title:
                self.books[isbn].title = title
            if author:
                self.books[isbn].author = author
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def search_book(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book.title.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")

    def add_member(self, name, member_id):
        if member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member_id] = Member(name, member_id)
            print("Member added successfully.")

    def update_member(self, member_id, name=None):
        if member_id in self.members:
            if name:
                self.members[member_id].name = name
            print("Member updated successfully.")
        else:
            print("Member not found.")

    def delete_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member deleted successfully.")
        else:
            print("Member not found.")

    def issue_book(self, member_id, isbn):
        if member_id not in self.members:
            print("Member not found.")
            return
        if isbn not in self.books or self.books[isbn].is_loaned:
            print("Book is not available.")
            return

        self.books[isbn].is_loaned = True
        self.members[member_id].loaned_books.append(isbn)
        print("Book issued successfully.")

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            print("Member not found.")
            return
        if isbn not in self.members[member_id].loaned_books:
            print("This member did not loan this book.")
            return

        self.books[isbn].is_loaned = False
        self.members[member_id].loaned_books.remove(isbn)
        print("Book returned successfully.")