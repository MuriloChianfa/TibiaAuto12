import time
import threading

from Engine.GUI import *
from Engine.ScanAmulet import ScanAmulet, SearchForAmulet

FoundedImg = False
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
                Checking()
                CheckingButtons()
                try:
                    ThreadAutoRing = threading.Thread(target=ScanAutoAmulet)
                    ThreadAutoRing.start()
                except:
                    print("Error: Unable To Start ThreadAutoSSA!")
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoSSA: OFF')
                Checking()
                CheckingButtons()

        def ScanAutoAmulet():
            while EnabledAutoSSA:
                NoHasAmulet = ScanAmulet(AmuletPositions)
                if NoHasAmulet:
                    if RadioButton.get() == 0:
                        pyautogui.press(HotkeyAmulet.get())
                        print("Pressed ", HotkeyAmulet.get(), " To Reallocated Your Amulet")
                        time.sleep(1)
                    elif RadioButton.get() == 1:
                        print("Not Concluded")
                        time.sleep(2)
                    elif RadioButton.get() == 2:
                        Amulet = NameAmulet.get()
                        AmuletLocate[0], AmuletLocate[1] = SearchForAmulet(Amulet)
                        if AmuletLocate[0] and AmuletLocate[1] != 0:
                            MousePosition = pyautogui.position()
                            pyautogui.moveTo(AmuletLocate[0], AmuletLocate[1])
                            pyautogui.mouseDown(button='left')
                            pyautogui.moveTo(AmuletPositions[0] + 16, AmuletPositions[1] + 16)
                            pyautogui.mouseUp(button='left')
                            pyautogui.moveTo(MousePosition)
                            print("Amulet Reallocated On: X =", AmuletPositions[0] + 16, "Y =", AmuletPositions[1] + 16,
                                  "From: X =",
                                  AmuletLocate[0], "Y =", AmuletLocate[1])
                            time.sleep(0.3)

            # if EnabledAutoRing:
            # root.after(300, ScanAutoAmulet)

        def CheckClick():
            Checking()

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

        DescLabel = self.AutoSSA.addLabel('', [130, 16, 6], [130, 140])
        BackImage = 'images/Fundo.png'
        Back = self.AutoSSA.openImage(BackImage, [128, 128])

        # def CheckImage():
        # NameImage = NameAmulet.get()
        # NameImage2 = 'images/Amulets/' + NameImage + '.png'
        # AmuletImage = self.AutoSSA.openImage(NameImage2, [128, 128])
        # return AmuletImage

        def CheckImg(NameImage):
            print(NameImage)
            NameImage2 = 'images/Amulets/' + NameImage + '.png'
            AmuletImage = self.AutoSSA.openImage(NameImage2, [128, 128])
            global FoundedImg
            FoundedImg = True
            return self.AutoSSA.addImage(AmuletImage, [130, 16, 6], [110, 160])

        def Checking():
            global FoundedImg
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoSSA.addImage(Back, [130, 16, 6], [110, 160])
                FoundedImg = False
                HotkeyOption = self.AutoSSA.addOption(HotkeyAmulet, Hotkeys, [130, 180], 6)
                if EnabledAutoSSA:
                    HotkeyOption.configure(state='disabled')
                else:
                    HotkeyOption.configure(state='normal')
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Position To Search')
                self.AutoSSA.addImage(Back, [130, 16, 6], [110, 160])
                FoundedImg = False
                LabelX = self.AutoSSA.addLabel('X:', [130, 16, 6], [145, 160])
                EntryX = self.AutoSSA.addEntry([160, 160], 6)
                LabelY = self.AutoSSA.addLabel('Y:', [130, 16, 6], [145, 180])
                EntryY = self.AutoSSA.addEntry([160, 180], 6)
                if EnabledAutoSSA:
                    LabelX.configure(state='disabled')
                    EntryX.configure(state='disabled')
                    LabelY.configure(state='disabled')
                    EntryY.configure(state='disabled')
                else:
                    LabelX.configure(state='normal')
                    EntryX.configure(state='normal')
                    LabelY.configure(state='normal')
                    EntryY.configure(state='normal')
            elif RadioButton.get() == 2:
                DescLabel.configure(text='Image To Search')
                if not FoundedImg:
                    NameImage = NameAmulet.get()
                    CheckImg(NameImage)

        def CheckingButtons():
            RButton1 = self.AutoSSA.addRadio('Hotkey', RadioButton, 0, [30, 45], [130, 16, 6], CheckClick)
            RButton2 = self.AutoSSA.addRadio('Position', RadioButton, 1, [30, 65], [130, 16, 6], CheckClick)
            RButton3 = self.AutoSSA.addRadio('Search', RadioButton, 2, [30, 85], [130, 16, 6], CheckClick)
            AmuletLabel = self.AutoSSA.addLabel('Amulet', [130, 16, 6], [198, 45])
            OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [170, 75], width=10)
            if EnabledAutoSSA:
                DescLabel.configure(state='disabled')

                RButton1.configure(state='disabled')
                RButton2.configure(state='disabled')
                RButton3.configure(state='disabled')
                AmuletLabel.configure(state='disabled')
                OptionNameAmulet.configure(state='disabled')
            else:
                DescLabel.configure(state='normal')

                RButton1.configure(state='normal')
                RButton2.configure(state='normal')
                RButton3.configure(state='normal')
                AmuletLabel.configure(state='normal')
                OptionNameAmulet.configure(state='normal')

        Checking()
        CheckingButtons()

        self.AutoSSA.loop()
