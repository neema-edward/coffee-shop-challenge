class Customer:
    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            print("Name must be a string")
            return
        
        
