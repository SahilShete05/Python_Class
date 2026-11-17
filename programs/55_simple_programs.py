# Create 10 variables with different values and identify their data types.

a = 10
b = 25.5
c = "Python"
d = True
e = [1, 2, 3]
f = (10, 20, 30)
g = {1, 2, 3}
h = {"name": "Rahul", "age": 20}
i = None
j = 5 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))


# Write a program to check the data type of a variable before and after reassignment.

a = 100
print(type(a))

a = "Hello"
print(type(a))

# Create variables to store employee ID, name, salary, department, and employment status.

employee_id = 101
name = "Amit"
salary = 35000.50
department = "IT"
employment_status = True

print(employee_id)
print(name)
print(salary)
print(department)
print(employment_status)



# Accept the length and width of a rectangle and calculate its area. Identify the data types used.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle:", area)

# Write a program to swap two variables without using a third variable.
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

# .Predict the output:

a = 10
b = 20.5
c = "30"

print(type(a + b))
print(type(str(a)))
print(type(float(c)))

# <class 'float'>
# <class 'str'>
# <class 'float'>

# Type Conversion

# Convert "250" into an integer and calculate its square.

a = "250"
b = int(a)

square = b ** 2
print("Square:", square)

# Convert 45 into a float, string, and boolean.

a = 45

print(float(a))
print(str(a))
print(bool(a))

# Convert 99.99 into an integer. Explain the output.

a = 99.99
b = int(a)
print(b)

# Accept a number as a string and convert it into an integer.

num = input("Enter a number: ")
num = int(num)
print("Number:", num)
print("Data type:", type(num))

# Accept a student's marks in string format and calculate the percentage after conversion.

marks = input("Enter marks: ")
marks = float(marks)
total = 500
percentage = (marks / total) * 100
print("Percentage:", percentage, "%")

# Predict the output:

a = 100
b = 20.5

print(str(a) + str(b))
print(int(b))
print(float(a))
print(bool(0))
print(bool(""))

# 10020.5
# 20
# 100.0
# False
# False


# String Data Type

# Accept a person's full name and display it in uppercase and lowercase.

name = input("Enter your full name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# Count the number of characters in a string.

text = input("Enter a string: ")
print("Number of characters:", len(text))

# Reverse a given string without using built-in reverse methods.

text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reverse:", reverse)

# Count how many times the letter "a" appears in a string.

text = input("Enter a string: ")
count = text.lower().count("a")
print("Count of a:", count)


# Replace all spaces in a sentence with hyphens.

sentence = input("Enter a sentence: ")
new_sentence = sentence.replace(" ", "-")
print(new_sentence)


# Check whether a given word exists in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence.split():
    print("Word exists")
else:
    print("Word does not exist")

# Accept an email address and extract the username and domain.

email = input("Enter email address: ")
username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)

# Create a sentence using three variables with string formatting.

name = "Rahul"
age = 20
city = "Nashik"

sentence = f"My name is {name}. I am {age} years old and I live in {city}."

print(sentence)

# List Data Type

# Create a list of 15 numbers and find all numbers greater than 50.

numbers = [10, 60, 25, 75, 90, 30, 55, 15, 80, 45, 65, 20, 100, 35, 50]

for num in numbers:
    if num > 50:
        print(num)

# Find the second-largest number in a list.


numbers = [10, 20, 40, 30, 50]
unique = list(set(numbers))
unique.sort()
print("Second largest:", unique[-2])


# Remove duplicate elements from a list.

numbers = [1, 2, 3, 2, 4, 1, 5]
new_list = list(set(numbers))
print(new_list)

# Create two lists and combine them into one list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2
print(list3)

# Find common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)

# Create a list of student marks and count how many students passed (marks greater than or equal to 40).

marks = [35, 45, 67, 30, 80, 90, 25]
count = 0

for mark in marks:
    if mark >= 40:
        count += 1

print("Passed students:", count)

# Separate positive, negative, and zero values into three different lists.

numbers = [10, -5, 0, 20, -10, 0, 5]

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

# .Find the sum of all even numbers in a list.

numbers = [1, 2, 3, 4, 5, 6, 8]
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)

# Create a nested list containing student names and marks. Access individual elements.

students = [
    ["Rahul", 85],
    ["Amit", 90],
    ["Priya", 95]
]

print(students[0])
print(students[0][0])
print(students[0][1])

print(students[1][0])
print(students[1][1])

# .Reverse a list without using the reverse() method or slicing.

numbers = [1, 2, 3, 4, 5]
reverse = []

for num in numbers:
    reverse.insert(0, num)

print(reverse)

