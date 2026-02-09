#create a list of 5 product and print them with numbers
products=["chair","laptop","Buds","laptop","keyboard","mouse"]
# for i, item in enumerate(products, 1):
#     print(f"{i}, {item}") 
    
# operations in list
# adding products to the product list
products.append("mobile")
products.insert(0,"iphone")
# print(products)
# tem_list=[2,3,1,4,5]
# tem_list.extend(products)
# print(tem_list)
# for i in range(5):
#     print(tem_list[i])
# products.sort()
# sorted(products)
# products.reverse()
# new=products.copy()
# new=products[:]
# print(new)    
# Add "watch" to the end and "tie" to the beginning of the list
products.append("watch")
products.insert(0,"tie")
 
# Remove the second item and print the updated lis
products.remove("mobile")
print(products)
# product="shoes"
# # Check if "shoes" is in the list and print "Available" or "Not found".

if "laptop" in products:
   print("availabel")
else:
  print("not availabel")
# products.reverse()
# print(products)
#     #  Sort a list of prices [1200, 800, 1500, 999] in ascending order
# prices= [1200, 800, 1500, 999]
# prices.sort()
# # prices.reverse()
# count=1
# print(prices)
# # Count how many times "shirt" appears in the list
# for i in products:
#     products.count("laptop")
#     print("laptop")
x=products.count("laptop")
print(x)

# Create a list from user input (ask 3 times and append)
# lst=[]
# name=input("enter your name ")
# # print(f"heelo {name}")
# color=input("enter your fav color ")
# # print(f"my fav color is{color}")
# animal=input("enter your fav animal ")
# # print(f"my fav animal is{animal}")
# lst.append(name)
# lst.append(color)
# lst.append(animal)
# print("list of elements",lst)

# Make a copy of the list and add a new item to the copy only
# naya=products.copy()
# naya.append("bulb")
# print(naya)

# Print only items that start with "B" (use loop – preview)

if "B" in products:
    print("yes")
    