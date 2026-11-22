

# 1. Student Management System

class Student:
    def __init__(self, student_name, roll_no, course):
        self.student_name = student_name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("Name:", self.student_name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


s1 = Student("Sahil", 35, "Python")
s2 = Student("Harshal", 33, "Java")
s3 = Student("Hari", 32, "React")

s1.display_details()
s2.display_details()
s3.display_details()


# 2. Employee Salary Details

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        annual_salary = self.salary * 12
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Annual Salary:", annual_salary)


e1 = Employee("Sahil", 12, 10000)
e1.calculate_salary()


# 3. Mobile Phone Details

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def apply_discount(self, discount):
        final_price = self.price - discount
        print("Final Price:", final_price)


m1 = Mobile("Apple", "iPhone 13", 50000)
m1.display_details()
m1.apply_discount(1000)


# 4. Bank Account

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Total Balance:", self.balance)


b1 = BankAccount("Sahil", 100000)
b1.deposit(10000)
b1.withdraw(5000)
b1.display_balance()


# 5. Car Rental System

class Car:
    def __init__(self, name, rent_per_day):
        self.name = name
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        total = self.rent_per_day * days
        print("Car Name:", self.name)
        print("Rental Days:", days)
        print("Total Rent:", total)


c1 = Car("BMW", 10000)
c1.calculate_rent(5)



# 6. Laptop Information - No Argument Constructor

class Laptop:
    def __init__(self):
        self.brand = "Dell"
        self.ram = "16GB"
        self.price = 55000

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Price:", self.price)


l1 = Laptop()
l1.display()


# 7. Book Information - Parameterized Constructor

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)


b1 = Book("Python", "Sahil", 255)
b2 = Book("Java", "Harshal", 350)

b1.display()
b2.display()


# 8. Rectangle Area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Rectangle Area:", area)


r1 = Rectangle(5, 6)
r1.calculate_area()


# 9. Electricity Bill

