from user_separate import User


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()


class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(f"Los privilegios de Admin son: {str(self.privileges)} ")    

