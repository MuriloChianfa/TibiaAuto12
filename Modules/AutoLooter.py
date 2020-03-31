from Engine.GUI import *

EnabledAutoLooter = False


class AutoLooter:
    def __init__(self, root, Player, SQMs):
        self.AutoLooter = GUI('AutoLooter', 'Module: Auto Looter')
        self.AutoLooter.DefaultWindow('DefaultWindow')

        def SetAutoLooter():
            global EnabledAutoLooter
            if not EnabledAutoLooter:
                EnabledAutoLooter = True
                ButtonEnabled.configure(text='AutoLooter: ON')
                ScanAutoLooter()
            else:
                EnabledAutoLooter = False
                ButtonEnabled.configure(text='AutoLooter: OFF')

        def ScanAutoLooter():
            if EnabledAutoLooter:
                print("Try Lock AutoLooter")
                print("Try This")

            root.after(300, ScanAutoLooter)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoLooter.addButton('Ok', self.AutoLooter.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoLooter
        if not EnabledAutoLooter:
            ButtonEnabled = self.AutoLooter.addButton('AutoLooter: OFF', SetAutoLooter, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoLooter.addButton('AutoLooter: ON', SetAutoLooter, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoLooter.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoLooter.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoLooter.loop()

