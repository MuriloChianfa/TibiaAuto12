import json
import tkinter as tk


def GetData():
    with open("Scripts/GUILoader.json", 'r') as LoadsJson:
        data = json.load(LoadsJson)

    return data


class GUISetter:
    def __init__(self, Locate):
        self.Locate = Locate
        self.Variables = Variables(Locate)
        self.SetVariables = SetVariables(Locate)


class Variables:
    def __init__(self, Locate):
        self.Locate = Locate

    # For Usage This:
    # Variable, Initiated = self.Setter.Variables.Bool('')
    def Bool(self, VarName):
        Variable = tk.BooleanVar()
        InitiatedVariable = SetVariables(self.Locate).GetBoolVar(VarName)
        Variable.set(InitiatedVariable)

        return Variable, InitiatedVariable

    # For Usage This:
    # Variable, Initiated = self.Setter.Variables.Str('')
    def Str(self, VarName):
        Variable = tk.StringVar()
        InitiatedVariable = SetVariables(self.Locate).GetVar(VarName)
        Variable.set(InitiatedVariable)

        return Variable, InitiatedVariable

    # For Usage This:
    # Variable, Initiated = self.Setter.Variables.Int('')
    def Int(self, VarName):
        Variable = tk.IntVar()
        InitiatedVariable = SetVariables(self.Locate).GetVar(VarName)
        Variable.set(InitiatedVariable)

        return Variable, InitiatedVariable


class SetVariables:
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

    # self.Setter.SetVariables.SetVar
    def SetVar(self, Name, Value):
        Returned = GetData()
        Returned['Loaders'][self.Locate][Name] = Value
        with open("Scripts/GUILoader.json", 'w') as wJson:
            json.dump(Returned, wJson, indent=4)
