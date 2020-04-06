import time
import threading

from Engine.GUI import *
from Engine.ScanRing import ScanRing, SearchForRing

EnabledAutoRing = False
Rings = [
    'MightRing',
    'EnergyRing'
]
RingLocate = [0, 0]


class AutoRing:
    def __init__(self, root, RingPositions):
        self.AutoRing = GUI('AutoRing', 'Module: Auto Ring')
        self.AutoRing.DefaultWindow('DefaultWindow')

        def SetAutoRing():
            global EnabledAutoRing
            if not EnabledAutoRing:
                EnabledAutoRing = True
                ButtonEnabled.configure(text='AutoRing: ON')
                try:
                    ThreadAutoRing = threading.Thread(target=ScanAutoRing)
                    ThreadAutoRing.start()
                except:
                    print("Error: Unable To Start ThreadAutoRing!")
            else:
                EnabledAutoRing = False
                ButtonEnabled.configure(text='AutoRing: OFF')

        def ScanAutoRing():
            while EnabledAutoRing:
                NoHasRing = ScanRing(RingPositions)
                if NoHasRing:
                    Ring = NameRing.get()
                    RingLocate[0], RingLocate[1] = SearchForRing(Ring)
                    if RingLocate[0] and RingLocate[1] != 0:
                        MousePosition = pyautogui.position()
                        pyautogui.moveTo(RingLocate[0], RingLocate[1])
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(RingPositions[0] + 16, RingPositions[1] + 16)
                        pyautogui.mouseUp(button='left')
                        pyautogui.moveTo(MousePosition)
                        print("Ring Alocated On: X =", RingPositions[0] + 16, "Y =", RingPositions[1] + 16, "From: X =",
                              RingLocate[0], "Y =", RingLocate[1])
                        time.sleep(0.3)

            # if EnabledAutoRing:
                # root.after(300, ScanAutoRing)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        NameRing = tk.StringVar()
        NameRing.set('MightRing')

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

        self.AutoRing.addLabel('Ring', [130, 16, 6], [160, 70])
        OptionNameRing = self.AutoRing.addOption(NameRing, Rings, [130, 100], width=10)

        self.AutoRing.loop()

