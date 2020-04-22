import time
import keyboard
import threading
import pygetwindow

from Engine.GUI import *
from Engine.ScanAmulet import ScanAmulet, SearchForAmulet
from Conf.Hotkeys import Hotkeys, PressHotkey

FoundedImg = False
EnabledAutoSSA = False
WaitingForClick = False
Amulets = [
    'SSA',
    'PlatinumAmulet'
]
Amulet = 'SSA'
AmuletLocate = [0, 0]
MaxLen = 4


class AutoSSA:
    def __init__(self, root, AmuletPositions):
        self.AutoSSA = GUI('AutoSSA', 'Module: Auto SSA')
        self.AutoSSA.DefaultWindow('DefaultWindow')

        def SetAutoAmulet():
            global EnabledAutoSSA
            if not EnabledAutoSSA:
                EnabledAutoSSA = True
                ButtonEnabled.configure(text='AutoSSA: ON')
                print("AutoSSA: ON")
                global Amulet
                Amulet = NameAmulet.get()
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
                print("AutoSSA: OFF")
                Checking()
                CheckingButtons()

        def ScanAutoAmulet():
            while EnabledAutoSSA:
                NoHasAmulet = ScanAmulet(AmuletPositions, Amulet)
                if NoHasAmulet:
                    if RadioButton.get() == 0:
                        PressHotkey(HotkeyAmulet.get())
                        print("Pressed ", HotkeyAmulet.get(), " To Reallocated Your Amulet")
                        time.sleep(1)
                    elif RadioButton.get() == 1:
                        try:
                            X = int(TextEntryX.get())
                            Y = int(TextEntryY.get())
                        except:
                            X = None
                            Y = None
                            print("Error To Get Type Of Position")
                            time.sleep(1)
                        if X and Y is not None:
                            if X < WidthScreen and Y < HeightScreen:
                                MousePosition = pyautogui.position()
                                pyautogui.moveTo(X, Y)
                                pyautogui.mouseDown(button='left')
                                pyautogui.moveTo(AmuletPositions[0] + 16, AmuletPositions[1] + 16)
                                pyautogui.mouseUp(button='left')
                                pyautogui.moveTo(MousePosition)
                                print("Amulet Reallocated On: X =", AmuletPositions[0] + 16, "Y =", AmuletPositions[1] + 16,
                                      "From: X =",
                                      X, "Y =", Y)
                                time.sleep(0.3)
                            else:
                                print("Lower Resolution Than Entered")
                                time.sleep(1)
                    elif RadioButton.get() == 2:
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

        def ReturnGetPosition():
            global WaitingForClick
            WaitingForClick = True
            AutoSSAWindow = pygetwindow.getWindowsWithTitle("Module: Auto SSA")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            time.sleep(0.1)
            TibiaAuto.minimize()
            AutoSSAWindow.minimize()
            time.sleep(0.1)
            Invisible = GUI('InvisibleWindow', 'InvisibleWindow')
            Invisible.InvisibleWindow('GetPosition')
            while WaitingForClick:
                X, Y = GetPosition()
                if keyboard.is_pressed("c"):
                    X, Y = GetPosition()
                    WaitingForClick = False
                    print(f"Your Click Is Located In: [X: {X}, Y: {Y}]")
                    TextEntryX.set(X)
                    TextEntryY.set(Y)
                    Invisible.destroyWindow()
                    TibiaAuto.maximize()
                    time.sleep(0.08)
                    AutoSSAWindow.maximize()
                    break
                Invisible.UpdateWindow(X, Y)

        def ValidateEntryX(*args):
            s = TextEntryX.get()
            if len(s) > MaxLen:
                if not s[-1].isdigit():
                    TextEntryX.set(s[:-1])
                else:
                    TextEntryX.set(s[:MaxLen])

        def ValidateEntryY(*args):
            s = TextEntryY.get()
            if len(s) > MaxLen:
                if not s[-1].isdigit():
                    TextEntryY.set(s[:-1])
                else:
                    TextEntryY.set(s[:MaxLen])

        WidthScreen, HeightScreen = pyautogui.size()

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        RadioButton = tk.IntVar()
        NameAmulet = tk.StringVar()
        NameAmulet.set('SSA')
        HotkeyAmulet = tk.StringVar()
        HotkeyAmulet.set("Shift + F2")
        TextEntryX = tk.StringVar()
        TextEntryY = tk.StringVar()

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

        AmuletImg = 'images/Amulets/SSA.png'
        ImageID = self.AutoSSA.openImage(AmuletImg, [64, 64])

        ImgLabel = self.AutoSSA.addLabel('Image To Search', [130, 16, 6], [30, 45])
        self.AutoSSA.addImage(ImageID, [130, 16, 6], [40, 65])

        DescLabel = self.AutoSSA.addLabel('', [130, 16, 6], [170, 130])
        BackImage = 'images/Fundo.png'
        Back = self.AutoSSA.openImage(BackImage, [150, 128])

        def Checking():
            global FoundedImg, Amulet
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoSSA.addImage(Back, [130, 16, 6], [160, 150])
                FoundedImg = False
                HotkeyOption = self.AutoSSA.addOption(HotkeyAmulet, Hotkeys, [165, 160], 10)
                if EnabledAutoSSA:
                    HotkeyOption.configure(state='disabled')
                else:
                    HotkeyOption.configure(state='normal')
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Position To Search')
                self.AutoSSA.addImage(Back, [130, 16, 6], [150, 150])
                FoundedImg = False

                ButtonGetPosition = self.AutoSSA.addButton('GetPosition', ReturnGetPosition, [80, 29, 215, 165],
                                                           [127, 17, 8], [123, 13, 5])

                LabelX = self.AutoSSA.addLabel('X:', [130, 16, 6], [160, 160])
                EntryX = self.AutoSSA.addEntry([175, 160], TextEntryX, width=4)
                TextEntryX.trace("w", ValidateEntryX)
                LabelY = self.AutoSSA.addLabel('Y:', [130, 16, 6], [160, 180])
                EntryY = self.AutoSSA.addEntry([175, 180], TextEntryY, width=4)
                TextEntryY.trace("w", ValidateEntryY)
                if EnabledAutoSSA:
                    ButtonGetPosition.configure(state='disabled')

                    LabelX.configure(state='disabled')
                    EntryX.configure(state='disabled')
                    LabelY.configure(state='disabled')
                    EntryY.configure(state='disabled')
                else:
                    ButtonGetPosition.configure(state='normal')

                    LabelX.configure(state='normal')
                    EntryX.configure(state='normal')
                    LabelY.configure(state='normal')
                    EntryY.configure(state='normal')

        def CheckingButtons():
            RButton1 = self.AutoSSA.addRadio('Hotkey', RadioButton, 0, [30, 145], [130, 16, 6], CheckClick)
            RButton2 = self.AutoSSA.addRadio('Position', RadioButton, 1, [30, 165], [130, 16, 6], CheckClick)
            AmuletLabel = self.AutoSSA.addLabel('Amulet', [130, 16, 6], [198, 45])
            OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [150, 85], width=16)
            if EnabledAutoSSA:
                DescLabel.configure(state='disabled')
                ImgLabel.configure(state='disabled')

                RButton1.configure(state='disabled')
                RButton2.configure(state='disabled')
                AmuletLabel.configure(state='disabled')
                OptionNameAmulet.configure(state='disabled')
            else:
                DescLabel.configure(state='normal')
                ImgLabel.configure(state='normal')

                RButton1.configure(state='normal')
                RButton2.configure(state='normal')
                AmuletLabel.configure(state='normal')
                OptionNameAmulet.configure(state='normal')

        Checking()
        CheckingButtons()

        self.AutoSSA.loop()
