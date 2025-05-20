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
        return self.coffee.upper()
    
    @name.setter
    def name(self, new_coffee):
        if isinstance (new_coffee, str):
            self.coffee = new_coffee
        else:
            raise ValueError("Not a string!!")
    
order = Order("Neema", "Mocha", 7.8)
print(order.coffee)
order.coffee = "Cappucino"
print(order.coffee)