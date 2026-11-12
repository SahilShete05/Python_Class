# Practise Questions python : 

# 1. Remove Duplicate Elements: Write a Python program to remove duplicate elements from a list without using set().
   
#    Example: [10, 20, 10, 30, 20, 40]
   
#    Output: [10, 20, 30, 40]

list1 = [10,20,10,30,20,40] 
list2 = []

for i in list1 :
    if i not in list2 :
        list2.append(i)
           
print(list2)


# 2. Find Second Largest Element: Write a program to find the second-largest element from a list without using the sort() method.
   
#    Example: [10, 50, 20, 80, 40]
   
#    Output: 50


list3 =  [10, 50, 20, 80, 40]
largest = list3[0]


print(list3[0])

for i in list3 :
    if i > largest :
        second_largest = largest
        largest = i
        
    elif i < largest and  i > second_largest :
        second_largest = i

print(second_largest)        

 

# 3. Separate Even and Odd Numbers: Write a program to separate even and odd numbers from a list and store them in two different lists.
   
#    Example: [10, 15, 20, 25, 30, 35]
   
#    Output:
#    - Even: [10, 20, 30]
#    - Odd: [15, 25, 35]

list4 = [10, 15, 20, 25, 30, 35]
even = []
odd = []

for i in list4 :
    if i % 2 == 0 :
        even.append(i)
    else :
        odd.append(i)    

print("Even list", even)
print("Odd list", odd) 


# 4. Find Common Elements: Write a program to find common elements between two lists without using set operations.
   
#    Example:
#    - List 1: [10, 20, 30, 40]
#    - List 2: [30, 40, 50, 60]
#    Output: [30, 40]


List5 = [10, 20, 30, 40]
List6 = [30, 40, 50, 60]
common = []

for i in List5 :
    if i in List6 :
        common.append(i)

print(common)


# 5. Move Zeros to the End: Write a program to move all zeros to the end of a list without changing the order of other elements.
   
#    Example: [0, 10, 0, 20, 30, 0, 40]
   
#    Output: [10, 20, 30, 40, 0, 0, 0]

list5 = [0, 10, 0, 20, 30, 0, 40]
result = []

for i in list5 :
    if i != 0 :
        result.append(i)

for i in list5 :
    if i == 0 :
        result.append(i)

print(result)        




# Section 2: Set â€“ 5 Questions

# 6. Find Unique Elements: Write a program to remove duplicate values from a list using a set and display only unique elements.
   
#    Example: [10, 20, 10, 30, 20, 40]
#    Output: {10, 20, 30, 40}

lists = [10,20,10,30,20,40] 
sets = set(lists)
print(sets)
   


# 7. Find Union and Intersection: Write a program to find the union and intersection of two sets.
   
#    Example:
#    - A = {10, 20, 30, 40}
#    - B = {30, 40, 50, 60}

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union of two sets", A | B) 
print("Intersection of two sets", A & B )

# 8. Find Difference: Write a program to display elements that are present in the first set but not in the second set.
   
#    Example:
#    - A = {10, 20, 30, 40}
#    - B = {30, 40, 50}
#    Output: {10, 20}

A = {10, 20, 30, 40}
B = {30, 40, 50}

print("Present in A but no in B", A - B)


# 9. Find Common Students: Two sets contain the names of students enrolled in Java and Python courses. Write a program to display students enrolled in both courses.
   
#    Example:
#    - Java = {"Amit", "Rahul", "Sneha", "Priya"}
#    - Python = {"Sneha", "Priya", "Raj", "Kiran"}
#    Output: {"Sneha", "Priya"}


Java = {"Amit", "Rahul", "Sneha", "Priya"}
Python = {"Sneha", "Priya", "Raj", "Kiran"}
print("Common Students",Java & Python)

# 10. Check Subset: Write a program to check whether all elements of one set are present in another set.
# Example:
# - A = {10, 20}
# - B = {10, 20, 30, 40, 50}
# Output: A is a subset of B

A = {10, 20}
B = {10, 20, 30, 40, 50}

print(A <= B)

# Section 3: Tuple â€“ 5 Questions
# 11. Find Maximum and Minimum: Write a program to find the maximum and minimum values from a tuple without using max() and min().

# Example: (45, 12, 89, 23, 67)

# Output:
# - Maximum: 89
# - Minimum: 12

Tuple1 = (45, 12, 89, 23, 67)

max_num = Tuple1[0]
min_num = Tuple1[0]

for i in Tuple1:
    if i > max_num:
        max_num = i

    if i < min_num:
        min_num = i

print("Minimum", min_num)
print("Maximum", max_num)

# 12. Count Element Frequency: Write a program to count how many times a particular element occurs in a tuple without using the count() method.

# Example: (10, 20, 10, 30, 10, 40)
# Output: 10 occurs 3 times

tuples = (10, 20, 10, 30, 10, 40)
num = tuples[0]
cnt = 0
for i in tuples :
    if num == i :
        cnt += 1    

print("count", cnt)


# 13. Reverse a Tuple: Write a program to reverse a tuple without using the built-in reversed() function.

# Example: (10, 20, 30, 40, 50)
# Output: (50, 40, 30, 20, 10)

tuple12 = (10, 20, 30, 40, 50)
lists = []
i = len(tuple12) - 1

while i >= 0:
    lists.append(tuple12[i])
    i -= 1

result = tuple(lists)
print(result)



# 14. Find Duplicate Elements: Write a program to identify duplicate elements in a tuple.

# Example: (10, 20, 10, 30, 20, 40, 50)
# Output: (10, 20)

t = (10, 20, 10, 30, 20, 40, 50)
t2 = set()

for i in t :
    if t.count(i) > 1 :
        t2.add(i)

print(t2)

# 15. Merge Two Tuples: Write a program to merge two tuples and create a new tuple containing only the common elements once.

# Example:
# - T1 = (10, 20, 30, 40)
# - T2 = (30, 40, 50, 60)

# Output: (30, 40)

T1 = (10, 20, 30, 40)
T2 = (30, 40, 50, 60)
LIST_COMMON = []

for i in T1 :
    if i in T2 :
        LIST_COMMON.append(i) and i not in LIST_COMMON
        
print(tuple(LIST_COMMON))        
