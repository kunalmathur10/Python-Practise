# q1: Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True
num = int(input("Enter the number here: "))
if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is a not a Prime Number")

# q2: Find Factorial
# Sol:
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
num = int(input("Enter the number here: "))
print(factorial(num))

# q3: Fibonacci Series
# sol:
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a, end ="")
        a,b = b, a+b

num = int(input("Enter the number here: "))
print(fibonacci(num))

# q4:Palindrome
# Sol:
def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False
num = int(input("Enter the number here: "))       
if is_palindrome(num):
    print("It is palindrome")
else:
    print("Not Palindrome")
