
import csv

class Book:
    def __init__(self, book_id, author_name, book_title, pub_year, genre, edition, quantity):
        self.book_id = book_id
        self.author_name = author_name
        self.title = book_title
        self.pub_year = pub_year
        self.genre = genre 
        self.edition = edition
        self.quantity = quantity
    

    def add_book(self):
            book_id = input("Enter book ID: ")
            author_name = input("Enter author name: ")
            book_title = input("Enter book title: ")
            pub_year = input("Enter publication year: ")
            genre = input("Enter book genre: ")
            edition = input("Enter book edition: ")
            quantity = input("Enter book quantity: ")

            
            book_data = f"{book_id},{author_name},{book_title},{pub_year},{genre},{edition},{quantity}\n"
            found = False
            with open("book_data.csv", "r+") as file:
                for line in file:
                    if book_data.strip() ==line.strip():
                        found = True
                        break
            if found: 
                print ("This book already exist in the system!! ")
        
            else:
                with open("book_data.csv", "a+" ) as file:
                    file.write(book_data)
                print(" Book added Sucessfully!!")

            # if not found:
            #     with open("book_data.csv", "a+") as file:
            #         file.write(book_data)
            #     print("Book added successfully!")
            # else:
            #     print("Book already exists ")

    def search_by_field(self, field_name, index ):
        found = False
        with open("book_data.csv", "r") as file:
            for line in file: 
                book_info = line.strip().split(",")
                if book_info[index] == field_name:
                    found = True 
                    return found 
        return found
          

def main(): 
    book = Book('book_id ==book_id', 'author_name ==author_name', 'book_title==book-title', 'pub_year==pub_year', 'genre==genre', 'edition==edition', 'quantity==quantity')
    while True: 
        print("\n Enter your choice  ")
        print( "1. Add book ")
        print ("2. Search by author")
        print ("3. Search by title")
        print ("4. Search book by Pub year")
        print ("5. Search book by genre")
        print ("6. Search by edition")
        print ("7. Search for quantity ")
        print ("8. exit")

        user_choice = input(" Enter your choice (1-8) :")

        if user_choice == "1":
            book.add_book()
        elif user_choice == "2":
            author_name = input("enter author name:  ")
            found = book.search_by_field(author_name, 1)
            if found:
                print (" Book found ")
            else: 
                print(" book not in the system ")
        elif user_choice == "3":
            book_title = input("Enter book title: ")
            found = book.search_by_field(book_title, 2)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "4":
            pub_year = input("Enter publication year: ")
            found = book.search_by_field(pub_year, 3)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "5":
            genre = input("Enter book genre: ")
            found = book.search_by_field(genre, 4)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "6":
                edition = input("Enter book edition: ")

                found = book.search_by_field(edition, 5)
                if found:
                    print("Book found.")
                else:
                    print("Book not found.")
        elif user_choice == "7":
            quantity = input("Enter book quantity: ")
            found = book.search_by_field(quantity, 6)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "8":
            print("Exiting...")
            break
        else: 
            print("Invalid choice. please enter a valid choice ")

main() 

