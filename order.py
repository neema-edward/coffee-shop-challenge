class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

        if not isinstance (price, float):
            raise TypeError("Price is not float!")
            
        if price < 1.0 or price > 10.0:
            raise TypeError("Price is off range")
        
    @property
    def price(self):
        return self.price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    
order = Order("Neema", "Mocha", 7.8)
print(order.price)
order.price = "8.0"
print(order.price)



 



