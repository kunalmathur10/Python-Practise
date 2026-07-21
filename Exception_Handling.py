# Definition: An exception is a runtime event which interupts the normal flow of program. Exception handling allow us to handle such errors gracefully without terminating the program.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Divide nahi hoga")
# The upper code gives value Error, if enter abc in place of number so the correct version is :


try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Divide nahi hoga")
except ValueError:
    print("Enter valid integers")

try:
    print(10/0)
except Exception:
    print("Exception")
except ZeroDivisionError:
    print("Zero")

# This codes gives syntax error because exception is a parent class of all exceptions, it catches the error before the more specific handlers, so it will comes comes in last, so the correct code is :
try:
    print(10/0)
except ZeroDivisionError:
    print("Zero")
except Exception:
    print("Exception")

# Else concept: the else block exceute when no exception occurs in try block.

try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    result = a/b
except ZeroDivisionError:
    print("Divide nahi hoga")
except ValueError:
    print("Enter valid integers")
else:
    print(result)

#  Finally: The finally block always executed whether exception occurs or not. It is mainly used for cleaning activities like closing file, database connections etc.
# try
# ↓

# except (agar error aaya)

# ↓

# else (agar error nahi aaya)

# ↓

# finally (hamesha)

def test():
    try:
        return "Hello"
    finally:
        print("Finally executed")
x= test()
print(x)
print(test())
# In the above function firstly finally executed and return execute.

def test():
    try:
        return 10
    finally:
        return 20
print(test())
# The above codr returns 20 because firstly function return 10 THEN IT EXecuted finally in which return overwrites the above return it wil give the value 20.

# Raise: The raise statement is used when we manually throw an exception when the specific condition or business rule is violated. 

try:
    age = int(input("Enter the age here: "))
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as e:
    print(e)
print("Program Finished")

salary = -5000

if salary < 0:
    raise ValueError("Salary cannot be negative")

print("Salary Accepted")