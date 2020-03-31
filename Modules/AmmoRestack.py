from Engine.GUI import *

EnabledAmmoRestack = False


class AmmoRestack:
    def __init__(self, root):
        self.AmmoRestack = GUI('AmmoRestack', 'Module: Ammo Restack')
        self.AmmoRestack.DefaultWindow('DefaultWindow')

        def SetAmmoRestack():
            global EnabledAmmoRestack
            if not EnabledAmmoRestack:
                EnabledAmmoRestack = True
                ButtonEnabled.configure(text='AmmoRestack: ON')
                ScanAmmoRestack()
            else:
                EnabledAmmoRestack = False
                ButtonEnabled.configure(text='AmmoRestack: OFF')

        def ScanAmmoRestack():
            if EnabledAmmoRestack:
                print("Try Lock AmmoRestack")
                print("Try This")

            root.after(300, ScanAmmoRestack)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AmmoRestack.addButton('Ok', self.AmmoRestack.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAmmoRestack
        if not EnabledAmmoRestack:
            ButtonEnabled = self.AmmoRestack.addButton('AmmoRestack: OFF', SetAmmoRestack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AmmoRestack.addButton('AmmoRestack: ON', SetAmmoRestack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AmmoRestack.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AmmoRestack.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AmmoRestack.loop()

