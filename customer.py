from coffee import Coffee
from order import Order


class Customer:

    all_customer = []

    def __init__(self, name):
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
            
        
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name should be 1 to 15 characters long!")
            
        self._name = name
        Customer.all_customer.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be 1 to 15 characters long!")
        
        self._name = name

    
    def orders(self):
        customer_orders = []
        for order in Order.all_orders:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

    def coffees(self):
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee object!")
        new_order = Order(self, coffee, price)
        return new_order

customer = Customer("Neema")
print(customer.name)
        

