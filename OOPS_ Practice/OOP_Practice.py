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

# Encapsulation: 
# q1: Create a student class using encapsulation:
# Sol: 
class Students:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
s1 = Students(90)
print(s1.get_marks())
s1.__marks

# Question 4 (Interview Level) ⭐⭐⭐⭐
# Problem

# ATM System

# Requirements

# Private Variables

# __pin

# __balance

# Methods

# change_pin()

# deposit()

# withdraw()

# check_balance()

# Conditions

# Wrong PIN → Access Denied
# Correct PIN → Transaction

# Sol;
class ATM:

    def __init__(self):
        self.__pin = 123456
        self.__balance = 50000
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Invalid Pin" )

    def deposit(self, pin, amount):
        if pin == self.__pin:
            if amount > 0:
                self.__balance += amount
                print(f"₹{amount} has been deposited successfully")
                print(f"Available Balance: ₹{self.__balance}")
            else:
                print("Deposit amount must be greater than 0")
        else:
            print("Invalid Pin")

    def withdraw(self,pin,amount):
        if pin == self.__pin:
            if amount > 0:
                if amount <= self.__balance:
                    self.__balance -= amount
                    print(f"₹{amount} has been withdrawal successfully")
                    print(f"Available Balance: ₹{self.__balance}")
                else:
                    print("Insufficient Balance")
            else:
                print("Withdraw amount must be greater than 0")
        else:
            print("Invalid Pin")

    def check_balance(self, pin):
        if pin == self.__pin:
            print(f"Available Balance: ₹{self.__balance}")
        else:
            print("Invalid Pin")
X = ATM()
X.change_pin(123456, 3456)
X.withdraw(3456, 5000)
X.deposit(3456, 5000)
X.check_balance(3456)
# X.__pin
# Internal change in private variable like this thats why we cant access private variable
# print(X._ATM__balance) internally python aise bna deta hai private variable but 
# techically apan isko access kar sakte hai
