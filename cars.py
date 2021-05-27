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

