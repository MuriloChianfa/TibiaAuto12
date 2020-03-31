from Engine.GUI import *

EnabledColorChange = False


class ColorChange:
    def __init__(self, root, Player):
        self.ColorChange = GUI('ColorChange', 'Module: Color Change')
        self.ColorChange.DefaultWindow('DefaultWindow')

        def SetColorChange():
            global EnabledColorChange
            if not EnabledColorChange:
                EnabledColorChange = True
                ButtonEnabled.configure(text='ColorChange: ON')
                ScanColorChange()
            else:
                EnabledColorChange = False
                ButtonEnabled.configure(text='ColorChange: OFF')

        def ScanColorChange():
            if EnabledColorChange:
                print("Try Lock ColorChange")
                print("Try This")

            root.after(300, ScanColorChange)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.ColorChange.addButton('Ok', self.ColorChange.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledColorChange
        if not EnabledColorChange:
            ButtonEnabled = self.ColorChange.addButton('ColorChange: OFF', SetColorChange, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.ColorChange.addButton('ColorChange: ON', SetColorChange, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.ColorChange.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.ColorChange.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.ColorChange.loop()

