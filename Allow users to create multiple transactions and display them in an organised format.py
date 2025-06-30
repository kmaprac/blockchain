from tabulate import tabulate
# Function to add a transaction
def add_transaction(transactions, transaction_id, description, amount): 
    transactions.append({"ID": transaction_id, "Description": description,"Amount": amount})

# Display transactions in a tabular format 
def display_transactions(transactions):
    headers = ["Transaction ID", "Description", "Amount"] 
    table = [[t["ID"], t["Description"], t["Amount"]] for t in transactions]
    print(tabulate(table, headers, tablefmt="grid"))

# Main program 
def main():
    transactions = [] # List to store transactions 
    print("Welcome to the Secure Messaging Transaction System!")
    while True:
        print("\nOptions: ") 
        print("1. Add Transaction")
        print("2. Display Transactions") 
        print("3. Exit")
        choice = input("\nEnter your choice (1/2/3): ") 
        if choice == "1":
            transaction_id = input("Enter Transaction ID: ") 
            description = input("Enter Description: ") 
            amount = float(input("Enter Amount: "))
            add_transaction(transactions, transaction_id, description, amount)
            print("Transaction added successfully!") 
        elif choice == "2":
            if transactions: 
                display_transactions(transactions)
            else:print("No transactions to display!") 
        elif choice == "3":
            print("Exiting... Goodbye!") 
            break
        else:
            print("Invalid choice. Please select again.")

# Run the program
# if __name__ == " main ": 
main()
