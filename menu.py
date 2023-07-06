import csv 
import books
import borrowers



def add_user():
    name = input("enter your full legal name: ")
    address = input ("enter your full address ")
    phone = input (" enter your phone number ")
    email = input (" enter your email ")
    user_data = f"{name},{address},{phone},{email} "
    with open("user_data.csv", "a" ) as file:
        file.write(user_data)
    print("User added sucessfully")


def Admin_menu():
    print (" Welcome to  Admin Menu ")
    print("1. Add a new user")
    print("2. Add a new book")
    print("3. Update book information")
    print("4. Remove a book")
    print("5. Remove a user")
    print("6. Exit")

       
    admin_choice = int(input("enter your choice "))
    if admin_choice == 1:
        print( "Add a new user")
        name = input("enter your full legal name: ")
        address = input ("enter your full address ")
        phone = input (" enter your phone number ")
        email = input (" enter your email ")
        user_data = f"{name},{address},{phone},{email} "
        with open("user_data.csv", "a" ) as file:
            file.write(user_data)
        print("User added sucessfully")
        
    elif admin_choice ==2:
        print("add a new book")
        
    elif admin_choice ==3:
        print( "update the book information ")
    elif admin_choice == 4: 
        print (" remove a book " )
    elif admin_choice == 5: 
        print (" remove a user " )
    else: 
        print (" exit from the menu " )
   


def borrower_menu():
        print("Borrower Menu")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Update personal information")
        print("4. Cancel membership")
        print("5. Exit")

        borrower_choice = int(input("enter your choice"))
        
        if borrower_choice == 1: 
            print (" Borrow a book ")
        elif borrower_choice ==2: 
            print ("Return a book ")
        elif borrower_choice ==3:
            print("update personal information ")
        elif borrower_choice == 4: 
            print ("your membership will be cancel memebership in 24 hours  ")
        else: 
            print ( "Wrong input, Try again with right choice ")
       

def main_menu():
        print("Welcome to AS Library Management System")  
        print("Please enter your choice to contiue ")
        print (" 1. Admin Menu ")
        print (" 2. Borrower Menu ")

        user_choice = int(input("Choose the number as per your role: 1 For Admin Menu, 2 for Borrower Menu "))
        if user_choice == 1:
            Admin_menu()
        elif user_choice == 2: 
            borrower_menu()
        else: 
            print (" Please enter a valid input from menu ")



admin_data = ["Added a new user", "Add a book", "Update Book Information", "Remove a book", "Remove a user"]
borrower_data = ["Borrow a book", "Return a book", "Update Personal Information", "Revoke Membership"]

filename = 'data_storage.csv'
def write_csv_file(data_storage, admin_data, borrower_data):
        with open(data_storage, "w", newline= '') as file: 
            writer = csv.writer(file)
            writer.writerows(admin_data)
            writer.writerows(borrower_data)

write_csv_file(filename, admin_data, borrower_data)

print(f" CSV file '{filename}' add in the data storage ")

main_menu()
