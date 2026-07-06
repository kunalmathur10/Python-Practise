# q1:Second Largest
# Sol:
def second_largest(nums):
    largest = float("-inf")
    second_largest = float("-inf")
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
List = [25,25,47,63,97,93]
print(second_largest(List))

# q2: Remove Duplicates
# Sol:
def rem_duplicates(nums):
    freq={}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    return list(freq.keys())

List = [25,25,47,63,97,93,96,97,93,62]
print(rem_duplicates(List))

# q3:Find Duplicate Elements
# sol:
def duplicate(nums):
    freq={}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    duplicate = [(key)for key in freq if freq[key] > 1]
    return duplicate
List = [25,25,47,63,97,93,96,97,93,62]
print(duplicate(List))

# q4:Pair with Target Sum (Two Sum)
# Sol:
def two_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
List = [25,25,47,63,97,93,96,97,93,62]
target = 72
print(two_sum(List, target))

# q5:Frequency of Elements
# Sol:
def freq_elements(sentence):
    freq = {}
    for element in sentence.lower().split():
        freq[element] = freq.get(element, 0) + 1
    return freq

love = "The Cat and the dog played and the cat slept while the dog barked"
print(freq_elements(love))