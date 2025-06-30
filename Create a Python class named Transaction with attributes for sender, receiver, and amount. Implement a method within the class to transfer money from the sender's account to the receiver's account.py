class Transaction:
    def __init__ (self, sender, receiver, amount): 
        self.sender = sender
        self.receiver = receiver 
        self.amount = amount
    def transfer(self, accounts): 
        """
        Transfers money from the sender's account to the receiver's account.
        :param accounts: Dictionary holding account balances for allusers.
        """
        if self.sender not in accounts:
            print(f"Error: Sender '{self.sender}' does not exist.") 
            return
        if self.receiver not in accounts:
            print(f"Error: Receiver '{self.receiver}' does not exist.") 
            return
        if accounts[self.sender] < self.amount:
            print(f"Error: Insufficient funds in sender '{self.sender}' account.")
            return
        
        # Perform the transfer 
        accounts[self.sender] -= self.amount 
        accounts[self.receiver] += self.amount
        print(f"Transfer successful: {self.amount} transferred from {self.sender} to {self.receiver}.")
        # Example usage
        if __name__ == " main ":
        # Sample account balances 
            accounts = {
            "Alice": 5000,
            "Bob": 3000,
            "Charlie": 7000,
            }
            # Display initial account balances
            print("Initial account balances:")
            for user, balance in accounts.items(): 
                print(f"{user}: {balance}")
            # Create and perform a transaction
            transaction = Transaction("Alice", "Bob", 1500) 
            transaction.transfer(accounts)
            # Display updated account balances 
            print("\nUpdated account balances:") 
            for user, balance in accounts.items():
                print(f"{user}: {balance}")