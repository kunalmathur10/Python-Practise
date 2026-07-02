# q1: Print 1-10
# Sol:
for i in range(1,11):
    print(i)
# q2: print even numbers from 1 to 100 :
#  Sol:
for i in range(1,100):
    if i%2==0:
        print(i)
    # OR
for i in range(2,100,2):
    print(i)

# q3:Find sum of numbers from 1 to 100
# Sol:
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

# q4: Count how many numbers are divisible by 3 between 1 and 50
# Sol:
count = 0
for i in range(1,51):
    if i%3==0:
        count += 1
print(count)   
    #  or Optimize solution
count = 0
for i in range(3,51,3):
    count += 1
print(count)

# q5: Find largest element in a list
# Sol:
nums = [12, 45, 3, 67, 23]
largest = 0
for i in nums:
    if i > largest:
        largest = i
print("Largest number is", largest)
# Optimize solution
nums = [12, 45, 3, 67, 23]
largest = max(nums)
print(largest)

# q6: Find second largest element in a list
# Sol:
nums = [12, 45, 3, 67, 23]
largest = float("-inf")
second_largest = float("-inf")
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest is", second_largest)
#  OR
import heapq
nums = [12, 45, 3, 67, 23]
second_large = heapq.nlargest(2, list(set(nums)))[1]
print(second_large)

# q7: Count frequency of each character
# Sol:
word = "successful"
freq ={}
for ch in word:
    if ch in freq:
        freq[ch] = freq[ch]+ 1
    else:
        freq[ch] = 1
print(freq)
# Optimise version
word = "rudraa"
freq = {}
for ch in word:
    freq[ch]= freq.get(ch,0) + 1
print(freq)

# q8: Reverse a string using a loop
# Sol:
word = "kunal"
rev = ""
for i in word:
    rev = i + rev
print(rev)
# Optmise version
word = "varun"
print(word[::-1])

# q9: Check whether a number is prime or not
# Sol:
num = 23
# num = int(input())

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

# q10: Remove duplicates without using set()
# Sol:
nums = [1,2,2,3,3,4,5]
uni= []
freq= {}
for num in nums:
    if num in freq:
        freq[num] = freq[num]+1
    else:
        freq[num] = 1
for key in freq:
    if freq[key] == 1:
        uni.append(key)
print(uni)

# Optimise version
nums = [1,2,2,3,3,4,5]
uni= []
freq= {}
for num in nums:
    freq[num] = freq.get(num,0) + 1
uni = [(key)for key in freq if freq[key] == 1]
print(uni)

# q11 Find all pairs whose sum equals target
nums = [2,7,11,15,3,8]
target = 10
# Sol:
seen = set()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i],nums[j])
# Optimise version
nums = [2,7,11,15,3,8]
target = 10
seen = set()
for num in nums:
    complement = target - num
    if complement in seen:
        print(complement, num)
    seen.add(num)
