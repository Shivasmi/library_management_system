
import csv

class Book:
    def __init__(self, book_id, author_name, title, pub_year, genre, edition, quantity):
        self.book_id = book_id
        self.author_name = author_name
        self.title = title
        self.pub_year = pub_year
        self.genre = genre 
        self.edition = edition
        self.quantity = quantity
    
    # def __write_csv_file(book_data):
    #     with open("book_data.csv", "w", newlines =' ') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(book_data)
   
    def add_book(self):
            book_id = input("Enter book ID: ")
            author_name = input("Enter author name: ")
            title = input("Enter book title: ")
            pub_year = input("Enter publication year: ")
            genre = input("Enter book genre: ")
            edition = input("Enter book edition: ")
            quantity = input("Enter book quantity: ")

            
            book_data = f"{book_id},{author_name},{title},{pub_year},{genre},{edition},{quantity}\n"
            found = self.search_book_by_title(self.title)
            if not found:
                with open("book_data.csv", "a") as file:
                    file.write(book_data)
                print("Book added successfully!")
            else:
                print("Book already exists ")



    def search_book_by_author(self, author_name):
        found = False
        with open("book_data.csv", "r") as file:
            
            for line in file: 
                book_info = line.strip().split(",")
                if book_info[2] == author_name:
                    found = True 
                    return found 
                
            if not found:
                return found 
            

    def search_book_by_title(self, title):
        found = False
        with open ("book_data.csv", "r" ) as file:
            for line in file:
                book_info = line.strip().split(",")
                if book_info == title:
                    found = True
                    return found 
            
            if not found:
                return found
                
    def search_book_by_pub_year(self, pub_year):
        found =False
        with open("book_data.csv", "r" ) as file: 
            for line in file: 
                book_info = line.strip().split(",")
                if book_info == pub_year:
                    found = True
                    return found
            if not found: 
                return found

    def search_book_by_genre(self, genre):
        found = False
        with open ("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                if book_info == genre:
                    found = True
                    return found 
                
            if not found:
                return found
    def search_book_edition (self, edition):
        found = False
        with open ("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                if book_info == edition:
                    found = True
                    return found 
            if not found: 
                return found
            
    def search_quantity( self, quantity):
        found = False
        with open ("book_data.csv", "r") as file:
            for line in file: 
                book_info = line.strip().split(",")
                if book_info == quantity:
                    found = True
                    return found 
            if not found:
                return found
            

def main(): 
    book = Book('book_id', 'author_name', 'title', 'pub_year', 'genre', 'edition', 'quantity')
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
            found = book.search_book_by_author(author_name)
            if found:
                print (" Book found ")
            else: 
                print(" book not in the system ")
        elif user_choice == "3":
            title = input("Enter book title: ")
            found = book.search_book_by_title(title)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "4":
            pub_year = input("Enter publication year: ")
            found = book.search_book_by_pub_year(pub_year)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "5":
            genre = input("Enter book genre: ")
            found = book.search_book_by_genre(genre)
            if found:
                print("Book found.")
            else:
                print("Book not found.")
        elif user_choice == "6":
                edition = input("Enter book edition: ")

                found = book.search_book_by_edition(edition)
                if found:
                    print("Book found.")
                else:
                    print("Book not found.")
        elif user_choice == "7":
            quantity = input("Enter book quantity: ")
            found = book.search_book_by_quantity(quantity)
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

