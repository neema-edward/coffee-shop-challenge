class Customer:
    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            print("Name must be a string!")
            return
        
        if len(name) < 1 or len(name) > 15:
            print("Number should be 1 to 15 characters long!")
            return
        
        
