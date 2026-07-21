# Definition: File handling is the process of creating, reading, writing, update, delete the files stored on secondary storage.
#  File handling ka matlab hard disk me stored file ke saath kaam karna.
# | Mode | Existing File          | File Doesn't Exist |
# | ---- | ---------------------- | ------------------ |
# | `r`  | Read                   | ❌ Error            |
# | `w`  | Delete content + Write | ✅ Create           |
# | `a`  | Append at end          | ✅ Create           |

# Create a file student.txt and write Rahul Kunal Amit
file = open("student.txt", "w")
file.write("Rahul\nKunal\nAmit")
file.close()
# Optimise version
with open("student.txt", "w") as file:
    file.write("Rahul\nKunal\nAmit")
# why with: because with automatically close the file even if exception occurs, prevents resource leaks.

# q2: Append new student Amit in existing file
with open("student.txt", "a") as file:
    file.write("\nAmit")

# q3: Read entire file and print
# Sol;
with open("student.txt", "r") as file:
    data = file.read()
    print(data)

# q4: Print total characters in file
# Sol:
with open("student.txt", "r") as file:
    data = file.read()
    print(len(data))

# q5: Count total number of words in file:
# Sol:
with open("student.txt", "r") as file:
    data = file.read()
    words = data.split()
    print(len(words))

# q6: Count number of lines
# Sol:
with open("student.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))

# q7: Count vowels
# Sol:
with open("student.txt", "r") as file:
    data = file.read()
    count = 0
    for i in data.lower():
        if i in "aeiou":
            count += 1
    print(count)

# q8: Copy one file into another
# Sol;
with open("student.txt", "r") as source:
    data = source.read()
with open("backup.txt", "w") as target:
    target.write(data)
print("Copied successfully")

# q9: Merge two files
# Sol:
with open("file1.txt", "r") as f1:
    data1 = f1.read()
with open("file2.txt", "r") as f2:
    data2 = f2.read()
with open("file3.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

# q10: Employee record system
# Sol;
while True:
    print("\n1. Add employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        with open("employee.txt", "a") as file:
            file.write(name + "\n")
    elif choice == "2":
        with open("employee.txt", "r") as file:
            data = file.read()
            print(data)
    elif choice == "3":
        break

# q11: Find the longest word from file
# Sol:
with open("student.txt", "r") as file:
    data = file.read()
    longest = ""
    for word in data.lower().split():
        if len(word) > len(longest):
            longest = word
    print(f"Longest word is: {longest}")

# q12: Find the frequency of each word
# Sol:
with open("student.txt", "r") as file:
    data = file.read()
    freq = {}
    for word in data.lower().split():
        freq[word] = freq.get(word, 0) + 1
    print(freq)


