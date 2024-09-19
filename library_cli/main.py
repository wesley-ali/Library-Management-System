import sys
from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Update Member")
        print("7. Delete Member")
        print("8. Issue Book")
        print("9. Return Book")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter book ISBN to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            library.update_book(isbn, title if title else None, author if author else None)

        elif choice == '3':
            isbn = input("Enter book ISBN to delete: ")
            library.delete_book(isbn)

        elif choice == '4':
            keyword = input("Enter title or keyword to search: ")
            library.search_book(keyword)

        elif choice == '5':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)

        elif choice == '6':
            member_id = input("Enter member ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            library.update_member(member_id, name if name else None)

        elif choice == '7':
            member_id = input("Enter member ID to delete: ")
            library.delete_member(member_id)

        elif choice == '8':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.issue_book(member_id, isbn)

        elif choice == '9':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            library.return_book(member_id, isbn)

        elif choice == '0':
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()