# 1) Day of the Week

day = int(input("Enter a number from 1 to 7 "))

match day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wedenesday")
    case 4 :     
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number!")  


# 2)Age Group Classifier

age = int(input("Enter your age: "))

match age:
    case n if n < 0:
        print("Invalid age")
    case n if n <= 12:
        print("Child")
    case n if n <= 19:
        print("Teenager")
    case n if n <= 59:
        print("Adult")
    case _:
        print("Senior")



# 3. Basic ATM Menu 

choice = input("Enter choice (balance, deposit, withdraw): ")

match choice:
    case "balance":
        print("Your balance is 5000")
    case "deposit":
        print("Money deposited")
    case "withdraw":
        print("Money withdrawn")
    case _:
        print("Invalid choice")

code = int(input("Enter status code: "))


# 4) HTTP Response Handler

match code:
    case 200 | 201:
        print("Request successful")
    case 301 | 302:
        print("Redirection")
    case 400 | 401 | 403 | 404:
        print("Client error")
    case 500 | 502 | 503:
        print("Server error")
    case _:
        print("Unknown status code")     


# 5) Menu-Driven Program    

print("1. Say Hello")
print("2. Display Square")
print("3. Display Cube")
print("4. Exit")     


choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Hello!")

    case 2:
        num = int(input("Enter a number: "))
        print("Square =", num ** 2)

    case 3:
        num = int(input("Enter a number: "))
        print("Cube =", num ** 3)

    case 4:
        print("Exiting program...")

    case _:
        print("Invalid choice!")


# 6) Shape Identifier        

shape = input("Enter shape: ").lower()

match shape:
    case "circle":
        print("Shape has no sides")
    case "triangle":
        print("Shape has 3 sides")
    case "square":
        print("Shape has 4 equal sides")
    case "rectangle":
        print("Shape has 4 sides")
    case _:
        print("Unknown shape")

# 7. Month Name     
 
month = int(input("Enter month number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")  
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month")   


# 8) Season Finder        

month = int(input("Enter month (1-12): "))

match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8 | 9:
        print("Monsoon")
    case 10 | 11:
        print("Post-monsoon")
    case 12 | 1 | 2:
        print("Winter")
    case _:
        print("Invalid month")


# 9) Electricity Bill Calculator

units = int(input("Enter electricity units: "))

match units:
    case n if n < 0:
        print("Invalid units")

    case n if n <= 100:
        print("Bill:", n * 5)

    case n if n <= 200:
        print("Bill:", n * 7)

    case _:
        print("Bill:", units * 10)


# 10) Mobile Recharge Plan Selector        

plan = int(input("Choose plan (1, 2, or 3): "))

match plan:
    case 1:
        print("Price: ₹199")
        print("Data: 1 GB/day")

    case 2:
        print("Price: ₹299")
        print("Data: 2 GB/day")

    case 3:
        print("Price: ₹399")
        print("Data: 3 GB/day")

    case _:
        print("Invalid plan")