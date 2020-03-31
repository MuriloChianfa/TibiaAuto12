from Engine.GUI import *

EnabledPythonScripts = False


class PythonScripts:
    def __init__(self, root):
        self.PythonScripts = GUI('PythonScripts', 'Module: Python Scripts')
        self.PythonScripts.DefaultWindow('DefaultWindow')

        def SetPythonScripts():
            global EnabledPythonScripts
            if not EnabledPythonScripts:
                EnabledPythonScripts = True
                ButtonEnabled.configure(text='PythonScripts: ON')
                ScanPythonScripts()
            else:
                EnabledPythonScripts = False
                ButtonEnabled.configure(text='PythonScripts: OFF')

        def ScanPythonScripts():
            if EnabledPythonScripts:
                print("Try Lock PythonScripts")
                print("Try This")

            root.after(300, ScanPythonScripts)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.PythonScripts.addButton('Ok', self.PythonScripts.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledPythonScripts
        if not EnabledPythonScripts:
            ButtonEnabled = self.PythonScripts.addButton('PythonScripts: OFF', SetPythonScripts, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.PythonScripts.addButton('PythonScripts: ON', SetPythonScripts, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.PythonScripts.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.PythonScripts.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.PythonScripts.loop()

