import tkinter as tk
from conf.conf_manager import ConfManager


def GetData():
    return ConfManager.get('GUILoader.json')


def check_gui(gui_changes, init, get, name):
    if get != init:
        gui_changes.append((name, get))


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

    # For Usage This:
    # Variable, Initiated = self.Setter.Variables.Int('')
    def array(self, name):
        initiated_array = SetVariables(self.Locate).GetVar(name)
        array = initiated_array

        return array, initiated_array


class SetVariables:
    def __init__(self, Locate):
        self.Locate = Locate

    def GetBoolVar(self, VarName):
        if GetData()['Loaders'][self.Locate][VarName]:
            return True
        return False

    def GetVar(self, VarName):
        return GetData()['Loaders'][self.Locate][VarName]

    # self.Setter.SetVariables.SetVar
    def SetVar(self, Name, Value):
        Returned = GetData()
        Returned['Loaders'][self.Locate][Name] = Value

        ConfManager.set(Returned, 'GUILoader.json')
