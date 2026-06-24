from data import *
def check_stock():
     if stock>0:
        print("stock is available")
     else:
        print("out of stock")
check_stock()


def add_stock(new_stock):
      
       try:
         global stock 
         new_stock=int(new_stock)
         if stock < minimum:
            print(" before adding stock",stock)
               # if new_stock>0:
            stock=stock+new_stock
            print("after adding stock",stock)
         else:
                print(" stock avilable")
       
       except ValueError as e:
          print(f"valueerror caught :{e}")
       except TypeError as e:
          print(f"typeerror caught:{e}")
       except ZeroDivisionError as e:
          print(f"zerodivision error caught:{e}")
       except Exception as e:
          print(f"error caught:  {e}")
       finally:
          print("sucessfully completed")
               
add_stock(23)

class Stockislow(Exception):
   pass
class userisnotactive(Exception):
   pass


def stock_status():
   if is_active == 1 and stock>0:
      print("user is  active and stock is sufficient")
   if stock==0:
      raise Stockislow("stock is low")
   if is_active==0:
      raise userisnotactive("user is not active")

      

try:
   stock_status()
except Stockislow as e:
   print("stockislow error caught:",e)
except userisnotactive as e:
   print("userisnotactive error caught: ",e)
except Exception as e:
   print("error caught :",e)
finally:
   print("stock status function completed")
   