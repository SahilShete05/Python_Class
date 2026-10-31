
# 1) Print numbers from 1 to 10

i = 1
while i <= 10:
    print("Number", i)
    i += 1


# 2) Print numbers from 10 to 1 in reverse order

i = 10
while i >= 1:
    print("Number", i)
    i -= 1


# 3) Print all even numbers from 1 to 50

i = 2
while i <= 50:
    print("Even Number", i)
    i += 2


# 4) Print all odd numbers from 1 to 50

i = 1
while i <= 50:
    print("Odd Number", i)
    i += 2


# 5) Multiplication table of a number

number = int(input("Enter any number: "))
i = 1

while i <= 10:
    print(number, "*", i, "=", number * i)
    i += 1


# 6) Sum of numbers from 1 to 100

total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print("Sum of numbers from 1 to 100 is", total)


# 7) Print each character of a string

name = "Sahil"
i = 0

while i < len(name):
    print(name[i])
    i += 1


# 8) Squares of numbers from 1 to 10

i = 1
while i <= 10:
    print("Square of", i, "is", i ** 2)
    i += 1


# 9) Numbers between 1 and 100 divisible by 5

i = 1
while i <= 100:
    if i % 5 == 0:
        print(i, "is divisible by 5")
    i += 1


# 10) Print every element of a list

name = ["Sahil", "Harshal", "Hari"]
i = 0

while i < len(name):
    print(name[i])
    i += 1


# 11) Calculate factorial of a number

number = int(input("Enter any number: "))
fact = 1
i = 1

while i <= number:
    fact *= i
    i += 1

print("Factorial is", fact)


# 12) Print numbers from -10 to 10

i = -10
while i <= 10:
    print(i)
    i += 1


# 13) Count vowels in a string

vowel_count = 0
text = input("Enter any text: ")
i = 0

while i < len(text):
    if text[i] in "AEIOUaeiou":
        vowel_count += 1
    i += 1

print("There are", vowel_count, "vowels in your entered string")


# 14) Sum all elements in a list without using sum()

list_number = [10, 20, 30, 40, 50]
total = 0
i = 0

while i < len(list_number):
    total += list_number[i]
    i += 1

print("Sum of all numbers in list is", total)


# 15) Reverse a string without slicing or reversed()

text = input("Enter any text: ")
reversed_text = ""
i = 0

while i < len(text):
    reversed_text = text[i] + reversed_text
    i += 1

print(reversed_text)


# 16) Sum of even numbers from 1 to 100

even_sum = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        even_sum += i
    i += 1

print("Even number sum from 1 to 100 is", even_sum)


# 17) Sum of odd numbers from 1 to 100

odd_sum = 0
i = 1

while i <= 100:
    if i % 2 != 0:
        odd_sum += i
    i += 1

print("Odd number sum from 1 to 100 is", odd_sum)


# 18) Print the first n multiples of a number

number = int(input("Enter the number: "))
n = int(input("How many multiples do you want? "))
i = 1

while i <= n:
    print(number * i)
    i += 1


# 19) Count even and odd numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 15, 17, 21, 22, 26,
           44, 56, 77, 88, 99]

even_count = 0
odd_count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print("Even number count in list is", even_count)
print("Odd number count in list is", odd_count)


# 20) Print numbers divisible by both 3 and 5

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1


# 21) Print each character of a string in uppercase

text = input("Enter any text: ")
i = 0

while i < len(text):
    print(text[i].upper())
    i += 1


# 22) Count uppercase and lowercase letters

text = input("Enter any text: ")
upper_count = 0
lower_count = 0
i = 0

while i < len(text):
    if text[i].isupper():
        upper_count += 1
    elif text[i].islower():
        lower_count += 1
    i += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


# 23) Check whether a string is a palindrome

text = input("Enter any text: ")
reverse_text = ""
i = 0

while i < len(text):
    reverse_text = text[i] + reverse_text
    i += 1

if text == reverse_text:
    print("String is a palindrome")
else:
    print("String is not a palindrome")


# 24) Count positive, negative and zero values

numbers = [10, -5, 0, 20, -8, 0, 15]
positive = 0
negative = 0
zero = 0
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        positive += 1
    elif numbers[i] < 0:
        negative += 1
    else:
        zero += 1
    i += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)


# 25) Print all prime numbers from 1 to 100

number = 2

while number <= 100:
    i = 2
    is_prime = True

    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(number)

    number += 1


# 26) Print numbers from 1 to 20 with their cubes

i = 1

while i <= 20:
    print("Cube of", i, "is", i ** 3)
    i += 1


# 27) Calculate product of all elements in a list

