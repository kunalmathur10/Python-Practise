# q1: Square using Lambda
# Sol:
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def square(num):
    result = (lambda x: x ** 2)  
    return (result(num))

print(square(5))

# q2: Sort using Lambda
# Sol:
def sort(num):
    result = lambda x: sorted(x)
    return result(num)
data = [1,2,15,3,4,5,6,17,18,19,20,8,9,16,10,11,12,13,14]
print(sort(data))
# or for dictionary
def dictionary_sort(data, by = "Key", reverse = False):
    if by == "key":
        return dict(sorted(data.items(), key = lambda x: x[0], reverse = reverse))
    elif by == "value":
        return dict(sorted(data.items(), key = lambda x: x[1], reverse = reverse))
    else:
        return "the data is not valid"
student = {
    "Rahul": 85,
    "Kunal": 95,
    "Aman": 78,
    "Rohit": 90
}

# print(dictionary_sort(student, by="key"))
# print(dictionary_sort(student, by="value"))
print(dictionary_sort(student, by="value",reverse=True))

# q3: using map function
# Sol:
def usecase(data):
   return list(map(lambda x:x*x, data ))
data = [1,2,15,3,4,5,6,17,18,19,20,8,9,16,10,11,12,13,14]
print(usecase(data))
#  Add two lists element-wise using map() and lambda.
# sol:
def two_list_sum(first, second):
   return list(map(lambda x, y: x+y, first, second))
first = [1,2,15,3,4,5,6,17,18,19,20,8,9,16,10,11,12,13,14]
second= [1,2,15,3,4,5,6,17,18,19,20,8,9,16,10,11]
print(two_list_sum(first, second))

# Add two dictionaries using map function 
# Sol:
def dictionary_add(first, second):
    return dict(map(lambda x, y: (x[0], x[1] + y[1]), first.items(), second.items()))

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "A": 5,
    "B": 15,
    "C": 25
}
print(dictionary_add(dict1, dict2))

# q4: using filter 
def filtered_results(data):
    return list(filter(lambda x: x%2 == 0, data))
data = [1,2,15,3,4,5,6,17,18,19,20,8,9,16,10,11,12,13,14]
print(filtered_results(data))

# Find Words Longer Than 5 Characters
def characters_len(data):
    return list(filter(lambda x: len(x) > 5, data))

words = ["Python", "Java", "SQL", "Machine", "AI"]
print(characters_len(words))

# Filter Employees Having Salary
# Sol:
def filtered_salary(data):
    return list(filter(lambda x: x["salary"] >= 50000, data))
employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Kunal", "salary": 80000},
    {"name": "Aman", "salary": 45000},
    {"name": "Rohit", "salary": 70000}
]

print(filtered_salary(employees))

# q5: reduce function 
# sol:
from functools import reduce
def red_usecase(data):
    return (reduce (lambda x, y: x+y, data))
salary = [100,123,125,145,16,125,456,147]
print(red_usecase(salary))


