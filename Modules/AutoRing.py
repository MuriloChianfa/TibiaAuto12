from Engine.GUI import *

EnabledAutoRing = False


class AutoRing:
    def __init__(self, root):
        self.AutoRing = GUI('AutoRing', 'Module: Auto Ring')
        self.AutoRing.DefaultWindow('DefaultWindow')

        def SetAutoRing():
            global EnabledAutoRing
            if not EnabledAutoRing:
                EnabledAutoRing = True
                ButtonEnabled.configure(text='AutoRing: ON')
                ScanAutoRing()
            else:
                EnabledAutoRing = False
                ButtonEnabled.configure(text='AutoRing: OFF')

        def ScanAutoRing():
            if EnabledAutoRing:
                print("Try Lock AutoRing")
                print("Try This")

            root.after(300, ScanAutoRing)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoRing.addButton('Ok', self.AutoRing.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoRing
        if not EnabledAutoRing:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: OFF', SetAutoRing, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: ON', SetAutoRing, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoRing.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoRing.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoRing.loop()

