class Customer:
    def __init__(self, name):
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
            
        
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Number should be 1 to 15 characters long!")
            
        self._name = name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance (name, str, len<16 or len>0):
            self._name = name,

        else:
            raise TypeError("Name must be a string!")
        

# customer = Customer("Neema")
# print(customer.name)
        

