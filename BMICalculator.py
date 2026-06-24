#basic details of the user
for i in range(1,3):  
  name=input("enter your name ")
  weight=float(input("enter your weight "))
  height=float(input("enter your height "))
  record=[name,weight,height]
  print(" Person",i,record,)
  bmi=weight/(height*height)
  print(bmi)
  if bmi<20:
    print("underweight")
  elif bmi>20 and bmi<35:
    print("normal")
  else:
    print("overweight")
# print(record)

#here defined a fun to calculate bmi(body mass index)
# for i in range(1,3):

#
