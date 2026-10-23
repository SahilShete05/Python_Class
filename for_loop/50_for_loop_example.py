# 1) Write a Python program to print numbers from 1 to 10 using a for loop.

for i in range(1,11) :
    print("Number", i)

# 2) Write a Python program to print numbers from 10 to 1 in reverse order    

for i in range(10,0,-1) :
    print("Number", i)

# 3) Write a Python program to print all even numbers from 1 to 50.

for i in range(2,51,2) :
    print("Even Number", i)

# 4) Write a Python program to print all odd numbers from 1 to 50    

for i in range(1,51,2) :
    print("Odd Number" ,i)

# 5) Write a Python program to print the multiplication table of a number entered by the user.

number = int(input("Enter any number "))

for i in range(1,11) :
    print(number, "*", i, "=", number * i)

# 6) Write a Python program to calculate the sum of numbers from 1 to 100    

total = 0
for i in range(1,101) :
    total += i
print("Sum of number from 1 to 100 is" , total)


# 7)Write a Python program to print each character of a string on a separate line.

name = "Sahil"
for char in name :
    print(char)

# 8) Write a Python program to display the squares of numbers from 1 to 10.

for i in range(1,11) :
    print("Square of ", i, "is", i**2)

# 9) Write a Python program to print all numbers between 1 and 100 that are divisible by 5    

for i in range(1,101) :
    if(i % 5 == 0) :
        print(i, "is divisible by 5")  

# 10 Write a Python program to print every element of a list using a for loop        

name = ["Sahil", "Harshal", "Hari"] 

for fname in name :
    print(fname)

# 11) Write a Python program to calculate the factorial of a number using a for loop.    

fact = 1
number = int(input("Enter any number "))

for i in range(1, number + 1) :
    fact *= i
print(fact) 


# 12) Write a Python program to count the number of characters in a string without using len()

text = input("Enter any string ")
counter = 0

for char in text :
    counter += 1

print("There are", counter , "in a entered text")


# 13) Write a Python program to count the number of vowels in a string.

vowel_count = 0
text = input("Enter any text ")

for char in text :

    if(char == "A" or char == "E" or char == "I" or char == "O" or char == "U" or 
       char == "a" or char == "e" or char == "i" or char == "o" or char == "u") :
        
        vowel_count += 1

print("There are" , vowel_count, "vowels in your entered string")            


# 14) Write a Python program to calculate the sum of all elements in a list without using sum()

list_number = [10, 20, 30, 40, 50]
total = 0

for number in list_number :
    total = total + number
print("Sum of all numbers in list is ", total)  


# 15) Write a Python program to reverse a string using a for loop without using slicing or reversed().

text = input("Enter any text ")
reversed_text = ""

for char in text :
    reversed_text = char + reversed_text 
print(reversed_text)    


# 16) Write a Python program to calculate the sum of even number using a for loop.

even_sum = 0

for i in range(1,101) :
    if(i % 2 == 0) :
        even_sum += i
print("Even number sum from 1 to 100 is ",even_sum) 



# 16) Write a Python program to calculate the sum of odd number using a for loop.

odd_sum = 0

for i in range(1,101) :
    if(i % 2 != 0) :
        odd_sum += i
print("Odd number sum from 1 to 100 is",odd_sum)   



# 17) Write a Python program to print the first n multiples of a number entered by the user.       

Number = int(input("Enter any number "))

for i in range (1,Number + 1) :
    print(i * Number)

# 18) Write a Python program to count how many even and odd numbers are present in a list.

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,21,22,26,44,56,77,88,99]
even_count = 0
odd_count = 0

for number in list :
    if(number % 2 == 0) :
        even_count += 1
    else :
        odd_count += 1

print("Even number count in list is" , even_count)
print("Odd number count in list is", odd_count)     


# 19) Print numbers divisible by both 3 and 5

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0) :
        print(i)


# 20) Print each character of a string in uppercase

text = input("Enter any text: ")

for char in text:
    print(char.upper())  


# 21) Count uppercase and lowercase letters     

text = input("Enter any text: ")
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)        


# 22) Check whether a string is a palindrome

text = input("Enter any text: ")
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text

