# class mydetials:
#       name="naveen"
#       emial_id="naveen@123gmail.com"
#       phone_no=9111100000
      
# user1=mydetials()
# print(user1.name)
# print(user1.phone_no)
# user2=mydetials()
# user2.name="virat"
# user2.phone_no=9000011001
# print(user2.name)
# print(user2.phone_no)

# class Student:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
# s1=Student("naveen",22)
# print(s1.name)
# print(s1.age)   
# print(s1.__dict__)                

# class adding:
#       def add(self,a,b):
#           print(a+b)
# c=adding()
# c.add(3,2)

# class car:
#       color="red"
#       speed=200
#       accelerate=[]
#       def accelerate_car(self,*speed):
#             self.accelerate.append(speed)
#             print("acceleration",self.accelerate)
            
# car1=car()
# print(car1.color)
# car1.accelerate_car(10,20,30)

# class Student:
#       name="Naveen"
#       marks=90
#       def grades(self,marks):
#             if marks>=90 and marks <=100:
#                   print("grade A")
#             elif marks>70 and marks<90:
#                   print("grade B")
#             else:
#                   print("grade C")
# s1=Student()
# s1.grades(95)
# s1.grades(89)

# # creating bank account class with balance withdraw(),deposite() method
# class Bank_Account:
#       def __init__(self,balance=0):
#             self.balance=balance
#       def deposite(self,amount):
#             self.balance+=amount
#             print("deposited:",amount)
#             print("current balance",self.balance)
            
#       def withdraw(self,amount):
#              if amount>self.balance:
#                   print("insufficient balance")
#              else:
#                   self.balance-=amount
#                   print("withdraw amount",amount)
#                   print("current balance",self.balance)
            
            
# account1=Bank_Account()
# account1.deposite(10000)
# account1.withdraw(900)
#  #creating __str__ method
# class A:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
            
#       def __str__(self):
#             return f"user name: {self.name},'\n' age: {self.age}"
# a1=A("naveen",22)
# print(a1)
# class Book:
#       def __init__(self,title,author,price):
#             self.title=title
#             self.author=author
#             self.price =price
            
#       def __str__(self):
#             return f"{self.title} by {self.author} clear cost {self.price}"
      
# class User:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
#       def __repr__(self):
#             return f"user name: {self.name},age: {self.age}"
# u1=User("naveen",20)
# print(dir(u1))
            
# b1=Book("atomic habits ","james",499)
# # print(b1)

# class is_prime:
#       @staticmethod
#       def prime(a):
#             count=0
#             for i in range(1,a+1):
#                 if(a%i==0):
#                   count+=1
            
#             if count==2:
#                   print("prime",a)
#             else:
#                   print("it is not prime",a)
# print(is_prime.prime(7))

# class Hours_to_min:
#       @staticmethod
#       def hours():
#             h=int(input("Enter a num: "))
#             return h*60
# print(Hours_to_min.hours())

# class product:
#       def __init__(self,name,age,height_cm):
#             self.name=name
#             self.age=age
#             self.height_cm=height_cm
#             self.measurements={}
#             self.cart=[]
#             is_premium=False
#       def add_measurements(self, key,value):
#             self.measurements[key]=value
#             print(f"added {key}:{value} cm for {self.name}")
#       def add_cart(self,product_name):
#             self.product_name=product_name
#             self.cart.append(product_name)
#             print(f"{self.name}  added {product_name} to cart")
#       def get_summary(self):
#             if not self.cart:
#                   return "cart is empty"
#             return f"{self.name}, cart: {','.join(self.cart)}"
# p1=product("naveen",22,170)
# p1.add_measurements("chest",20)
# p1.add_measurements("waist",20)
# p1.add_cart("pink shirt")
# p1.add_cart("iphone")
# p1.add_cart("redmi")
# print(p1.get_summary())