class ElectricityBill:
    def __init__(self, customer_name, units_consumed):
        self.customer_name = customer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        if self.units_consumed <= 100:
            bill = self.units_consumed * 5

        elif self.units_consumed <= 200:
            bill = (100 * 5) + ((self.units_consumed - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((self.units_consumed - 200) * 10)

        print("Customer Name:", self.customer_name)
        print("Units Consumed:", self.units_consumed)
        print("Total Bill: ₹", bill)


customer1 = ElectricityBill("Rahul", 250)
customer1.calculate_bill()


# 10. Product Inventory

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total_price(self):
        total = self.price * self.quantity
        return total

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Updated Quantity:", self.quantity)


p1 = Product("Laptop", 50000, 2)
p1.display_product()
print("Total Price:", p1.calculate_total_price())
p1.update_quantity(5)


# 11. Company Employee Counter

class Employee:
    company_name = "TCS"
    employee_count = 0

    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id

        Employee.employee_count += 1

    def display(self):
        print("Company:", Employee.company_name)
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Total Employees:", Employee.employee_count)


e1 = Employee("Sahil", 101)
e2 = Employee("Harshal", 102)
e3 = Employee("Rahul", 103)

e1.display()
e2.display()
e3.display()


# 12. School Student Information

class Student:
    school_name = "ABC School"

    def __init__(self, student_name, roll_number):
        self.student_name = student_name
        self.roll_number = roll_number

    def display(self):
        percentage = 85

        print("School:", Student.school_name)
        print("Student Name:", self.student_name)
        print("Roll Number:", self.roll_number)
        print("Percentage:", percentage)


s1 = Student("Sahil", 35)
s1.display()


# 13. Shopping Cart

class ShoppingCart:
    discount_percentage = 10

    def __init__(self, customer_name, total_amount):
        self.customer_name = customer_name
        self.total_amount = total_amount

    def calculate_discount(self):
        discount = self.total_amount * ShoppingCart.discount_percentage / 100

        final_amount = self.total_amount - discount

        print("Customer:", self.customer_name)
        print("Total Amount:", self.total_amount)
        print("Discount:", discount)
        print("Final Amount:", final_amount)


cart1 = ShoppingCart("Sahil", 5000)
cart1.calculate_discount()


# 14. Hospital Patient Management

class Patient:
    hospital_name = "City Hospital"

    def __init__(self, patient_name, patient_age, disease):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.disease = disease

    def display_patient(self):
        print("Hospital:", Patient.hospital_name)
        print("Patient Name:", self.patient_name)
        print("Age:", self.patient_age)
        print("Disease:", self.disease)


p1 = Patient("Sahil", 22, "Fever")
p2 = Patient("Rahul", 25, "Cold")
p3 = Patient("Harshal", 23, "Cough")

p1.display_patient()
p2.display_patient()
p3.display_patient()


# 15. Online Course Management

class Course:
    institute_name = "ABC Institute"

    def __init__(self, course_name, course_fee):
        self.course_name = course_name
        self.course_fee = course_fee

    def calculate_fee(self):
        discount = 1000

        final_fee = self.course_fee - discount

        print("Institute:", Course.institute_name)
        print("Course Name:", self.course_name)
        print("Original Fee:", self.course_fee)
        print("Discount:", discount)
        print("Final Fee:", final_fee)


c1 = Course("Python", 10000)
c1.calculate_fee()



# 16. ATM Withdrawal System

class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient Balance")
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


a1 = ATM("Sahil", 50000)

print("Current Balance:", a1.check_balance())
print("After Withdraw:", a1.withdraw(5000))
print("After Deposit:", a1.deposit(10000))


# 17. Temperature Converter

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius


t1 = Temperature(37)

print("Celsius to Fahrenheit:", t1.celsius_to_fahrenheit())
print("Fahrenheit to Celsius:", t1.fahrenheit_to_celsius(98.6))


# 18. Student Result Management

class StudentResult:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculate_total(self):
        total = self.sub1 + self.sub2 + self.sub3
        return total

    def calculate_percentage(self):
        percentage = self.calculate_total() / 300 * 100
        return percentage

    def display_result(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")


s1 = StudentResult("Sahil", 80, 85, 90)
s1.display_result()


# 19. Food Ordering System

class FoodOrder:
    def __init__(self, customer_name, food_item, food_price, quantity):
        self.customer_name = customer_name
        self.food_item = food_item
        self.food_price = food_price
        self.quantity = quantity

    def calculate_bill(self):
        total = self.food_price * self.quantity
        return total

    def apply_coupon(self, discount):
        final_bill = self.calculate_bill() - discount
        return final_bill

    def display_order(self):
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Food Price:", self.food_price)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.calculate_bill())
        print("Final Bill:", self.apply_coupon(50))


f1 = FoodOrder("Sahil", "Pizza", 250, 2)
f1.display_order()


# 20. Vehicle Management System

class Vehicle:
    vehicle_count = 0

    def __init__(self, vehicle_name, vehicle_type, vehicle_price):
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.vehicle_price = vehicle_price

        Vehicle.vehicle_count += 1

    def display_details(self):
        print("Vehicle Name:", self.vehicle_name)
        print("Vehicle Type:", self.vehicle_type)
        print("Vehicle Price:", self.vehicle_price)

    def calculate_insurance(self, rate):
        insurance = self.vehicle_price * rate / 100
        return insurance

    def update_price(self, new_price):
        self.vehicle_price = new_price
        print("Updated Price:", self.vehicle_price)


v1 = Vehicle("BMW", "Car", 5000000)
v2 = Vehicle("Honda", "Bike", 150000)
v3 = Vehicle("Audi", "Car", 6000000)

v1.display_details()

print("Insurance:", v1.calculate_insurance(5))

v1.update_price(5500000)

print("Total Vehicles:", Vehicle.vehicle_count)
