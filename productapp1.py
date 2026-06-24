# # #Keyboard product basic details
# brand= "Logitech"
# connection= "Wired"
# color= "Black"
# price= 1000
# stock= 10

# #using list to store colors
# typesof_colors=["red","green","white","black"]

# #using tuple for store brand names
# brand_types=("dell","hP","zebronics","apple")

# #using set to store connection types 
# connection_types={"wired","wireless","bluetooth"}

# # using dictionary to store prices
# keyboard_prices={
# "dell":1500,
# "hp":2000,
# "zebronics":2500,
# "apple":3000
# }
# # from data import *

# def display_details():
#     print("=====Keybooard Details======")
#     print("brand",brand)
#     print("connection type",connection)
#     print("color",color)
#     print("price",price)
#     print("avialble stock:",stock)
#     print("avialble colors:",typesof_colors)
#     print("avialble brands :",brand_types)
#     print("available connection types:",connection_types)
#     print("prices:",keyboard_prices)
# display_details()

# def check_stock():
#      if stock>0:
#         print("stock is available")
#      else:
#         print("out of stock")
# # check_stock()
#  #select keyboard brand and price
# # choose_keyboard=""
# # original_price=0
# # choose_color=""
# # type_c=""

# def select_keyboard():
#     global choose_keyboard,original_price
#     choose_keyboard=input("enter the brand name (dell,hP,zebronics):")
#     if choose_keyboard in keyboard_prices:
#         original_price=keyboard_prices[choose_keyboard]
#         print(f"you have selected {choose_keyboard} and price for {choose_keyboard} is {original_price}")
#     else:
#        print(" invalid brand")
# # select_keyboard()

# #select keyboard color
# def select_color():
#    global choose_color
#    choose_color=input("enter your keyboard color (red,green,white):")
#    if choose_color in typesof_colors:
#       print(f"you have selected :{choose_color} color keyboard")
#    else:
#       print("invalid color")
# # select_color()

# def select_conn_type():
#     global type_c
#     type_c=input("enter available connection types(wired,wireless,bluetooth) ")
#     if type_c in connection_types:
#        print(f"you have selected {type_c} keyboard")
#     else:
#        print("invalid connetion type")
# # select_connection_type()

# def ordered_details():
#     print(f"your ordered {choose_color} color keyboard {choose_keyboard} brand {type_c} type and price is {original_price}")
# ordered_details()

def loop_fun():
 while True:
    option = input("""select options :
                        1.display details :
                        2.select brand :
                        3.select color :
                        4.select connection type :
                        5.show your ordered details :
                        6.exit
                     Enter your option here: """  )
    if option =="1":
       print("product details are")
       display_details()
    elif option=="2":
       print(" you select brand here")
       select_keyboard()
    elif option=="3":
       print(" select color here")
       select_color()
    elif option=="4":
       print("select here connection type")
       select_conn_type()
    elif option=="5":
       print("Here what you have ordered")
       
       
   
      #  global choose_color,choose_keyboard,type_c,original_price
       ordered_details()
    elif option=="6":
       print("exiting_____")
       break
    else:
       print("Invalid input")
loop_fun()

#decorative fun
def my_decarator(fun):
    def wrapper():
     print("before function run")
    fun()
    print("after function run")
    return wrapper()
 
# multiple variable type arguements

def add_colors(*color1):
   typesof_colors.append(color1)
   return 
   
add_colors("blue","pink")
print("after adding colors",typesof_colors)

# multiple keyword arguements 
def add_prices(**multiprices):
   keyboard_prices.update(multiprices)
   print(keyboard_prices)
add_prices(brand_name="microsoft",price=3500,)
   


def main():
   print("=====display product details=====")
   display_details()
   print("=================================")
  
   print("====display the selected brand and its price=====")
   select_keyboard()
   print("===============================")
   
   print("display selected keyboard color")
   select_color()
   print("================================")

   print('======display keyboard type=======')
   select_conn_type()
   print("======================")
   
   print("=====display the  ordered details====")
   ordered_details()
   print("======================")
   
   # loop_fun()

   
   # add_prices(brand_name="microsoft",price=3500,)

   
if __name__ == "__main__":
   main()
                       
                   
   

   


