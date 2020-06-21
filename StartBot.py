import sys
import json

from Modules.__init__ import WindowSelectCharacter

'''
    The Main Init Throws You Into The Character Selection Window In Modules On __init__.py...
    Take A Look Over There
'''

if __name__ == '__main__':
    with open('Scripts/Loads.json', 'r') as LoadsJson:
        data = json.load(LoadsJson)

    if len(sys.argv) == 1:
        data['Platform'] = "Windows"
        with open('Scripts/Loads.json', 'w') as wJson:
            json.dump(data, wJson, indent=4)

    elif len(sys.argv) == 2:
        if sys.argv[1] == 'linux-client':
            data['Platform'] = "Linux"
            with open('Scripts/Loads.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)

    WindowSelectCharacter()
