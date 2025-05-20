# from coffee import Coffee
# from order import Order


# class Customer:

#     all_customer = []

#     def __init__(self, name):
        
#         if not isinstance(name, str):
#             raise TypeError("Name must be a string!")
            
        
#         if len(name) < 1 or len(name) > 15:
#             raise ValueError("Number should be 1 to 15 characters long!")
            
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if isinstance (name, str, len<16 or len>0):
#             self._name = name,

#         else:
#             raise TypeError("Name must be a string!")
        
#     def orders(self):
#         customer_orders = []
#         for order in order.all_orders:
#             if order.customer == self:
#                 customer_orders.append(order)
#         return customer_orders

#     def coffees(self):
#         coffees = []
#         for order in self.orders():
#             if order.coffee not in coffees:
#                 coffees.append(order.coffee)
#         return coffees

#     def create_order(self, coffee, price):
#         if not isinstance(coffee, Coffee):
#             raise TypeError("Coffee must be a Coffee object!")
#         new_order = Order(self, coffee, price)
#         return new_order

# customer = Customer("Neema")
# print(customer.name)
        

# This file defines the Customer class for the Coffee Shop Challenge.

from order import Order
from coffee import Coffee  # Added import for Coffee class

class Customer:
    all_customer = []  # List to store all customers

    def __init__(self, name):
        # Check if name is a string
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        # Check if name is 1 to 15 characters
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be 1 to 15 characters long!")
        self._name = name
        Customer.all_customer.append(self)  # Add customer to list

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # Check if name is a string
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        # Check if name is 1 to 15 characters
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be 1 to 15 characters long!")
        self._name = name  # Removed trailing comma

    def orders(self):
        # Return all orders for this customer
        customer_orders = []
        for order in Order.all_orders:  # Fixed: Use Order, not order
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

    def coffees(self):
        # Return unique coffees this customer ordered
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees

    def create_order(self, coffee, price):
        # Create a new order for this customer
        if not isinstance(coffee, Coffee):  # Fixed: Use Coffee, not coffee
            raise TypeError("Coffee must be a Coffee object!")
        new_order = Order(self, coffee, price)
        return new_order

# Test the code
customer = Customer("Neema")
print(customer.name)  # Should print: Neema