# class number:
#       def __init__(self,a):
#             self.a=a
#             # self.b=b
#       def __add__(self,b):
#             # c=self.a+self.b
#             return self.a+b.a
#       def __and__(self, other):
#             return self.a and other.a
#       def __eq__(self, value):
#             return self.a==value.a
# n1=number(5)
# n2=number(5)
# print(n1+n2)
# print(n1&n2)
# print(n1==n2)

#inheritance  
#create a Animal class with eat() method  and creata a dog class that inherit add bark
# class Animal:
#       def eat(self):
#             print("animal can eat food")
# class dog(Animal):
#       def bark(self):
#             print("dog can bark")
# d=dog()
# d.bark()
# d.eat()
# # make a vehicle with speed and move() create a car that inherit and overide move()
# class Vehicle:
#       def __init__(self,speed):
#             self.speed=speed
#       def move(self):
#             print("car moving with speed :",self.speed)
# class Car(Vehicle):
#       def move(self):
#             print(f"car driving speed {self.speed} km/h")
# v=Vehicle(50)
# v.move()
# car=Car(80)
# car.move()

# method overriding

# class Shape:
#       def area(self):
#             print("area methods should be implemented by child classes")
# class Rectangle(Shape):
#       def __init__(self,length,width):
#             self.length=length
#             self.width=width
#       def area(self):
#             print("area of rectangle:",self.length*self.width)
# class Circle(Shape):
#       def __init__(self,radius):
#             self.radius=radius
#       def area(self):
#             print(f"area of circle :{3.14*self.radius*self.radius}") 
# r=Rectangle(5,6)
# r.area()
# c=Circle(3)     
# c.area()
# create a employee with name salary create a manager that inherits add bonus
# class Employee:
#       def __init__(self,name,salary):
#             self.name=name
#             self.salary=salary
#       def employe_info(self):
#             print(f"employe name:{self.name} and his salary:{self.salary}")
# class Manager(Employee):
#       def __init__(self,name,salary,bonus):
#             super().__init__(name,salary)
#             self.bonus=bonus
#       def manager_info(self):
#             self.salary=self.salary+self.bonus
#             print(f"manager name:{self.name} and his salary:{self.salary}")

# e=Employee("ashish",24000)
# e.employe_info()
# m=Manager("vikram",40000,5000)
# m.manager_info()

# create a bankaccount with balance deposite() withdraw and create saving account that adds intrest
# class Bankaccount:
#       def __init__(self,balance):
#             self.balance=balance
#       def deposite(self,amount):
#             self.amount=amount
#             self.balance=self.balance+amount
#             print(f"deposited:{self.amount}")
#             print(f"current balance:{self.balance}")
#       def withdraw(self,amount):
#             self.amount=amount
#             if amount>self.balance:
#                   print("balance is low")
#             else:
#                   self.balance=self.balance-amount
#                   print(f"amount withdrawed:{amount}")
#                   print(f"current balance:{self.balance}")
# class SavingAccount(Bankaccount):
#       def add_interest(self,rate):
#             interest=self.balance*(rate/100)
#             self.balance=self.balance+interest
#             print(f"interest interest{interest}")
#             print(f"new balance :{self.balance} ")
# b=Bankaccount(20000)
# b.deposite(5000)
# b.withdraw(5000)
# s=SavingAccount(20000)
# s.deposite(5000)
# s.withdraw(5000)
# s.add_interest(2)

#create a product with a private and property to get/set price(prevent negative)
class product:
      def __init__(self,price):
            self.__price=price
      @property
      def price(self):
            return self.__price
      @price.setter
      def price(self,value):
            if value>0:
               self.__price=value
            else:
                  print("price can not be negative")
p=product(50)
print(p.price)
p.price=-60
print(p.price)
            

#Polymorphism
# class Animal:
#       def eat(self):
#             return "animal can eat"
# class tiger(Animal):
#       def eat(self):
#             return "tiger eat animals"
# class cow(Animal):
#       def eat(self):
#             print("cow eat grass")
# t=tiger()
# c=cow()
# c.eat()
# print(t.eat())
