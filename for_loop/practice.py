# To find out given number is prime or not using for loop


number = int(input("Enter any number "))

if number <= 1 :
    isPrime = False 

else :
    isPrime =  True   

    for i in range(2, int(number ** 0.5) + 1) :
        if number % i == 0 :
            isPrime = False
            break
print(isPrime)   



# To find out given number is prime or not using for loop


number = int(input("Enter any number "))

if number <= 1 :
    isPrime = False 

else :
    i = 2
    isPrime = True

    while ( i <= (number ** 0.5) ) :
        if number % i == 0 :
            isPrime = False
            break
        i += 1

print(isPrime)    



# reverse number / string  using for loop

number = input("Enter any number ")
rev = ""

for i in number :
    rev = i + rev
print(rev)

# reverse string using while loop

text =  input("Enter any text")
rev = ""
i = len(text) - 1

while i >= 0 :
    rev = rev + text[i]
    i -= 1
print(rev)    


# reverse number using while loop

number = int(input("Enter any number "))
rev = 0

while number > 0 :
    remainder = number % 10
    rev = rev * 10 + remainder 
    number = number // 10

print(rev)    



# Fibonacci sequence using while loop

number = int(input("Enter any number  "))

a = 0 
b = 1
i = 0

while i < number :
    print(a)
    c = a + b
    a = b
    b = c
    i += 1


# Fibonacci sequence using for loop

number = int(input("Enter any number "))

a = 0
b = 1

for i in range(number) :
    print(a)
    c = a + b
    a = b
    b = c



# Armstrong Number using for Loop

numbers = int(input("enter any number ")) 
sum = 0
total_digits = len(str(numbers))  

for number in str(numbers) :
    sum = sum + int (number) ** total_digits 

if sum == numbers :
    print("yes")
else :
    print("no")        


# Armstrong Number using while Loop

numbers = int(input("Enter any number"))
temp = numbers
sum = 0
total_digits = len(str(numbers))

while temp > 0 :
    remainder = temp % 10 
    sum = sum + remainder ** total_digits
    temp = temp // 10

if sum == numbers :
    print("Yes")
else :
    print("No")        

