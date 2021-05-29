class User():
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def describe_user(self):
        full_name=self.first_name.title()+" "+self.last_name.title()
        return full_name
       
    def greet_user(self):
        print("Good Morning "+self.first_name.title()+"!")