numbers = [2, 3, 4, 5]
product = 1
i = 0

while i < len(numbers):
    product *= numbers[i]
    i += 1

print("Product is", product)


# 28) Remove all spaces from a string

text = input("Enter a string: ")
new_text = ""
i = 0

while i < len(text):
    if text[i] != " ":
        new_text += text[i]
    i += 1

print("String without spaces:", new_text)


# 29) Print multiplication table in reverse order

number = int(input("Enter a number: "))
i = 10

while i >= 1:
    print(number, "*", i, "=", number * i)
    i -= 1


# 30) Print all factors of a number

number = int(input("Enter a positive number: "))
i = 1

while i <= number:
    if number % i == 0:
        print(i)
    i += 1


# 31) Print numbers from 1 to 30 with their fourth powers

i = 1

while i <= 30:
    print("Fourth power of", i, "is", i ** 4)
    i += 1


# 32) Calculate sum of five numbers entered by the user

total = 0
i = 1

while i <= 5:
    number = int(input("Enter a number: "))
    total += number
    i += 1

print("Total sum is", total)


# 33) Find largest number without using max()

numbers = [12, 45, 7, 89, 34, 56]
largest = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("Largest number is", largest)


# 34) Find smallest number without using min()

numbers = [32, 15, 67, 4, 29, 11]
smallest = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] < smallest:
        smallest = numbers[i]
    i += 1

print("Smallest number is", smallest)


# 35) Print ASCII value of each character

text = input("Enter a string: ")
i = 0

while i < len(text):
    print(text[i], "=", ord(text[i]))
    i += 1


# 36) Count how many times a character appears

text = input("Enter a string: ")
target = input("Enter a character to count: ")
count = 0
i = 0

while i < len(text):
    if text[i] == target:
        count += 1
    i += 1

print("Character appears", count, "times")


# 37) Print string in alternate uppercase and lowercase

text = input("Enter a string: ")
result = ""
i = 0

while i < len(text):
    if i % 2 == 0:
        result += text[i].upper()
    else:
        result += text[i].lower()
    i += 1

print(result)


# 38) Separate even and odd numbers into two lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
    i += 1

print("Even:", even)
print("Odd:", odd)


# 39) Count even numbers from 1 to 20

count = 0
i = 1

while i <= 20:
    if i % 2 == 0:
        count += 1
    i += 1

print("Even numbers:", count)


# 40) Count odd numbers from 1 to 221

count = 0
i = 1

while i < 222:
    if i % 2 == 1:
        count += 1
    i += 1

print("Odd numbers:", count)


# 41) Print positive numbers from a list

numbers = [-2, 5, -8, 10, 3, -1]
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        print(numbers[i])
    i += 1


# 42) Print numbers from 1 to 10 with their addition by 5

i = 1

while i <= 10:
    print(i, "+ 5 =", i + 5)
    i += 1


# 43) Print numbers in a list greater than 10

numbers = [5, 12, 8, 20, 15, 3]
i = 0

while i < len(numbers):
    if numbers[i] > 10:
        print(numbers[i])
    i += 1


# 44) Count spaces in a sentence

text = input("Enter a sentence: ")
count = 0
i = 0

while i < len(text):
    if text[i] == " ":
        count += 1
    i += 1

print("Total spaces:", count)


# 45) Count letters in a word

word = input("Enter a word: ")
count = 0
i = 0

while i < len(word):
    count += 1
    i += 1

print("Number of letters:", count)


# 46) Print each character of a string in lowercase

text = input("Enter a string: ")
i = 0

while i < len(text):
    print(text[i].lower())
    i += 1


# 47) Print numbers and their halves

i = 1

while i <= 10:
    print(i, "Half is", i / 2)
    i += 1


# 48) Count zeros in a list

numbers = [0, 5, 0, 3, 8, 0, 2]
count = 0
i = 0

while i < len(numbers):
    if numbers[i] == 0:
        count += 1
    i += 1

print("Number of zeros:", count)


# 49) Count numbers less than 10 in a list

numbers = [5, 12, 3, 8, 15, 7, 20]
count = 0
i = 0

while i < len(numbers):
    if numbers[i] < 10:
        count += 1
    i += 1

print("Numbers less than 10:", count)


# 50) Count numbers greater than 20 in a list

numbers = [10, 25, 30, 15, 45, 8]
count = 0
i = 0

while i < len(numbers):
    if numbers[i] > 20:
        count += 1
    i += 1

print("Count:", count)


# 51) Count numbers greater than zero

numbers = [-2, 5, 0, 8, -4, 3]
count = 0
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        count += 1
    i += 1

print("Positive numbers:", count)





