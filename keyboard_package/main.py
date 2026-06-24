

from user import *
def main():
   
   
   while True:
      print("""
                1.register
                2.login
                3.show user details
            """)
      choice=input("Enter your choice ")
      
      if choice=='1':
         name1=input("Enter user name:")
         password1=input("Enter your password 1")
         user1=User(name1,password1)
         user1.get_user_info()
         
if __name__ == "__main__":
   main()
                       
                   
   

   


