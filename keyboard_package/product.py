# from data import*
#creating product class and diplay product details
class Product:
     def __init__(self,name,brand,color,price):
          self.name=name
          self.brand= brand
          self.color=color
          self.price =price
          self.stock= 10

     def display_details(self):
        print("=====Product  Details======")
        print("Product Name:",self.name)
        print("brand",self.brand)
        print("color",self.color)
        print("price",self.price)
        print("avialble stock:",self.stock)
p1=Product("mobile","moto","black",20000)
p1.display_details()