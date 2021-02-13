# Name: Jayly Console
# Credit: JaylyMC
# Console Version: 1.4
# Launcher Version: 1.0
import json

#Open manifest file
with open(r"System\Launcher\manifest.json", "r") as manifest_import:
    json_manifest = json.load(manifest_import)
    # Stored data from python
    py_manifest = json.loads("""
{
    "format_version": 1,
    "header": {
        "description": "n/a",
        "name": "Jayly Console",
        "uuid": "9a88798c-8385-4152-bfcd-3d5378a54205",
        "version": [ 1, 4, 0 ]
    },
    "authentication": [
        {
            "type": "main",
	    "token": "9HvkEVft2Nb5sD7Zdh3V4dUG3XMFxeUH"
        },
	{
            "type": "backup",
	    "token": "LJt5VH7qzVwZBQPa5fWFvzqQGxk7BuHT"
        }
    ]
}
""")
    # Json and python compare
    if json_manifest == py_manifest:
        print("Verified Jayly Console's manifest.")
        print("Installing Login Service.")
        print("")
        import System.Profiles.login
    else:
        print("Unable to verify Jayly Console's manifest, please import the original one")
        print("Press ENTER to exit the console.")
        #Exit Console
        exit = input()
