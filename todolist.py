def To_do_list():
    tasks=[]
    
    while True:
      print("""
               1: add taks
               2: remove task    
               3: show task    
               4:quit""")
      choice =input("Enter your option :")
      if choice=="1":
         task=input("enter your task ")
         tasks.append(task)
      elif choice=="2":
          task=input("enter task to remove ")
          if task in tasks:
             tasks.remove(task)
          else:
             print("task is not found 1")
      elif choice=="3":
           print("tasks")
           for task in tasks:
                    print("--",task)
      elif choice==4:
           break
      else:
           print("invalid input")
To_do_list()
                    
          