# Iterator is a object which provides the facility to access the elements one by one from the data.
# With the help of next function (next()), it returns the next elements
# Iterator ke 2 Important Methods
# iter() → Iterator object banata hai.
# next() → Next return the value.

# example
# data = [10,20,30,40,50]
# itr = iter(data)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# q2: By using the iterator print all the elements of list without using for loop
# Sol:
data = [10,20,30,40,50]
itr = iter(data)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break