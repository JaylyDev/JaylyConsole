import json

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
if json_client_name == py_client_name:
 print("Client name: Correct")
else:
 print("Client name: Incorrect")
if json_client_description = py_client_description:
if json_client_uuid = py_client_uuid:
if json_client_version = py_client_versuin
   for json_manifest_tokens in manifest_json['token']:
if json_manifest_token_main == py_manifest_token_main:
 else if json_manifest_token_backup == py_manifest_token_backup:
  else:
