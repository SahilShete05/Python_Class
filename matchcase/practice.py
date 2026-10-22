grade = "B"

match grade :
    case "A" :
        print("Excellent")
    case "B" :
        print("Very Good")
    case "C" :
        print("Good")
    case "D" :
        print("Average")
    case "E" :
        print("Need Improvement")
    case "F" :
        print("Fail") 
    case _ :
        print("Invalid Grade")           


month = "Mar"

match month :
    case "Jan" | "Feb" | "Mar" :
        print("Quarter 1")
    case "Apr" | "May" | "June" :
        print("Quarter 2")  
    case "July" | "Aug" | "Sept" :
        print("Quarter 3") 
    case "Oct" | "Nov" | "Dec" :
        print("Quarter 4") 
    case _ :
        print("Invalid Month")           


Role = 3

match Role :
    case 1 : 
        print("Admin")
    case 2 : 
        print("Teacher")
    case 3 : 
        print("Student")
    case 4 : 
        print("Premium Student")
    case _ :
        print("Invalid")    

operation = input("Enter any operator f")
a = 40
b = 20

match operation :
    case "+" :
        print(F"Addition of {a}+ {b} is " , a+b)
    case "-" : 
        print(F"Subtraction of {a} - {b} is " ,a-b)   
    case "*" :
        print(F"Multiplcation of {a} * {b} is", a*b)
    case "/" :
        print(F"Divison of {a} / {b} is", a/b)
    case _ :
        print("Invalid Operator")
               
            
            
            
