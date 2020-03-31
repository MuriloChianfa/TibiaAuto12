from Engine.GUI import *

EnabledSortLoot = False


class SortLoot:
    def __init__(self, root):
        self.SortLoot = GUI('SortLoot', 'Module: Sort Loot')
        self.SortLoot.DefaultWindow('DefaultWindow')

        def SetSortLoot():
            global EnabledSortLoot
            if not EnabledSortLoot:
                EnabledSortLoot = True
                ButtonEnabled.configure(text='SortLoot: ON')
                ScanSortLoot()
            else:
                EnabledSortLoot = False
                ButtonEnabled.configure(text='SortLoot: OFF')

        def ScanSortLoot():
            if EnabledSortLoot:
                print("Try Lock SortLoot")
                print("Try This")

            root.after(300, ScanSortLoot)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.SortLoot.addButton('Ok', self.SortLoot.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledSortLoot
        if not EnabledSortLoot:
            ButtonEnabled = self.SortLoot.addButton('SortLoot: OFF', SetSortLoot, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.SortLoot.addButton('SortLoot: ON', SetSortLoot, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.SortLoot.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.SortLoot.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.SortLoot.loop()

