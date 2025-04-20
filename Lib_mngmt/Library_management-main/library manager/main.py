from add_book import add_book_
from delete_book import delete_book
from add_user import add_user
from show_books import display_all_books
from search_book import search_books_by_title
from delete_user import delete_user_by_id
from update_user import update_user_by_id
from search_user import search_user_by_field
from show_users import show_all_users
from borrow import borrow_book
from return_ import return_book
from show_borrow import show_borrowed_books

def main():
    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Display All Books")
        print("4. Search Book by Title")
        print("5. Add User")
        print("6. Delete User")
        print("7. Show All Users")
        print("8. Search User")
        print("9. Update User")
        print("10. Borrow Book")
        print("11. Return Book")
        print("12. Show Borrowed Books of User")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = int(input("Enter Published Year: "))
            genre = input("Enter Genre: ")
            add_book_(book_id, title, author, year, genre)

        elif choice == '2':
            book_id = input("Enter Book ID to delete: ")
            delete_book(book_id)

        elif choice == '3':
            display_all_books()

        elif choice == '4':
            title = input("Enter keyword to search in title: ")
            search_books_by_title(title)

        elif choice == '5':
            user_id = input("Enter User ID: ")
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            add_user(user_id, username, email)

        elif choice == '6':
            user_id = input("Enter User ID to delete: ")
            delete_user_by_id(user_id)

        elif choice == '7':
            show_all_users()

        elif choice == '8':
            field = input("Enter field to search by (username/email): ")
            value = input("Enter value: ")
            search_user_by_field(field, value)

        elif choice == '9':
            user_id = input("Enter User ID to update: ")
            field = input("Enter field to update: ")
            value = input("Enter new value: ")
            update_user_by_id(user_id, {field: value})

        elif choice == '10':
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            duration = int(input("Enter Borrow Duration (days): "))
            borrow_book(user_id, book_id, duration)

        elif choice == '11':
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID to return: ")
            print(return_book(user_id, book_id))

        elif choice == '12':
            user_id = input("Enter User ID: ")
            show_borrowed_books(user_id)

        elif choice == '13':
            print("Exiting Library Management System. Bye!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 13.")

if __name__ == "__main__":
    main()
from add_book import add_book_
from show_books import display_all_books

# Test: Add a book and display all books
add_book_("b001", "1984", "George Orwell", 1949, "Dystopian")
display_all_books()


    


