username = "Sahil"
password = "Sahil123"

if(username == "Sahil") : 
    print("Username is correct")
    if(password == "Sahil123"):
        print("Passowrd is correct")
    else: 
        print("Passowrd is incorrect")    
else:
    print("Username is incorrect")    



age = 10
eligible_vote=True
if(age >= 18):
    print("Your age is atleast 18 years old")
    if(eligible_vote): 
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")    
    

else:
    print("You are not 18 years old")    


marks = 12
Pass = True

if(Pass):
    print("You have passed the exam")
    if(marks >=75):
        print("You have scored atleast 75 marks")
    else:
        print("You have not scored atleast 75 marks")
else:
    print("You have not passed the exam")  

positive = 33

if(positive == 0):
    print("You have entered 0")

elif(positive > 0):
    print("Your number is positive")
    if(positive % 2 == 0):
        print("Your number is even")
    else:
        print("Your number is odd")    

else:
    print("You have entered negative number")    

age = 22
salary = 50000


if(age > 25):
    print("Your age is eligible for loan")

    if(salary > 50000):
        print("Your salary is sufficient for taking a loan")
    else:
        print("Your salary is sufficient for taking a loan")    

else:
    print("Your age is not eligible for loan")  



username = "Sahil"
password="Sahil11"
isActive = True

if(username == "Sahil" and password=="Sahil11"):
    print("Your have logged in successfully")
    if(isActive):
        print("Your account is active")
    else:
        print("Your account is not active")
else:
     print("Your username or password is invalid")

number = 56

if(number <10 and number > 50):
    print("Your number is between 10 and 50")
else:
    print("Your number is not between 10 and 50")    


number =  21

if(number % 3 == 0  and number % 7 == 0 ):
    print("Your number is divisble by 3 and 7")

else:
    print("Your number is not divisble by 3 and 7")

age = 22
qualification = True

if(age<21 and age > 35):
    print("Your age is matched for job")

    if(qualification):
        print("Your qualification matches job role")
    else:    
        print("Your qualification matches job role")

else:
    print("Your age is not matched for job")

name = "S"


if(name == "A" or name=="E" or  name=="I" or name=="O" or name == "U" or name == "a" or name=="e" or name=="i" or name=="o" or name == "u"):
    print("It is vowel")

else:
    print("It is not vowel")

number = 56

if(number <100 and number > 200):
    print("Your number is between 10 and 50")
else:
    print("Your number is not between 10 and 50")  

theory = True
practical = True

if(theory == True and practical == True):
    print("You have passed")

else:
    print("You have not passed")

order= 600
premimum = True


if(order >= 500 or premimum):
    print("You are eligible for free order")
else:    
    print("You are eligible for free order")   



A,B,C,D = 111,2,3,4

if(A>B and A>C and A>D):
    print("A is greatest of all number")
elif(B>A and B>C and B>D):
    print("B is greatest of all number")    
elif(C>A and C>B and C>D):
    print("C is greatest of all number") 
else:
    print("D is greatest of all number")       






