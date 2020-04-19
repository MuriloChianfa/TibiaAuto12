import time
import threading

from Engine.GUI import *
from Engine.ScanAmulet import ScanAmulet, SearchForAmulet

EnabledAutoSSA = False
Hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]
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
                ButtonEnabled.configure(text='AutoSSA: ON')
                try:
                    ThreadAutoRing = threading.Thread(target=ScanAutoAmulet)
                    ThreadAutoRing.start()
                except:
                    print("Error: Unable To Start ThreadAutoSSA!")
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoSSA: OFF')

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
                        print("Amulet Alocated On: X =", AmuletPositions[0] + 16, "Y =", AmuletPositions[1] + 16, "From: X =",
                              AmuletLocate[0], "Y =", AmuletLocate[1])
                        time.sleep(0.3)

            # if EnabledAutoRing:
            # root.after(300, ScanAutoAmulet)

        def Check():
            RadioNumber = RadioButton.get()
            print(RadioNumber)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        RadioButton = tk.IntVar()
        NameAmulet = tk.StringVar()
        NameAmulet.set('SSA')
        HotkeyAmulet = tk.StringVar()
        HotkeyAmulet.set("f6")

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

        self.AutoSSA.addLabel('Amulet', [130, 16, 6], [198, 45])
        OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [170, 75], width=10)

        self.AutoSSA.addRadio('Search', RadioButton, 0, [30, 45], [130, 16, 6], Check)
        self.AutoSSA.addRadio('Hotkey', RadioButton, 1, [30, 65], [130, 16, 6], Check)
        self.AutoSSA.addRadio('Position', RadioButton, 2, [30, 85], [130, 16, 6], Check)

        DescLabel = self.AutoSSA.addLabel('', [130, 16, 6], [130, 140])
        BackImage = 'images/Fundo.png'
        Back = self.AutoSSA.openImage(BackImage, [128, 128])

        NameImage = NameAmulet.get()
        NameImage2 = 'images/Amulets/' + NameImage + '.png'
        AmuletImage = self.AutoSSA.openImage(NameImage2, [128, 128])

        def Checking():
            if RadioButton.get() == 0:
                DescLabel.configure(text='Image To Search')
                self.AutoSSA.addImage(AmuletImage, [130, 16, 6], [110, 160])
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoSSA.addImage(Back, [130, 16, 6], [110, 160])
                self.AutoSSA.addOption(HotkeyAmulet, Hotkeys, [130, 180], 6)
            elif RadioButton.get() == 2:
                DescLabel.configure(text='Position To Search')
                self.AutoSSA.addImage(Back, [130, 16, 6], [110, 160])
                self.AutoSSA.addLabel('X:', [130, 16, 6], [120, 160])
                self.AutoSSA.addEntry([140, 160])
                self.AutoSSA.addLabel('Y:', [130, 16, 6], [120, 180])
                self.AutoSSA.addEntry([140, 180])

            root.after(300, Checking)

        Checking()

        self.AutoSSA.loop()

