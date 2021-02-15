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
