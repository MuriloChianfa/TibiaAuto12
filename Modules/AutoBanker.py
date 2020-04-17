import time

from Engine.GUI import *
from Engine.ScanCap import ScanCap

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
                CapLocate = pyautogui.locateOnScreen('images/PlayerStats/Cap.png')
                if CapLocate:
                    FirstNumberBox = CapLocate[0] + 21, CapLocate[1] + 7
                    EndFirstNumberBox = FirstNumberBox[0] + 7, FirstNumberBox[1] + 10

                    SecondNumberBox = CapLocate[0] + 15, CapLocate[1] + 7
                    EndSecondNumberBox = SecondNumberBox[0] + 7, SecondNumberBox[1] + 10

                    ThirdNumberBox = CapLocate[0] + 9, CapLocate[1] + 7
                    EndThirdNumberBox = ThirdNumberBox[0] + 7, ThirdNumberBox[1] + 10

                    FourNumberBox = CapLocate[0] + 3, CapLocate[1] + 7
                    EndFourNumberBox = FourNumberBox[0] + 7, FourNumberBox[1] + 10

                    FirstNumber = ScanCap(FirstNumberBox, EndFirstNumberBox)
                    SecondNumber = ScanCap(SecondNumberBox, EndSecondNumberBox)
                    ThirdNumber = ScanCap(ThirdNumberBox, EndThirdNumberBox)
                    FourNumber = ScanCap(FourNumberBox, EndFourNumberBox)

                    print(FourNumber, ThirdNumber, SecondNumber, FirstNumber)
                    time.sleep(1)

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

