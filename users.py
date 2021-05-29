class User():
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def describe_user(self):
        full_name=self.first_name.title()+" "+self.last_name.title()
        return full_name
       
    def greet_user(self):
        print("Good Morning "+self.first_name.title()+"!")

class Privileges():
    def __init__(self):
        self.privileges=['can delete post','can add post','can ban user','can edit post']    
    
    def show_privileges(self):
        for privileges in self.privileges:
            print("Admin "+privileges)

class Admin(User):

    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()