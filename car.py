class Car(): # Parent Class
    """ A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model=model
        self.year=year
        self.odometer_reading =0
    
    def get_descriptive(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name
    
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")
    
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back on odometer.")
    
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

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
    
