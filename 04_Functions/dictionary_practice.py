# q1: Word Frequency
# Sol:
def word_freq(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word,0) + 1
    return freq
sentence = "python is easy and python is powerful python is used for data science machine learning web development automation and data analysis data science uses python because python has many libraries data analysis requires pandas pandas makes data analysis easy machine learning requires scikit learn and python helps developers build better applications with practice practice improves coding and practice improves problem solving"
print(word_freq(sentence))

# q2: Character Frequency
# Sol:
def char_freq(sentence):
    freq = {}
    for words in sentence.lower().split():
        for ch in words:
            freq[ch] = freq.get(ch,0) + 1
    return freq

sentence = "python is easy and python is powerful python is used for data science machine learning web development automation and data analysis data science uses python because python has many libraries data analysis requires pandas pandas makes data analysis easy machine learning requires scikit learn and python helps developers build better applications with practice practice improves coding and practice improves problem solving"
print(char_freq(sentence))

# q3: Merge Two Dictionaries
# Sol:
def merge_dict(first, second):
    first.update(second)
    return first

product = {
    "id": 101,
    "name": "Laptop",
    "brand": "Dell",
    "price": 65000,
    "stock": 15
}
employee = {
    "id": 1,
    "name": "Rahul",
    "salary": 50000
}
print(merge_dict(product, employee))

# q4: Highest Value Key
# Sol:
def highest_value_key(data):
    max_key = None
    max_value = float("-inf")

    for key in data:
        if data[key] > max_value:
            max_value = data[key]
            max_key = key
    return max_key
product = {
    "id": 101,
    "name": 10000,
    "price": 65000,
    "stock": 15
}
            
# print(highest_value_key(product))

# q5: Invert Dictionary (means key ko value bana do aur value ko key)
# Sol:
def invert_dict(data):
    invert = {}
    for key, value in data.items():
        key, value = value, key
        invert[key] =  value
    return invert
# or optimise version
def invert_dict(data):
    invert = {}
    for key, value in data.items():
        invert[value] = key
    return invert

product = {
    "id": 101,
    "name": 10000,
    "price": 65000,
    "stock": 15
}
print(invert_dict(product))  
