# Generator: ek special type ka python function jo yield keyword ko use karta hai aur ek saath saari values memory me story nhi karta. Ye values ko ek ek karke generate karta hai.
#  It is a special python function which uses yield keyword to produce values one at a time instead of returning all values at once. This makes it more memory efficient, and use with large datasets.

# Example :
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# num = numbers()
# print(next(num))

# q1: Make a generator which gives number from 1 to 5:
# Sol:
# def counting():
#     for i in range(1,6):
#         yield i
# genrator = counting()
# for num in genrator:
#     print(num)

# q2: Even number generator 
# Sol:
# def even_num(n):
#     for i in range(2, n+1, 2):
#         yield i
# even = even_num(10)
# for num in even:
#     print(num)

# q3: Number whichis divisible by 3
# Sol:
# def divi_3(n):
#     for i in range(3, n+1, 3):
#         yield i
# nums = divi_3(45)
# for num in nums:
#     print(num)

# q4: 