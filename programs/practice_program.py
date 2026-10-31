# check whether a number is even or odd

num = int(input("Enter a number "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# check the num is negative , positive or zero

num = int(input("Enter a number: "))

if num == 0:
    print("Number is 0")

elif num < 0:
    print("It is Negative")

else:
    print("It is Positive")    

#  Reverse a number using while loop
    
a = 12345
ans = 0

while a > 0:
    rem = a % 10
    ans = ans * 10 + rem
    a = a // 10

print("Reverse number is", ans)
  

# Reverse a number using for loop
a = 12345
ans = 0

for i in range(len(str(a))):
    rem = a % 10
    ans = ans * 10 + rem
    a = a // 10

print("Reverse number is", ans)    


# palindrome or not

a = str(222)
rev = ""

for i in a:
    rev = i + rev

if rev == a:
    print("Palindrome")
else:
    print("Not a palindrome")


# Check whether a number is prime

num = 7
isPrime = True

if num < 2 :
    print("Not prime")

else :
    for i in range(2,num) :
        if(num % i == 0) :
            isPrime = False
            break

if isPrime :
    print("Prime")
else :
    print("Not Prime") 


# Print prime numbers from 2 to 100   

for num in range(2,101) :
    for j in range(2,num) :
        if (num % j == 0) :
            print("Not a prime --->", num)
            break
        else :
            print("prime --->" , num)    


# Find factorial of a number

facts = 1
num = 5

for i in range(1,num + 1) :
    facts *= i

print(facts)   


# Find square of a numbe

def square(num) :
    return num ** 2
print(square(4))

# Find cube of a numbe


def cube(num) :
    return num ** 3
print(cube(5))


#  Reverse a string
rev = ""
strings = "sahil"

for i in strings :
    rev = i + rev

print(rev)    


# Check even and odd numbers in a list

l = [1,2,3,4]
for i in l :
    if(i % 2 == 0) :
        print("even" , i)
    else :
        print("Odd", i)    

# Count even and odd numbers in a list

l = [1,2,3,4,7]
even_count = 0
odd_count = 0

for i in l :

    if(i % 2 == 0) :
        even_count += 1
        print("even" , i)
    else :
        print("Odd", i)  
        odd_count += 1  

print("Even count is", even_count)
print("Odd count is ", odd_count)      


# Reverse a list 

l = [1,2,3,45,5]
rev = []

for i in range(len(l)):
    rev.append(l[len(l)-1-i])
    i -= 1
print(rev)

# Find prime numbers from a list
l2 = [4, 5, 6, 7, 8, 9]
prime = []

for num in l2:
    if num >= 2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime.append(num)

print(prime)

# Print only string values from a list

l = ["sahil", 2,4,5]

for i in l :
    if isinstance(i,str) :
        print(i)


# Print only integer values from a list

l = ["sahil", 2,4,5]
for i in l :
    if isinstance(i,int) :
        print(i)


# Find maximum, minimum and sum in a tuple
t = (1,2,4,4,56,7,7,99)
print(max(t))
print(min(t))
print(sum(t))


#  Count elements in a tuple 
t = (1,3,4,5,6,7)
count = 0

for i in t :
    count += 1
print(count)   


# Check even and odd numbers in a tuple

for i in t :
    if (i % 2 == 0) :
        print("even")
    else :
        print("odd")    


dicts = {"1":"sahil", "2": "sss"}
for i,j in dicts.items() :
    print(i,j)

#  Find the total marks from a dictionary    

marks = {1:50, 2:55, 3:54, 4:66}
total = 0
for j in marks.values() :
    total += j

print(total)    

# Find students who scored more than 60

for h,i in marks.items():
    if(i > 60) :
        print(h)

# Check pass or fail
for h,i in marks.items():
    if(i > 50) :
        print("Pass")
    else :
        print("Fail")  

# Find maximum marks from a dictionary

max_marks = 0

for h,i in marks.items() :
    if(max_marks < i) :
        max_marks = i

print(max_marks)    
