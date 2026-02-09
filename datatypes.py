#all data types in python
a=10
b=2.5
c="python"
li=[1,2,3]
tu=("apple","banana","grapes")
di={"name":"lilliput","age":20,"gender":"male"}
print(type(a))
print(type(b))
print(type(c))
print(type(li))
print(type(tu))
print(type(di))

# boolean creating variables 
is_adult=False
has_money=True
is_weekend=True
a=has_money
a=False
has_money=a
if(is_adult or has_money and is_weekend):
   print("person can go to movie")
else:
   print("person can't go to movie")
   
   
# prblm on age 
age=int(input("enter the age "))
if age>=18:
   print("major")
else:
   print("minor")
   
#check number is + - or 0
num=int(input("enter a number "))
if(num>0):
   print("positive")
elif num<0:
   print("negative")
else:
   print("the number is zero")
   
   #boolean
is_stock=True
is_size=True
if(is_stock and is_size):
   print("can buy")
password=1345
byte_password = password.to_bytes(2)
print(byte_password)
print(type(byte_password))


 