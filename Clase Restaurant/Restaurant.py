class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"El restaurant llamado {self.restaurant_name} es del tipo {self.cuisine_type}")
    def open_restaurant(self):
        print("El restaurant esta abierto")
    def set_number_served(self,number_served):
        self.number_served=number_served
    def increment_number_served(self,increment):
        self.number_served+=increment

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        #Restaurant(restaurant_name,cuisine_type)
        self.flavors=["choco","frutilla","naranja"]
    def show_flavors(self):
        print("Los sabores de helados son: "+str(self.flavors))







class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print(f'El usuario se llama: {self.first_name} {self.last_name}') 
    def greet_user(self):
        print(f"Bienvenido {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attemps(self):
        self.login_attempts=0


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()


class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(f"Los privilegios de Admin son: {str(self.privileges)} ")    


