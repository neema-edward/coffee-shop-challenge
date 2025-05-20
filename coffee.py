class Coffee:
    def __init__(self, name):
        self.name = name
        if not isinstance (name, str):
            print("Must be a string!")
        
        if len(name) < 3:
            raise TypeError("Should be atleast 3 characters long!")
        
coffee1 = Coffee("Mocha")
print(coffee1.name)
