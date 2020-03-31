from Engine.GUI import *

EnabledAutoSeller = False


class AutoSeller:
    def __init__(self, root):
        self.AutoSeller = GUI('AutoSeller', 'Module: Auto Seller')
        self.AutoSeller.DefaultWindow('DefaultWindow')

        def SetAutoSeller():
            global EnabledAutoSeller
            if not EnabledAutoSeller:
                EnabledAutoSeller = True
                ButtonEnabled.configure(text='AutoSeller: ON')
                ScanAutoSeller()
            else:
                EnabledAutoSeller = False
                ButtonEnabled.configure(text='AutoSeller: OFF')

        def ScanAutoSeller():
            if EnabledAutoSeller:
                print("Try Lock AutoSeller")
                print("Try This")

            root.after(300, ScanAutoSeller)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoSeller.addButton('Ok', self.AutoSeller.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoSeller
        if not EnabledAutoSeller:
            ButtonEnabled = self.AutoSeller.addButton('AutoSeller: OFF', SetAutoSeller, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoSeller.addButton('AutoSeller: ON', SetAutoSeller, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoSeller.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoSeller.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoSeller.loop()

