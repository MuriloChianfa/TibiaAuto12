from Engine.GUI import *

EnabledAutoFish = False


class AutoFish:
    def __init__(self, root):
        self.AutoFish = GUI('AutoFish', 'Module: Auto Fish')
        self.AutoFish.DefaultWindow('DefaultWindow')

        def SetAutoFish():
            global EnabledAutoFish
            if not EnabledAutoFish:
                EnabledAutoFish = True
                ButtonEnabled.configure(text='AutoFish: ON')
                ScanAutoFish()
            else:
                EnabledAutoFish = False
                ButtonEnabled.configure(text='AutoFish: OFF')

        def ScanAutoFish():
            if EnabledAutoFish:
                print("Try Lock AutoFish")
                print("Try This")

            root.after(300, ScanAutoFish)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoFish.addButton('Ok', self.AutoFish.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoFish
        if not EnabledAutoFish:
            ButtonEnabled = self.AutoFish.addButton('AutoFish: OFF', SetAutoFish, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoFish.addButton('AutoFish: ON', SetAutoFish, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoFish.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoFish.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoFish.loop()