if text == reverse_text:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# 23) Count positive, negative and zero values in a list

numbers = [10, -5, 0, 20, -8, 0, 15]
positive = 0
negative = 0
zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)


# 24) Print all prime numbers from 1 to 100

for number in range(2, 101):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)


# 25) Print numbers from 1 to 20 with their cubes

for i in range(1, 21):
    print("Cube of", i, "is", i ** 3)

# 26) Calculate the product of all elements in a list

numbers = [2, 3, 4, 5]
product = 1

for number in numbers:
    product *= number

print("Product is", product)



# 27) Remove all spaces from a string using a for loop

text = input("Enter a string: ")
new_text = ""

for char in text:
    if char != " ":
        new_text += char

print("String without spaces:", new_text)


# 28 Print a multiplication table in reverse order

number = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(number, "*", i, "=", number * i)


# 29) Print all factors of a number

number = int(input("Enter a positive number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# 30) Print numbers from 1 to 30 with their fourth powers        

for i in range(1, 31):
    print("Fourth power of", i, "is", i ** 4)


# 31) Calculate the sum of numbers entered by the user

total = 0

for i in range(5):
    number = int(input("Enter a number: "))
    total += number

print("Total sum is", total)



# 32) Find the largest number in a list without using max()

numbers = [12, 45, 7, 89, 34, 56]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number is", largest)


# 33) Find the smallest number in a list without using min()

numbers = [32, 15, 67, 4, 29, 11]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest number is", smallest)



# 34)  Print the ASCII value of each character in a string

text = input("Enter a string: ")

for char in text:
    print(char, "=", ord(char))



# 35) Count how many times a character appears in a string    

text = input("Enter a string: ")
target = input("Enter a character to count: ")
count = 0

for char in text:
    if char == target:
        count += 1

print("Character appears", count, "times")


# 36) Print a string in alternate uppercase and lowercase

text = input("Enter a string: ")
result = ""

for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].upper()
    else:
        result += text[i].lower()

print(result)




# 37) Separate even and odd numbers into two lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even:", even)
print("Odd:", odd)


#38) Count even numbers from 1 to 20

count = 0

for i in range(1, 21):
    if i % 2 == 0:
        count += 1

print("Even numbers:", count)


# 39) Count odd numbers from 1 to 222

count = 0

for i in range(1, 222):
    if i % 2 == 1:
        count += 1

print("Odd numbers:", count)

# 40)  Print positive numbers from a list

numbers = [-2, 5, -8, 10, 3, -1]

for number in numbers:
    if number > 0:
        print(number)


# 41) Print numbers from 1 to 10 with their addition by 5

for i in range(1, 11):
    print(i, "+ 5 =", i + 5)


# 42) Print the numbers in a list that are greater than 10    


numbers = [5, 12, 8, 20, 15, 3]

for number in numbers:
    if number > 10:
        print(number)


# 43) Count the spaces in a sentence


text = input("Enter a sentence: ")
count = 0

for char in text:
    if char == " ":
        count += 1

print("Total spaces:", count) 


# 44) Count the letters in a word

word = input("Enter a word: ")
count = 0

for char in word:
    count += 1

print("Number of letters:", count)


#45) Print each character of a string in lowercase

text = input("Enter a string: ")

for char in text:
    print(char.lower())


# 46) Print numbers and their halves

for i in range(1, 11):
    print(i, "Half is", i / 2)    


# 47) Count zeros in a list    

numbers = [0, 5, 0, 3, 8, 0, 2]
count = 0

for number in numbers:
    if number == 0:
        count += 1

print("Number of zeros:", count)



# 48) Count numbers less than 10 in a list

numbers = [5, 12, 3, 8, 15, 7, 20]
count = 0

for number in numbers:
    if number < 10:
        count += 1

print("Numbers less than 10:", count)



#49) Count numbers greater than 20 in a list

numbers = [10, 25, 30, 15, 45, 8]
count = 0

for number in numbers:
    if number > 20:
        count += 1

print("Count:", count)


# 50) Count numbers greater than zero

numbers = [-2, 5, 0, 8, -4, 3]
count = 0

for number in numbers:
    if number > 0:
        count += 1

print("Positive numbers:", count)