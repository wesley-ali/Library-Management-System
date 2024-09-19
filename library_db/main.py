from models import Session, Book, Member, Loan
import datetime

session = Session()

def add_book(title, author, genre, year_published):
    new_book = Book(title=title, author=author, genre=genre, year_published=year_published)
    session.add(new_book)
    session.commit()
    print("Book added:", new_book)

def add_member(name, email):
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()
    print("Member added:", new_member)

def issue_book(member_id, book_id):
    loan = Loan(member_id=member_id, book_id=book_id)
    session.add(loan)
    session.commit()
    print("Book issued:", loan)

def return_book(loan_id):
    loan = session.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        loan.return_date = datetime.date.today()
        session.commit()
        print("Book returned:", loan)
    else:
        print("Loan not found.")

def list_books():
    books = session.query(Book).all()
    for book in books:
        print(book)

def list_members():
    members = session.query(Member).all()
    for member in members:
        print(member)

def list_loans():
    loans = session.query(Loan).all()
    for loan in loans:
        print(loan)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Members")
        print("7. List Loans")
        print("0. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            year_published = int(input("Enter year published: "))
            add_book(title, author, genre, year_published)

        elif choice == '2':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)

        elif choice == '3':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            issue_book(member_id, book_id)

        elif choice == '4':
            loan_id = int(input("Enter loan ID: "))
            return_book(loan_id)

        elif choice == '5':
            list_books()

        elif choice == '6':
            list_members()

        elif choice == '7':
            list_loans()

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()