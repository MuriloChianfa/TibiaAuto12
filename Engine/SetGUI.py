import json


def GetData():
    with open("Scripts/GUILoader.json", 'r') as LoadsJson:
        data = json.load(LoadsJson)

    return data


class SetGUI:
    def __init__(self, Locate):
        self.Locate = Locate

    def GetBoolVar(self, VarName):
        if GetData()['Loaders'][self.Locate][VarName]:
            return True
        else:
            return False

    def GetVar(self, VarName):
        Returned = GetData()['Loaders'][self.Locate][VarName]
        return Returned

    def SetVar(self, Name, Value):
        Returned = GetData()
        Returned['Loaders'][self.Locate][Name] = Value
        with open("Scripts/GUILoader.json", 'w') as wJson:
            json.dump(Returned, wJson, indent=4)
