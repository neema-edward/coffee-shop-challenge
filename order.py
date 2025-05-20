from coffee import Coffee
from customer import Customer


class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

        if not isinstance (price, float):
            raise TypeError("Price is not float!")
            
        if price < 1.0 or price > 10.0:
            raise TypeError("Price is off range")
        
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer object!")
        
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee object!")
        
    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    




 



