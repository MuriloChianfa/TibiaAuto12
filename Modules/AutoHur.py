from Engine.GUI import *

EnabledAutoHur = False


class AutoHur:
    def __init__(self, root):
        self.AutoHur = GUI('AutoHur', 'Module: Auto Hur')
        self.AutoHur.DefaultWindow('DefaultWindow')

        def SetAutoHur():
            global EnabledAutoHur
            if not EnabledAutoHur:
                EnabledAutoHur = True
                ButtonEnabled.configure(text='AutoHur: ON')
                ScanAutoHur()
            else:
                EnabledAutoHur = False
                ButtonEnabled.configure(text='AutoHur: OFF')

        def ScanAutoHur():
            if EnabledAutoHur:
                print("Try Lock AutoHur")
                print("Try This")

            root.after(300, ScanAutoHur)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoHur.addButton('Ok', self.AutoHur.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoHur
        if not EnabledAutoHur:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: OFF', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: ON', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoHur.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoHur.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoHur.loop()

