import json
import os.path

if os.path.isfile('profiles.json'):
    print ("User profiles exist")
    with open('profiles.json') as jc_profiles_file:
    jc_profiles = json.load(jc_profiles_file)
    for users in jc_profiles['profile']:
        
else:
    print ("User profiles do not exist")
