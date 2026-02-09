# Create a tuple of 5 colors and print the second one
colors=("red","blue","black","white","green")
print(colors[1])
# Unpack a tuple (name, age, city) into three variables and print them
product=("naveen",21,"dharmaram")
name,age,city=product
print(f"my name is {name} iam {age} years old and my city is {city}")

# Check if "red" is in a color tuple.
if "red" in colors:
   print("yes")
else:
   print("no")
# Count how many times 1 appears in (1,2,1,3,1)
numbers=(1,2,1,3,1)
cancat=numbers+(5,)
print(cancat)
cnt=numbers.count(1)
print(cnt)

# Find the index of "cap" in ("shirt", "cap", "watch").
prdct=("shirt","t-shirt","cap", "watch")
indx=prdct.index("cap")
print(indx)

# Check length of a tuple and print "Empty" if len == 0
temp_tuple=()
print(len(temp_tuple)) 
if temp_tuple==0:
   print("empty")
   
#    Use a tuple as key in a dictionary to store stock (product, size) → quantity
store_stock={
("shirt","t-shirt"):"product",
("S","L") : "size",
(12,20):"quantity"
}
print(store_stock[(12,20)])
# Create a tuple of coordinates (x, y) and print "Point: (x,y)"
