import json
import os
import os.path

if os.path.isfile('profiles.json'):
    print ("User profiles exist")
    with open('profiles.json') as jc_profiles_file:
        try:
            jc_profiles = json.load(jc_profiles_file)
            jc_client_username = input("Enter your username here: ")
            jc_client_password = input("Enter your password here: ")
            jc_client_username = jc_client_username.lower()
            for client in jc_profiles['profiles']:
                if client['username'] == jc_client_username:
                    user_password = return client['password']
                    if user_password == jc_client_password:
                        print("Correct login details")
                        print("Welcome " + jc_client_username)
                        print("Preparing your console...")
                        # Program redirects you to "JaylyConsole/Desktop/" folder
                        root_path = '/JaylyConsole/OS/Console/User/'
                        folders = ['Folder_1','Folder_x','Folder_y']
                        for folder in folders:
                            os.mkdir(os.path.join(root_path,folder))
                    else:
                        print("Incorrect username or password.")
                else:
                    print("Incorrect username or password.")
        except:
            print("Unable to convert profiles data to JSON")
else:
    print ("User profiles do not exist")
