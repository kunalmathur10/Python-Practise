# # q1:Reverse String
# # Sol:
# def reverse_string(word):
#     rev = ""
#     for i in word:
#         rev = i + rev
#     return rev
# word = input("Enter the word here: ")
# print(reverse_string(word))
# # or Optimise version
# word = input("Enter the word here: ")
# reverse = word[::-1]
# print(reverse)

# # q2: Palindrome string:
# # Sol:
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False
# # or 
# def is_palindrome(word):
#     return word == word[::-1]

# word = input("Enter the word here")
# print(word)
# print(word[::-1])
# if is_palindrome(word):
#     print("It is Palindrome")
# else:
#     print("It is not Palindrome")

# # q3: Count vowels
# # sol:
# def count_vowels():
#     count = 0
#     vowel = "aeiou"
#     for i in word.lower():
#         if i in vowel:
#             count += 1
#     return count
# word = (input("Enter the word here: "))
# print(count_vowels(word))

# q4: Anagram Check
# Sol:
# def anagram(word1, word2):
#     if sorted(word1) == sorted(word2):
#         return True
#     return False
# word1 = input("Enter the word here: ")
# word2 = input("Enter the word here: ")
# if anagram(word1, word2):
#     print(f"{word1} is anagram of {word2}")
# else:
#     print(f"{word1} is not a anagram of {word2}")

# q5:First Non-Repeating Character
# Sol: 
def first_non_rep_ch(word):
    freq = {}
    for ch in word.lower():
        freq[ch] = freq.get(ch,0) + 1
    for ch in word.lower():
        if freq[ch]==1:
            return ch
    return False
word = input("Enter the word here: ")
result = first_non_rep_ch(word)
if result:
    print(f"{result} is the first non-repeating character")
else:
    print("There is no non-repeating character")
