from cars import Car

class Battery():
    """A simple way to model abattery from an electric car."""

    def __init__(self,battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size=battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        
        message="this car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class EletricCar(Car): # Child Class
    """Represent aspects of a car,specific to eletric vechiles."""

    def __init__(self,make,model,year):
        """Initialize attributes if the parent cass.
       Then initialize attributes specific to an electric car."""
        super().__init__(make,model,year)
        self.battery=Battery()
    
