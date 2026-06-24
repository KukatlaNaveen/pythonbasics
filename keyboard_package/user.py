import re
import json
class User:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def register(self):
        if re.fullmatch(r'\d{4,}',self.password):
            print(f"User name:{self.name},")
            print(f"User password:{self.password}")
        else:
            print("password is not maatched",self.password)
user1=User("naveen","123456789")
user1.register()

class Auth(User):
    file="user.json"
    
    def register(self):
        try:
         with open(self.file, "r") as f:
            users = json.load(f)
        except:
         users = {}

    
