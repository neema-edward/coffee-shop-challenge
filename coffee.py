class Coffee:
    def __init__(self, name):
        self.name = name
        if not isinstance (name, str):
            print("Must be a string!")
            return
        
        if len(name) < 3:
            print("Should be atleast 3 characters long!")
            return
# coffee1 = Coffee("Mo")
# print(coffee1.name)
