# # positional args

# #1) additon of number


# def sum(*args) :
#     total = 0
#     for i in args :
#         total += i
#     print(total)

# sum(1,2,3,4,5)

# # 2 odd_even

# def even_odd(*args) :
#     for i in args :
#         if i % 2 == 0 :
#             print("even", i)
#         else :
#             print("odd",i)    

# even_odd(1,2,3,4,5,6)


# # keyword args 

# # 3) student_info
# def student_info(**kwargs) :
#     print(kwargs)

# student_info(name="Sahil", age = 15, city="akole")


# # 4 marks

# def marks(**kwargs) :
#         print(kwargs.values())


# marks(eng = 13,maths = 22, sci = 45, history = 33)


# # nested function
# # 5)

# def outer() :
#     print("before calling inner")
#     def inneer():
#         print("inner")
#     inneer()
#     print("afer calling inner")    

# outer()

# # 6)
# def number() :
#     def square(x) :
#         print(x * x) 
#     square(6)
# number()       


# # local and global

# # 7) 
# y = 111

# def caa() :
#     print(y)
#     global x 
#     x = 44
#     print(x)

# caa()


# # simple intrest

# def SI 


numbers = [2,5,6,7,9,11,13]
primenumbers = []

for num in numbers:
    if num < 2:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primenumbers.append(num)

print(primenumbers)
   