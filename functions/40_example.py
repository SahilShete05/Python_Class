# With Arguments and With Return Type

# 1) Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("Largest ", largest(15, 25))


# 2) Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))


# 3) Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("Factorial ", factorial(5))


# 4) Prime Number
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if prime(71):
    print("Prime Number")
else:
    print("Not Prime")


# 5) Reverse a Number
def reverse(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev

print("Reverse ", reverse(1234))


# 6) Palindrome Number
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if original == rev:
        return True
    else:
        return False

if palindrome(121):
    print("Palindrome")
else:
    print("Not Palindrome")


# 7) Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a = b
        b = a + b
    return a

print("Fibonacci:", fibonacci(10))


# 8) Count Digits
def count_digits(n):
    count = 0

    if n == 0:
        return 1

    while n > 0:
        count = count + 1
        n = n // 10

    return count

print("Total Digits", count_digits(12345))


# 9) Leap Year
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if leap_year(2024):
    print("Leap Year")
else:
    print("Not Leap Year")


# 10) Positive, Negative or Zero
def check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check(-10))


# Without Arguments and Without Return Type


# 1) Largest of Two Numbers
def largest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        print("Largest:", a)
    else:
        print("Largest:", b)

largest()


# 2) Even or Odd
def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd()


# 3) Factorial
def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

factorial()


# 4) Prime Number
def prime():
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime Number")

prime()


# 5) Reverse a Number
def reverse():
    n = int(input("Enter a number: "))
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    print("Reverse:", rev)

reverse()


# 6) Palindrome Number
def palindrome():
    n = int(input("Enter a number: "))
    original = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()


# 7) Fibonacci Series
def fibonacci():
    n = int(input("Enter number of terms: "))
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b

fibonacci()


# 8) Count Digits
def count_digits():
    n = int(input("Enter a number: "))
    count = 0

    if n == 0:
        count = 1
    else:
        while n > 0:
            count = count + 1
            n = n // 10

    print("Total Digits:", count)

count_digits()


# 9) Leap Year
def leap_year():
    year = int(input("Enter a year: "))

    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not Leap Year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")

leap_year()


# 10) Positive, Negative or Zero
def check():
    n = int(input("Enter a number: "))

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check()



# With Arguments and Without Return Type


# 1) Largest of Two Numbers
def largest(a, b):
    if a > b:
        print("Largest:", a)
    else:
        print("Largest:", b)

largest(15, 25)


# 2) Even or Odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(10)


# 3) Factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

factorial(5)


# 4) Prime Number
def prime(n):
    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime Number")

prime(71)


# 5) Reverse a Number
def reverse(n):
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    print("Reverse:", rev)

reverse(1234)


# 6) Palindrome Number
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome(121)


# 7) Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a = b
        b = a + b

fibonacci(10)


# 8) Count Digits
def count_digits(n):
    count = 0

    if n == 0:
        count = 1
    else:
        while n > 0:
            count = count + 1
            n = n // 10

    print("Total Digits", count)

count_digits(12345)


# 9) Leap Year
def leap_year(year):
    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not Leap Year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")

leap_year(2024)


# 10) Positive, Negative or Zero
def check(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check(-10)



# Without Arguments and With Return Type


# 1) Largest of Two Numbers
def largest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        return a
    else:
        return b

print("Largest:", largest())


# 2) Even or Odd
def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd())


# 3) Factorial
def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print("Factorial:", factorial())


# 4) Prime Number
def prime():
    n = int(input("Enter a number: "))

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if prime():
    print("Prime Number")
else:
    print("Not Prime")


# 5) Reverse a Number
def reverse():
    n = int(input("Enter a number: "))
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    return rev

print("Reverse:", reverse())


# 6) Palindrome Number
def palindrome():
    n = int(input("Enter a number: "))
    original = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if original == rev:
        return True
    else:
        return False

if palindrome():
    print("Palindrome")
else:
    print("Not Palindrome")


# 7) Fibonacci Series
def fibonacci():
    n = int(input("Enter number of terms: "))
    a = 0
    b = 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series

print("Fibonacci:", fibonacci())


# 8) Count Digits
def count_digits():
    n = int(input("Enter a number: "))
    count = 0

    if n == 0:
        return 1

    while n > 0:
        count = count + 1
        n = n // 10

    return count

print("Total Digits:", count_digits())


# 9) Leap Year
def leap_year():
    year = int(input("Enter a year: "))

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if leap_year():
    print("Leap Year")
else:
    print("Not Leap Year")


# 10) Positive, Negative or Zero
def check():
    n = int(input("Enter a number: "))

    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check())
