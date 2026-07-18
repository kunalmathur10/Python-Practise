class ATM:

    def __init__(self, account_holder, account_number, pin, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def login(self, entered_pin):
        entered_pin = int(input("Enter your pin here"))
        if entered_pin == self.pin:
            print("Login successful")
            self.display_menu()
        else:
            print("Invalid pin")

    def pin(self, pin):
        self.pin = pin
        return self.pin
    
    def menu(self):
        pass
    
    def deposit(self, amount):
        if amount <=0:
            print("Enter valid amount")
            return
        self.balance += amount
        print(f"₹{amount} deposited successfully, Balance: ₹{self.balance}")
        return self.balance
    
    def withdrawal(self, amount):
        if amount <= 0:
            print("Withdraw valid amount")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawl successfully, Balance: ₹{self.balance}")
            return self.balance
        else:
            print("Insufficient Balance")

    def display(self):
        self.account_holder
        self.account_number
    
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        return self.balance

    

    