# Tuple Data Type

# .Create a tuple of 15 numbers and find all numbers greater than 50.

numbers = (10, 60, 25, 75, 90, 30, 55, 15, 80, 45, 65, 20, 100, 35, 50)

for num in numbers:
    if num > 50:
        print(num)

# .Find the second-largest number in a tuple .

numbers = (10, 20, 40, 30, 50)
unique = sorted(set(numbers))

print("Second largest:", unique[-2])


# Remove duplicate elements from a tuple.

numbers = (1, 2, 3, 2, 4, 1, 5)
new_tuple = tuple(set(numbers))

print(new_tuple)

# Create two tuple and combine them into one tuple.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

# Find common elements between two tuples.

t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)

common = []

for num in t1:
    if num in t2:
        common.append(num)

print(tuple(common))

# Create a list of student marks and count how many students passed (marks greater than or equal to 40).

marks = (35, 45, 67, 30, 80, 90, 25)
count = 0

for mark in marks:
    if mark >= 40:
        count += 1

print("Passed students:", count)

# .Separate positive, negative, and zero values into three different tuples .

numbers = (10, -5, 0, 20, -10, 0, 5)

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", tuple(positive))
print("Negative:", tuple(negative))
print("Zero:", tuple(zero))

# Find the sum of all even numbers in a tuples.

numbers = (1, 2, 3, 4, 5, 6, 8)
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum:", total)

# Create a nested tuple containing student names and marks. Access individual elements.

students = (
    ("Rahul", 85),
    ("Amit", 90),
    ("Priya", 95)
)

print(students[0])
print(students[0][0])
print(students[0][1])

# Reverse a tuple without using the reverse() method or slicing.

numbers = (1, 2, 3, 4, 5)

reverse = ()

for num in numbers:
    reverse = (num,) + reverse

print(reverse)

# Set Data Type

# Create two sets of employee IDs and identify common employees.

set1 = {101, 102, 103, 104}
set2 = {103, 104, 105, 106}
common = set1.intersection(set2)
print("Common employees:", common)

# Find elements present in the first set but not in the second set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)
print(result)

# Check whether one set is a subset of another set.

set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))

# .Create a set from a string and display its unique characters.

text = "programming"
unique = set(text)
print(unique)

# 45.Given three sets of numbers, find the common elements among all three.

a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
c = {2, 3, 7, 8}
common = a.intersection(b, c)

print(common)

# Dictionary Data Type

# Create a dictionary of five employees with their salaries.

employees = {
    "Rahul": 30000,
    "Amit": 35000,
    "Priya": 40000,
    "Neha": 45000,
    "Rohit": 32000
}

print(employees)

# .Find the employee receiving the highest salary.

employees = {
    "Rahul": 30000,
    "Amit": 35000,
    "Priya": 40000,
    "Neha": 45000,
    "Rohit": 32000
}

highest_salary = 0
highest_employee = ""

for name, salary in employees.items():
    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

print("Employee:", highest_employee)
print("Highest Salary:", highest_salary)

# Calculate the total salary of all employees.

employees = {
    "Rahul": 30000,
    "Amit": 35000,
    "Priya": 40000,
    "Neha": 45000,
    "Rohit": 32000
}

total = sum(employees.values())
print("Total salary:", total)

# Count the frequency of each character in a given string using a dictionary.

text = "hello"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

# Create a dictionary from two lists: one containing keys and another containing values.
keys = ["name", "age", "city"]
values = ["Rahul", 20, "Nashik"]
my_dict = dict(zip(keys, values))

print(my_dict)

# Merge two dictionaries into one.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}

print(dict3)

# Create a dictionary containing product names and prices. Display products costing more than â‚¹500.

products = {
    "Laptop": 50000,
    "Mouse": 400,
    "Keyboard": 800,
    "Monitor": 12000,
    "Pen": 20
}

for name, price in products.items():
    if price > 500:
        print(name, price)

# Create a nested dictionary containing details of three students and display each student's information.

students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Amit",
        "age": 21,
        "marks": 90
    },
    "student3": {
        "name": "Priya",
        "age": 19,
        "marks": 95
    }
}

for key, value in students.items():
    print(key, value)

# Write a program to check whether a particular key exists in a dictionary.

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")

# Create a dictionary of subject names and marks. Find the highest-scoring subject.

subjects = {
    "Python": 90,
    "Java": 85,
    "C": 75,
    "HTML": 80,
    "SQL": 95
}

highest_marks = 0
highest_subject = ""

for subject, marks in subjects.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_subject = subject

print("Highest Subject:", highest_subject)
print("Highest Marks:", highest_marks)

