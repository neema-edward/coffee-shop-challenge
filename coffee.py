class Coffee:
    def __init__(self, name):

        if not isinstance (name, str):
            print("Must be a string!")
        
        if len(name) < 3:
            raise TypeError("Should be atleast 3 characters long!")
        self._name = name
    @property
    def name(self):
        return self._name
    
    def orders(self):
        coffee_orders = []
        for order in order.all_orders:
            if order.coffee == self:
                coffee_orders.append(order)
        return coffee_orders

    def customers(self):
        customers = []
        for order in self.orders():
            if order.customer not in customers:
                customers.append(order.customer)
        return customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = 0
        for order in orders:
            total_price += order.price
        return total_price / len(orders)
    
coffee1 = Coffee("Latte")
print(coffee1.name)

