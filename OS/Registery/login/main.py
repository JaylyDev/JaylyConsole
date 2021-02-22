import json
import os.path

if os.path.isfile('profiles.json'):
    print ("User profiles exist")
    with open('profiles.json') as jc_profiles_file:
        try:
            jc_profiles = json.load(jc_profiles_file)
            jc_client_username = input("Enter your username here: ")
            jc_client_password = input("Enter your password here: ")
            jc_client_username = jc_client_username.lower()
            for users in jc_profiles['profiles']:
                if users['username'] == jc_client_username:
                    print("Found a match of your username.")
                    print(jc_client_username)
                    for passwords in jc_client:
                else:
                    print("Incorrect username or password.")
        except:
            print("Unable to convert profiles data to JSON")
else:
    print ("User profiles do not exist")
