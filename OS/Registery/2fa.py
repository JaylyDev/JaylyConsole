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
  manifest_source = json.loads(manifest_py)
  for manifest_json in manifest_data['client']:
   json_client_name = manifest_json['name']
   json_client_description = manifest_json['description']
   json_client_uuid = manifest_json['uuid']
   json_client_version = manifest_json['version']
   for json_manifest_tokens in manifest_json['token']:
    json_manifest_token_main = json_manifest_tokens['main']
    json_manifest_token_backup = json_manifest_tokens['backup']
