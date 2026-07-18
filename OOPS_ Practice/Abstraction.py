# Definition: Abstraction means hiding implementation details and exposing only the essential functionalities to the user.
# User ko sirf kaam dikhana, implementation chhupa dena.

# q1: Create anabstract class shape
# sol:
from abc import ABC, abstractmethod
import math
class Shape(ABC):

    @abstractmethod

    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        area_rect = self.length * self.breadth
        print(f"Area of rectangle: {area_rect}")
        return area_rect
    
    def perimeter(self):
        peri_rect = 2*(self.length + self.breadth)
        print(f"Perimeter of rectangle: {peri_rect}")
        return peri_rect

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
            
    def area(self):
        cir_area = math.pi * self.radius ** 2
        print(f"Area of circle: {cir_area}")
        return cir_area
        
    def perimeter(self):
        cir_peri = 2 * math.pi * self.radius
        print(f"Perimeter of circle is: {cir_peri}")
        return cir_peri
r = Rectangle(12, 25)
r.area()
r.perimeter()

c = Circle(10)
c.area()
c.perimeter()
        
# q2: Create abstract class payment
# Sol:
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment is successful")

class CreditCard(Payment):
    def pay(self):
        print("Credit Card payment is successful")

class NetBanking(Payment):
    def pay(self):
        print("Payment using NetBanking is successful")

upi = UPI()
upi.pay()