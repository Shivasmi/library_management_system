import csv

class Borrowers:
    def __init__(self, borrower_id, name, address, phone, email):
        self.borrower_id = borrower_id
        self.name = name 
        self.phone = phone 
        self.address = address
        self.email = email
    
    
    def add_borrower_details(self, borrower_id):
        borrower_id = input("enter bowworer_id  " )
        name = input (" enter full name of the borrower  ")
        address = input (" enter full address  " )
        phone = input (" enter phone number  ")
        email = input (" enter email ")
        found = False
        borrower_data = f"{borrower_id}, {name}, {address},{phone}, {email}\n"
        if not found: 
            with open ("borrower_data.csv ", "a") as file:
                file.write(borrower_data)
            print(" user added sucessfully ")
        else: 
            print( " Borrowers already exit")

    def search_by_name(self, name):
        name = input("enter a valid name " )
        found = False
        with open("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split(",")
                if borrower_info[1] == name:
                    found = True
                    return found 
            if not found:
                print ("User name not found ")

    def search_by_address(self, address):
        address = input ( " enter a valid address")
        found = False
        with open ("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split(",")
                if borrower_info[2] == address:
                    found = True
                    return found
            if not found:
                print (" address didn't matched, try again" )

            

    def search_by_phone(self, phone):
        phone = input( " enter a phone number ")
        found = False
        with open ("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split(",")
                if borrower_info[3] == phone:
                    found = True
                    return found
            if not found:
                print ("phone Number didn't matched, try again ")

    def search_by_email(self, email):
        email = input(" enter a valid email" )
        found = False
        with open ("borrower_data.csv", "r") as file:
            for line in file: 
                borrower_info = line.strip().split(",")
                if borrower_info[4] == email:
                    found = True
                    return found 
                if not found:
                    print ("email didn't match up, please enter try again")


def main():
    borrower = Borrowers('borrower_id', 'name', 'address', 'phone', 'email')
    while True:
        print("\n Enter your choice  ")
        print ("1. add borrowers details ")
        print ("2. search by name ")
        print ("3. search by address ")
        print ("4. search by phone ")
        print ("5. search by email ")
        print ("6. Exit")

        user_choice = input("Enter your choice (1-6): ")

        if user_choice == "1":
            borrower.add_borrower_details("borrower_id")
        elif user_choice == "2":
            borrower.search_by_name('name')
        elif user_choice == "3":
            borrower.search_by_address("address")
        elif user_choice == "4":
            borrower.search_by_phone("phone")
        elif user_choice == "5":
            borrower.search_by_email("email")
        elif user_choice == "6":
            print(" exit " )
            break
        else: 
                print("Invalid choice. please enter a valid choice ")

main()
