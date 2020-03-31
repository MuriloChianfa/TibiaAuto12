from Engine.GUI import *

EnabledAutoGrouping = False


class AutoGrouping:
    def __init__(self, root):
        self.AutoGrouping = GUI('AutoGrouping', 'Module: Auto Grouping')
        self.AutoGrouping.DefaultWindow('DefaultWindow')

        def SetAutoGrouping():
            global EnabledAutoGrouping
            if not EnabledAutoGrouping:
                EnabledAutoGrouping = True
                ButtonEnabled.configure(text='AutoGrouping: ON')
                ScanAutoGrouping()
            else:
                EnabledAutoGrouping = False
                ButtonEnabled.configure(text='AutoGrouping: OFF')

        def ScanAutoGrouping():
            if EnabledAutoGrouping:
                print("Try Lock AutoGrouping")
                print("Try This")

            root.after(300, ScanAutoGrouping)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoGrouping.addButton('Ok', self.AutoGrouping.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoGrouping
        if not EnabledAutoGrouping:
            ButtonEnabled = self.AutoGrouping.addButton('AutoGrouping: OFF', SetAutoGrouping, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoGrouping.addButton('AutoGrouping: ON', SetAutoGrouping, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoGrouping.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoGrouping.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoGrouping.loop()

