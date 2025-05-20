class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        if not isinstance (price, float):
            raise TypeError("Price is not float!")
            
        if price < 1.0 or price > 10.0:
            raise TypeError("Price is off range")
        
    @property
    def name(self):
        return self.price
    
    @name.setter
    def name(self, new_coffee):
        if isinstance (new_coffee, str):
            self.coffee = new_coffee
        else:
            raise ValueError("Not a string!!")
    
order = Order("Neema", "Mocha", 7.8)
print(order.price)
order.price = "8.0"
print(order.price)