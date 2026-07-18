# Inheritance: Means code is taken from the parent class if its repeating in the child class.
# Inheritance matlab virasat
# Diffrent terms:
# 1- Method Lookup:
class Animal:
    def sleep(self):
        print("Sleeping")
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d = Dog()
d.eat()
# d object didnt find the methodin the dog class so it find that method in Animal class which is inherited class this is called the "Method Lookup"

# 2- Super(): meaning of super is, it says firstly run the constructor of parent class then the child class. ""Pehle Parent ka constructor chala do.""
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Sleeping")
        
# Single Level Inheritance: One parent class and one child class
class Animal:
    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    pass

# Multiple Inheritance:
class Father:
    def play(self):
        print("Playing")
class Mother:
    def cook(self):
        print("Cooking")

class Son(Father, Mother):
    pass

# q1: Employee → Manager create a employee class
# Sol: 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
     def __init__(self, name, salary, department):
         super().__init__(name, salary)
         self.department = department
     def display(self):
         super().display()
         print(f"Department: {self.department}")
m = Manager("Kunal", 50000, "Data Science")
m.display()

# q2: BankAccount → SavingsAccount
# Sol:
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than 0")
            return
        self.balance += amount
        print(f"Rs.{amount} deposited successfully, Available Balance: Rs.{self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than 0")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs.{amount} withdrawal successfully, Available Balance: Rs.{self.balance}")
        else:
            print("Insufficient Balance")
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest
        print(f"Available Balance: Rs.{self.balance}")
        return self.balance

    


