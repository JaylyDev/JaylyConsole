import json
import numpy

# manifest_py stores manifest data
manifest_py = """
{
 "client": [
   {
     "name": "JaylyConsole",
     "description": "client.description",
     "uuid": "5cc14a47-dbbc-4303-b498-6bbadc89a599",
     "has_license": true,
     "version": [1, 4, 0],
     "token": [ 
      "main": "5AvRkrf36UU4bHBX", 
      "backup": "vGAh6DeGTZ2RYCUE" 
     ]
   }
  ]
}
"""

# Opening the manifests
with open(r"manifest.json", "r") as manifest_data:
  manifest_json = json.loads(manifest_data)
  for manifest_json in manifest_data['client']:
   json_client_name = manifest_json['name']
   json_client_description = manifest_json['description']
   json_client_uuid = manifest_json['uuid']
   json_client_version = manifest_json['version']
   for json_manifest_tokens in manifest_json['token']:
    json_manifest_token_main = json_manifest_tokens['main']
    json_manifest_token_backup = json_manifest_tokens['backup']

manifest_source = json.loads(manifest_py)
  for py_manifest in manifest_source['client']:
   py_client_name = manifest_source['name']
   py_client_description = manifest_source['description']
   py_client_uuid = manifest_source['uuid']
   py_client_version = manifest_source['version']
   for py_manifest_tokens in manifest_source['token']:
    py_manifest_token_main = py_manifest_tokens['main']
    py_manifest_token_backup = py_manifest_tokens['backup']

# Compare the modules
error = 0 # Default error number
if json_client_name == py_client_name:
 print("Client name: Correct")
else:
 print("Client name: Incorrect")
 error1 = 101
if json_client_description = py_client_description:
 print("Client description: Correct")
else:
 print("Client description: Incorrect")
 error2 = 212
if json_client_uuid = py_client_uuid:
 print("Client description: Correct")
else:
 print("Client description: Incorrect")
 error3 = 323
if json_client_version = py_client_version:
 print("Client version: Correct")
else:
 print("Client version: Incorrect")
 error4 = 434
if json_manifest_token_main == py_manifest_token_main:
 print("Client token [main]: Correct")
 else:
  print("Incorrect client token, searching for backup client token...")
  error5 = 545
  if json_manifest_token_backup == py_manifest_token_backup:
   print("Client token [backup]: Correct")
   jcregistery_confirmation = true
   jcregistery_errorcode = float(error1) + float(error2) + float(error3) + float(error4) + float(error5)
  else:
   print("Unable to verify main and backup client token")
   
# Redirecting from 2fa.py to login.py
if jcregistery_confirmation == true:
 if jcregistery_errorcode =! 0:
  print("WARNING: JaylyConsole detects the metadata of JaylyConsole is different compared to the original.")
  print("Here is the Error code: " + str(jcregistery_errorcode))
 import login
else:
 print("""
 JaylyConsole is unable to verify the metadata of its application.
 Press \"Enter\" to shut down JaylyConsole.
 """)
