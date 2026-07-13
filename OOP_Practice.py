# q1: Create student class
# Sol:
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"grade: {self.grade}")

student1 = Student("Aman", 15, "A")
student1.display()
student2 = Student("Varun", 14, "C")
student2.display()

# q2: Create Employee Class
# Sol:
class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def annual_salary(self):
        return self.salary * 12

employee1 = Employee("Rahul", 50000, "HR")
employee1.display()
employee2 = Employee("Kunal", 80000, "Data Science")
employee2.display()
print(employee2.annual_salary())

# q3: Bank Account Class:
# Sol:
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount<=0:
            print("Deposit amount should be greater then 0")
            return
        self.balance += amount
        print(f"Rs. {amount} deposited successfully , Balance: Rs. {self.balance}")
        return self.balance
        
    
    def withdraw(self, amount):
        if amount <=0:
            print("Withdraw amount must be greater than 0")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} Withdrawl successful, Balance is Rs. {self.balance}")
            return self.balance
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Current Balance : Rs. {self.balance}")
        return self.balance
BankAccount1 = BankAccount("Arvind", 200000)
# BankAccount1.withdraw(300000)
BankAccount1.deposit(10000)