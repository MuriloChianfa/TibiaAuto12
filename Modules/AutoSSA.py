from Engine.GUI import *

EnabledAutoSSA = False


class AutoSSA:
    def __init__(self, root):
        self.AutoSSA = GUI('AutoSSA', 'Module: Auto SSA')
        self.AutoSSA.DefaultWindow('DefaultWindow')

        def SetAutoSSA():
            global EnabledAutoSSA
            if not EnabledAutoSSA:
                EnabledAutoSSA = True
                ButtonEnabled.configure(text='AutoSSA: ON')
                ScanAutoSSA()
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoSSA: OFF')

        def ScanAutoSSA():
            if EnabledAutoSSA:
                print("Try Lock SSA")
                print("Try This")

            root.after(300, ScanAutoSSA)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoSSA.addButton('Ok', self.AutoSSA.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoSSA
        if not EnabledAutoSSA:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: OFF', SetAutoSSA, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: ON', SetAutoSSA, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoSSA.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoSSA.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoSSA.loop()

