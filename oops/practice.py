class ShoppingCart() :
    def set_details(self,customer_name,product_name,price,quantity) :
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self) :
        total = self.price * self.quantity    
        return total

    def apply_discount(self,discount) :
        total = self.calculate_total()
        return total - ( total * discount) 
    
    def display_bill(self):

        total = self.calculate_total()

        print("Customer Name:", self.customer_name)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount:", total)

        if total > 5000:
            discount = total * 10 / 100
            final_amount = total - discount
            print("Discount (10%):", discount)
        else:
            final_amount = total

        print("Final Amount:", final_amount)
        
obj = ShoppingCart()
obj.set_details("Rahul", "Laptop", 3000, 2)
obj.display_bill()            



class LibraryBook:
    def set_details(self, book_name, author_name, price, is_available):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price
        self.is_available = is_available

    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print("Book issued successfully.")
        else:
            print("Sorry, book is not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned successfully.")
        else:
            print("Book was not issued.")

    def display_details(self):
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Price:", self.price)
        print("Availability:", "Available" if self.is_available else "Not Available")


book1 = LibraryBook()
book1.set_details("Python ", "sahil", 500, True)
book1.display_details()
book1.issue_book()
book1.return_book()
book1.display_details()


class ElectricityBill:
    def set_details(self, customer_name, units_consumed):
        self.customer_name = customer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        if self.units_consumed <= 100:
            self.bill = self.units_consumed * 3

        elif self.units_consumed <= 200:
            self.bill = (100 * 3) + ((self.units_consumed - 100) * 5)

        else:
            self.bill = (100 * 3) + (100 * 5) + ((self.units_consumed - 200) * 8)

    def display_bill(self):
        print("Customer Name:", self.customer_name)
        print("Units Consumed:", self.units_consumed)
        print("Total Electricity Bill: ₹", self.bill)


customer1 = ElectricityBill()
customer1.set_details("Rahul", 250)
customer1.calculate_bill()
customer1.display_bill()