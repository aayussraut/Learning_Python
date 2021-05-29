class Restaurant():
    
    def __init__(self,restautant_name,cuisine_type):
        self.restautant_name=restautant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print("Our "+self.restautant_name+"has a best ever "+self.cuisine_type+" that you have never ate in your life.")
    
    def open_restaurant(self):
        print(self.restautant_name+" is open")


class IceCreamStand(Restaurant):

    def __init__(self,restautant_name,cuisine_type='ice cream'):
        super().__init__(restautant_name,cuisine_type)
        self.flavors=['Chocolate','Vanilla','Stawberry']
    
    def icecream_flavors(self):
        print("The famous ice cream here are: ")
        for icecream in self.flavors:
            print(icecream)