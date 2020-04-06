import time
import threading

from Engine.GUI import *
from Engine.ScanAmulet import ScanAmulet, SearchForAmulet

EnabledAutoSSA = False
Amulets = [
    'SSA',
    'PlatinumAmulet'
]
AmuletLocate = [0, 0]


class AutoSSA:
    def __init__(self, root, AmuletPositions):
        self.AutoSSA = GUI('AutoSSA', 'Module: Auto SSA')
        self.AutoSSA.DefaultWindow('DefaultWindow')

        def SetAutoAmulet():
            global EnabledAutoSSA
            if not EnabledAutoSSA:
                EnabledAutoSSA = True
                ButtonEnabled.configure(text='AutoRing: ON')
                try:
                    ThreadAutoRing = threading.Thread(target=ScanAutoAmulet)
                    ThreadAutoRing.start()
                except:
                    print("Error: Unable To Start ThreadAutoSSA!")
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoRing: OFF')

        def ScanAutoAmulet():
            while EnabledAutoSSA:
                NoHasAmulet = ScanAmulet(AmuletPositions)
                if NoHasAmulet:
                    Amulet = NameAmulet.get()
                    AmuletLocate[0], AmuletLocate[1] = SearchForAmulet(Amulet)
                    if AmuletLocate[0] and AmuletLocate[1] != 0:
                        MousePosition = pyautogui.position()
                        pyautogui.moveTo(AmuletLocate[0], AmuletLocate[1])
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(AmuletPositions[0] + 16, AmuletPositions[1] + 16)
                        pyautogui.mouseUp(button='left')
                        pyautogui.moveTo(MousePosition)
                        print("Ring Alocated On: X =", AmuletPositions[0] + 16, "Y =", AmuletPositions[1] + 16, "From: X =",
                              AmuletLocate[0], "Y =", AmuletLocate[1])
                        time.sleep(0.3)

            # if EnabledAutoRing:
            # root.after(300, ScanAutoRing)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        NameAmulet = tk.StringVar()
        NameAmulet.set('SSA')

        self.AutoSSA.addButton('Ok', self.AutoSSA.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoSSA
        if not EnabledAutoSSA:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: OFF', SetAutoAmulet, [328, 29, 12, 469],
                                                    [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: ON', SetAutoAmulet, [328, 29, 12, 469],
                                                    [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoSSA.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoSSA.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoSSA.addLabel('Amulet', [130, 16, 6], [160, 70])
        OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [130, 100], width=10)

        self.AutoSSA.loop()

