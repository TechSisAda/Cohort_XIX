# Define the PizzaOrder class to handle the pizza order and billing
class PizzaOrder:
    def __init__(self, size, add_pepperoni, extra_cheese):
        self.size = size.upper()
        self.add_pepperoni = add_pepperoni.upper()
        self.extra_cheese = extra_cheese.upper()
        self.bill = 0


    def calculate_bill(self):
        if self.size == "S":
            self.bill += 15
        elif self.size == "M":
            self.bill += 20
        elif self.size == "L":
            self.bill += 25


        if self.add_pepperoni == "Yes":
            if self.size == "S":
                self.bill += 1
            else:
                self.bill += 2


        if self.extra_cheese == "Y":
            self.bill += 1

        return self.bill



size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Yes or No: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")



order = PizzaOrder(size, add_pepperoni, extra_cheese)



final_bill = order.calculate_bill()
print(f"Your final bill is: ${final_bill}")
print("Thank You!")
