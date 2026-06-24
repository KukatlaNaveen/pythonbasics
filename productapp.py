#product information using dictionary
vehicle_details= { 
  "product":"car",
  "vehicle_name":"Toyota",
  "vehicle_color":"white",
  "model_year":"2025", 
  "price": 1500000,
  "current_stock":10           
} 
minimum_stock=15
stock=minimum_stock-vehicle_details["current_stock"]
#display vehicle_details
# print("vehicle_details",vehicle_details)

available_models=["2010","2015","2020","2025"]

#display available models
# print("available_models",available_models)

#add availabel model using function
def add_model():
     new_model=input("enter the model year ")
     print(" before add availabel models ", available_models)
     available_models.append(new_model)
     print("after add availabel models are:",available_models)
# add_model()
    
# deduct model from availabel models
def remove_model():
    old_model=input("enter the remove availabel model ")
    print("before remove model year",available_models)
    available_models.remove(old_model)
    print("after remove model year",available_models)
# remove_model()

# create show room credentials using tuple
showroom_cred=("password123","password231","password321")
# print(showroom_cred)
# print(type(showroom_cred))

# 
# #just get a first  password from showroom credentials
def get_password():
    showroom_password=showroom_cred[0]
    print("first password from credentials:",showroom_cred[0])
# get_password()

# #add a password into the show room  credentials
def add_password():
    global showroom_cred
    temp_list=list(showroom_cred)
    temp_list.append("password789")
    showroom_cred=tuple(temp_list)
    print("after add password credentials-->",showroom_cred)
# add_password()

# # warehouses locations using set
product_loactions={"warehose_A","warehose_B","warehouse_C"}
# print("warehouse locations are:",product_loactions)
# print(type(product_loactions))

  #just check the alert stock
def check_current_stock():
    global product_details
    if(vehicle_details['current_stock']<=minimum_stock):
        print(" Alert ! stock is low",vehicle_details['current_stock'])
#check_current_stock()
    
# #calculate reorder 

def calculate_reorder_level():
    
     if(vehicle_details['current_stock']<=minimum_stock):
        print(f"we need add  stock {stock}") 
     else:
         print("stock is availabel")
# calculate_reorder_level() 
 
def add_stock():
     global number
     number =int(input("enter a number "))
     vehicle_details.update({"current_stock":number}) 
     print("add stock to the current stock",vehicle_details["current_stock"])   
# add_stock()

#updated vehicle details
def display_updated_details():
     print("vehicle details are -->",vehicle_details)
     print(f"available_models-->:{available_models} \n show room credentials-->:{showroom_cred}\n product locations-->: {product_loactions}")
# display_updated_details()
def main():
    print("======adding vehicle model year =======\n")
    add_model()
    print("===============================")
    print("-------remove vehicle model which is avialable in list--------\n")
    remove_model()
    print("---------------------------")
    
    print("======get password======\n")
    get_password()
    print("========================")
    
    print("-------add password--------\n")
    add_password()
    print("---------------------------")
    
    print("===========check current stock============\n")
    check_current_stock()
    print("========================")
    
    print("===========calculate reorder level=============\n")
    calculate_reorder_level()
    print("========================")
    
    print("==============adding stock==========\n")
    add_stock()
    print("========================")
    
    print("=======update details=================\n")
    display_updated_details()
    
if __name__ == "__main__":main()


    
     