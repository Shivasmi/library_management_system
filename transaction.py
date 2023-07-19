

import csv 
from datetime import datetime
class Transaction:
    def __init__(self, book_title, member_id, borrow_date, expected_return_date, actual_return_date):
        self.book_title = book_title
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.expected_return_date = expected_return_date
        self.actual_return_date = actual_return_date

   
    #Record the transaction in a csv file
    def record_transaction(self):
        transaction_data = [self.book_title, self.member_id, self.borrow_date, self.expected_return_date, self.actual_return_date]
        with open('transaction_data.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(transaction_data)
            print("You have successfully Borrowed a Book")
            #After Borrowed Successfully, Decrease Quantity on book data
            # Decrease quantity in book_data.csv by 1
        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[2] == self.book_title:
                if int(row[6]) > 0:
                    row[6] = str(int(row[6]) - 1)
                    break
            
        with open('book_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("Quantity updated successfully!")

    #record for book return transaction
    def return_date_transaction (self):
        return_data = [self.book_title, self.member_id, self.borrow_date, self.expected_return_date, self.actual_return_date]
        with open('transaction_data.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(return_data)
        
            print(" you have sucessfully return your borrowered bood on {return_data} ")
            #After borrowed sucessfully returned, increase quantity on book_data.csv by 1
           
        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[2] == self.book_title:
                if int(row[6]) > 0:
                    row[6] = str(int(row[6])+1)
                    break
        with open('book_data.csv', 'w', newline = '') as file: 
            writer = csv,writer(file)
            writer.writerows(rows)
            print(" Quantity have been updated after sucessfuly returned book in actual date have completed ")

    
    def search_transaction_by_field_name(self, field_name, index):
        found = False
        with open("transaction_data.csv", 'r' ) as file: 
            for line in file: 
                transaction_info = line.strip().split(",")
                if transaction_info[index] == field_name:
                    found = True
                    return found
            return found 

def main():
    transaction = Transaction ('book_title', 'member_id', 'borrow_date', 'expected_return_date', 'actual_return_date' )
    while True:
        print ("\n -----Transaction------")
        print ("1. add record of book borrower transaction  ")
        print ("2. add record of book return transaction ")
        print ("3. add record of member id login transaction ")
        print ("0. for exiting from the programm ")

        choice = input ("enter your choice: (1-3): " )
        borrow_date = datetime.now().strftime("%d/%m/%y")
        if choice == '1':
            book_title = input("enter the book title: ")
            member_id = int(input("enter your memeber id: "))
            borrow_date = int(input("enter the borrower date  in dd/mm/yy format:" ))
            expected_return_date = int(input("enter the date you expected to return the book in dd/mm/yy format: "))
            actual_return_date = int (input("enter the actual date you have return in dd/mm/yy format: "))

            transaction = Transaction (book_title, member_id, borrow_date, expected_return_date, actual_return_date)
            transaction.record_transaction()
            print("Transaction Add sucessfully" )

        elif choice == '2':
            
            book_title = input("enter the book title: ")
            member_id = int(input("enter your memeber id "))
            borrow_date = int(input("enter the date you borrow the book: "))
            expected_return_date = int(input ("enter the date you expected to return the book in dd/mm/yy format: "))
            actual_return_date = int (input("enter the date actual date you have return in dd/mm/yy format: "))

            transaction = Transaction (book_title, member_id, borrow_date, expected_return_date, actual_return_date)
            transaction.record_transaction()
            print("Transaction Add sucessfully" )

        elif choice == '3':
            member_id = input(" enter the memeber id of the transaction ")
            transaction = transaction.search_transaction_by_field_name(member_id)
            if transaction:
                print(" Transaction Found " )
            else: 
               return None
                
        elif choice == '0':
            print("exiting the program ")
            break
        else: 
            print (" invalid choice, please try agin ")

main()




            


                                           

                   




        

    
