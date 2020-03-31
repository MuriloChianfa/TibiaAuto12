from Engine.GUI import *

EnabledAutoBanker = False


class AutoBanker:
    def __init__(self, root):
        self.AutoBanker = GUI('AutoBanker', 'Module: Auto Banker')
        self.AutoBanker.DefaultWindow('DefaultWindow')

        def SetAutoBanker():
            global EnabledAutoBanker
            if not EnabledAutoBanker:
                EnabledAutoBanker = True
                ButtonEnabled.configure(text='AutoBanker: ON')
                ScanAutoBanker()
            else:
                EnabledAutoBanker = False
                ButtonEnabled.configure(text='AutoBanker: OFF')

        def ScanAutoBanker():
            if EnabledAutoBanker:
                print("Try Lock AutoBanker")
                print("Try This")

            root.after(300, ScanAutoBanker)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoBanker.addButton('Ok', self.AutoBanker.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoBanker
        if not EnabledAutoBanker:
            ButtonEnabled = self.AutoBanker.addButton('AutoBanker: OFF', SetAutoBanker, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoBanker.addButton('AutoBanker: ON', SetAutoBanker, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoBanker.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoBanker.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoBanker.loop()

