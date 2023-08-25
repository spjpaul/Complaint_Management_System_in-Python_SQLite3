import sqlite3
from prettytable import PrettyTable


# Function to create the complaints table in the database
def create_table():
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Customer_name TEXT NOT NULL,
            Customer_email TEXT NOT NULL,
            Address TEXT NOT NULL,
            City TEXT NOT NULL,
            Country TEXT NOT NULL,
            Pincode INTEGER,
            Mobile_Number INTEGER,
            Category TEXT NOT NULL,
            Service Text NOT NULL,
            TXN_ID_Account_No TEXT NOT NULL,
            Date_of_Transaction DATE,
            Branch TEXT NOT NULL 
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a new complaint to the database
def add_complaint(Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch):
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO complaints (Customer_name, Customer_email, Address, City, Country, Pincode, 
    Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 
    ?, ?, ?, ?)''', (Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category,
    Service, TXN_ID_Account_No, Date_of_Transaction, Branch))

    conn.commit()
    conn.close()

# Function to view all complaints in the database
def view_complaints():
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch FROM complaints')
    complaints = cursor.fetchall()

    conn.close()
    #to show the complaints

    if not complaints:
        return None

    return complaints

   #to Show the above return complaints in SQL Table like format
    #table = PrettyTable()
    #table.field_names = ["ID", "Customer Name", "Customer Email", "Address", "City", "Country", "Pincode",
                        # "Mobile Number", "Category", "Service", "TXN/Account No", "Date of Transaction", "Branch"]

    # Add the complaints data to the table
    #for complaint in complaints:
    #    table.add_row(complaint)

    # Print the table
    #print(table)


# Main function to run the complaints management system
def main():
    create_table()
#Main Menu
    while True:
        print("\n Welcome to JP Bergs Complaints Management System")
        print("1. To Register New Complaint")
        print("2. View Existing Complaints")
        print("3. Exit")

        pref = input("Enter your Preference (1/2/3): ")
      # Adding Customer details for new complaint registration,

        if pref == '1':
            Customer_name = input("Enter your Name: ")
            Customer_email = input("Enter your email: ")
            Address = input("Enter your Address: ")
            City = input("Enter your City: ")
            Country = input("Enter your Country: ")
            Pincode = input("Enter Pincode: ")
            Mobile_Number = input("Enter your Mobile Number: ")
            # Entering the Type and Sub type details
            print("\nType of Category")
            print("1. Financial Services")
            print("2. Insurance")
            print("3. Admin")
            print("4. Others")
            Category = input("Enter your Category (1/2/3): ")
            if Category =='1':
                    print("\nSelect Type of Service")
                    print("1. General Banking")
                    print("2. ATM")
                    print("3. e-Banking")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '2':
                    print("\nSelect Type of Service")
                    print("1. New Policy")
                    print("2. Online Payment Issues")
                    print("3. Agent Potral")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '3':
                    print("\nSelect Type of Service")
                    print("1. Delay in Settlement of Complaints")
                    print("2. Deficiency in Service")
                    print("3. Staff Rude Behaviour")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '4':
                    print("Please obtain complaint and forward to the email ID :crmmgr@jpb.com")
                    break
            else:
                    print("Exiting the complaints management system.")
                    break
            TXN_ID_Account_No = input("Enter the Transaction Number or Account Number: ")
            Date_of_Transaction = input("Enter the date of Transaction: ")
            Branch = input("Enter the Branch Name: ")

            add_complaint(Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch)
            print("Complaint added successfully!")
        # To view complaints
        elif pref == '2':
            complaints = view_complaints()

            #if not complaints:
            if complaints is None:
                print("No complaints found.")  # Moved this line here
            else:
                print("\nAll Complaints:")
                table = PrettyTable()
                table.field_names = ["ID", "Customer Name", "Customer Email", "Address", "City", "Country", "Pincode",
                                     "Mobile Number", "Category", "Service", "TXN/Account No", "Date of Transaction",
                                     "Branch"]

                for complaint in complaints:
                    table.add_row(complaint)

                print(table)
                #for complaint in complaints:
                    #print(f"ID: {complaint[0]}, Customer_name: {complaint[1]}, Customer_email: {complaint[2]}, Address: {complaint[3]}, City: {complaint[4]}, Country:{complaint[5]}, Pincode: {complaint[6]}, Mobile_Number: {complaint[7]}, Category: {complaint[8]}, Service: {complaint[9]}, TXN_ID_Account_No:{complaint[10]},Date_of_Transaction:{complaint[11]},Branch: {complaint[12]}")
# for exiting the complaints portal
        elif pref == '3':
            print("Exiting the complaints management system.")
            break
#Error in Entry
        else:
            print("Invalid choice. Please try again.")
# Main Iteration
if __name__ == "__main__":
    main()
