#Online Shopping System (Multilevel Inheritance)#
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, brand):
        super().__init__(name, price, warranty)
        self.brand = brand

    def display(self):
        print(self.name, self.price, self.warranty, self.brand)

m = MobilePhone("Phone", 20000, "1 Year", "Samsung")
m.display()