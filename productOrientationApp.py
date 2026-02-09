#product information
product_info= {
      "name":"laptop",
      "category": "Electronics",
      "sku": "LPA123",
      "current_stock":100
}

#using list for stock
inventory_history=[100,50,75,120,45] 

   #using tuple for supplier pins
supplier_cred = ("sup123","sup321")

warehouse_locat={'warehouse1','warehouse2','warehouse3'}
print("inventory_history =",inventory_history)

#add / deduct stock
def update_stock(change):
    product_info["current_stock"]+=change
    inventory_history.append(product_info)
                    
                    
#add stock   
update_stock(100)
#deduct stock
update_stock(-50)

#  print(inventory_history)
#Reorder level calculation

def calculate_reorder_level():
      avg_stock=sum(inventory_history)/len(inventory_history)
      return(avg_stock * 0.5)

      reorder_level = calculate_reorder_level()
#low stock alert
def check_low_stock(threshold=60):
  if product_info["current_stock"] < threshold:
                     print("Alert : Stock is low")
  else:
    print("Stock is suffiecent")
                                        
# Final product info
print("\nFinal product info:") 
for key, value in product_info.items():
 print(f"{key}: {value}")
                                        
                                        
print("\nsupplier credentials:")
print(supplier_cred)
                                        
print("\nwarehouse locations:")
print(warehouse_locat)
                                        
print("\nReorder level:", calculate_reorder_level)
                                        
check_low_stock()
                                                          
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                     

                                        
                                        
                                        
                    
   
                    



