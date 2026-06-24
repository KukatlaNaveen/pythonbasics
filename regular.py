import re
pin="1234a"
if re.fullmatch(r'\d{4}',pin):
   print("valid pin",pin)
else:
   print("invalide pin",pin)
   
mail_id="naveen123.@gmail.co.com"
if re.fullmatch(r'^[\w\.]+@[\w\.]+\.\w+$',mail_id):
    print("valid mail",mail_id)
else:
   print(mail_id,"not valid")
   
string="12345"
# pattern=re.match(r'\d')
if re.fullmatch(r'\d{5}',string):
   print(True)
else:
   print(False)
numbers="803450345"
if re.fullmatch(r'\d{10}',numbers):
   print(numbers)
else:
  print("wrong number")
data="contact me at test1@gmail.com and admin@yahoo.com an umbrells"
res=re.findall(r'[\w\.]+@[\w\.]+\.\w+',data)
print(res)
# rep=re.sub("navee@gmail.com",res)
# print(rep)
text ="I have 2 cars 13 bikes 10 and 1 house "
patern=re.findall(r'\d+',text,)
print(patern)
a="Regular Expressions and A e i o"
solution=re.findall(r'[aeiou]',a,re.IGNORECASE)
print(len(solution))
