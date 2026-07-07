# Decorators: Decorator ek function hota hai jo kisi dusre function ki functionality ko modify 
# ya extend karta hai bina uske original code ko change kiye.
# Decorator likho jo:

# "Welcome" print kare.
# Original function execute kare.
# "Good Bye" print kare.

def decorator(func):
    def wrapper(a, b):
        print("Welcome")
        addition = func(a, b)
        print("Good Bye")
        return addition
    return wrapper
@decorator
def greetings(a, b):
    return a+b
# greetings = decorator(greetings)
print(greetings(3,5))

# usings *args, **kwargs
# *args gives result in tuple, while **kwargs gives result in dictionary
def decorator(func):
    def wrapper(*args, **kwargs):
        print("WelCome hAi Ji")
        result = func(*args, **kwargs)
        print("Thank You for being patient")
        return result
    return wrapper
@decorator
def addition(*args, **kwargs):
    # total = 0
    # for i in args:
    #     total += i
    return sum(args)
print(addition(10,20,70,100))

def decorator(func):
    def wrapper(*args, **kwargs):
        print("WelCome hAi Ji")
        result = func(*args, **kwargs)
        print("Thank You for being patient")
        return result
    return wrapper
@decorator
def addition(*args, **kwargs):
    return kwargs
print(addition(name = "Kunal", city = "Mumbai"))

#  Authentication Decorator 
# Sol:
is_logged_in = True
def authentication_req(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper
@authentication_req
def view_profile(*args, **kwargs):
    print("Displaying your Profile")
view_profile()


