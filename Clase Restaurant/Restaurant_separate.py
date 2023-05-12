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