from Engine.GUI import *

EnabledModules = False


class Modules:
    def __init__(self, root):
        self.Modules = GUI('Modules', 'Module: Modules')
        self.Modules.DefaultWindow('DefaultWindow')

        def SetModules():
            global EnabledModules
            if not EnabledModules:
                EnabledModules = True
                ButtonEnabled.configure(text='Modules: ON')
                ScanModules()
            else:
                EnabledModules = False
                ButtonEnabled.configure(text='Modules: OFF')

        def ScanModules():
            if EnabledModules:
                print("Try Lock Modules")
                print("Try This")

            root.after(300, ScanModules)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.Modules.addButton('Ok', self.Modules.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledModules
        if not EnabledModules:
            ButtonEnabled = self.Modules.addButton('Modules: OFF', SetModules, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.Modules.addButton('Modules: ON', SetModules, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.Modules.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.Modules.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.Modules.loop()

