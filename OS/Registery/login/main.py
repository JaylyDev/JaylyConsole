import json
try:
    jc_login = open(r'profiles.json', 'r')
    json.loads(jc_login)
    jc_openfile = true
except FileNotFoundError:
    print("User profile does not exist.")
    jc_openfile = false
    
if jc_openfile == true:
    # Input the item name that you want to search
    jc_username = input("Enter your username: ")
    
    # Define a function to search the item
    def profiles (username):
      for user in profiles:
        if name.lower() == keyval['name'].lower():
          return user['unit_price']
     
    # Check the return value and print message
    if (profiles(username) != None):
      print("Welcome ", profiles(username))
      jc_password = input("Enter your password: ")
    else:
      print("User is not found")
