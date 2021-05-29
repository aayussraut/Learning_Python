from user import User

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