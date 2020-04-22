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
percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
lifeColorFull = [194, 74, 74]
lifeColor = [219, 79, 79]
MaxLen = 4


class AutoSSA:
    def __init__(self, root, AmuletPositions, HealthLocation):
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
                time.sleep(0.03)
                ThreadAutoAmulet = threading.Thread(target=ScanAutoAmulet)
                ThreadAutoAmulet.start()
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoSSA: OFF')
                print("AutoSSA: OFF")
                Checking()
                CheckingButtons()

        def ScanAutoAmulet():
            if CheckLifeBellowThan.get():
                BellowThan = LifeBellowThan.get()
                from Modules.AutoHeal import EnabledAutoHeal
                if EnabledAutoHeal:
                    while EnabledAutoSSA and EnabledAutoHeal:
                        NoHasAmulet = ScanAmulet(AmuletPositions, Amulet)
                        from Modules.AutoHeal import life
                        print(life, BellowThan)
                        if NoHasAmulet and life <= BellowThan:
                            Execute()
                else:
                    from Engine.ScanStages import ScanStages
                    while EnabledAutoSSA:
                        life = ScanStages('Life From AutoAmulet').ScanStages(HealthLocation, lifeColor, lifeColorFull)

                        if life is None:
                            life = 0

                        NoHasAmulet = ScanAmulet(AmuletPositions, Amulet)

                        if NoHasAmulet and life < BellowThan:
                            Execute()
            elif not CheckLifeBellowThan.get():
                while EnabledAutoSSA:
                    NoHasAmulet = ScanAmulet(AmuletPositions, Amulet)
                    if NoHasAmulet:
                        Execute()

        def Execute():
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

        def Recapture():
            print("Not Initiated")

        def CheckClick():
            Checking()

        def ReturnGetPosition():
            global WaitingForClick
            WaitingForClick = True
            AutoSSAWindow = pygetwindow.getWindowsWithTitle("Module: Auto SSA")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            RootWindowX = root.winfo_x()
            RootWindowY = root.winfo_y()
            AutoSSAWindowX = self.AutoSSA.PositionOfWindow('X')
            AutoSSAWindowY = self.AutoSSA.PositionOfWindow('Y')
            time.sleep(0.1)
            TibiaAuto.minimize()
            AutoSSAWindow.minimize()
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
                    TibiaAuto.moveTo(RootWindowX, RootWindowY)
                    time.sleep(0.08)
                    AutoSSAWindow.maximize()
                    AutoSSAWindow.moveTo(AutoSSAWindowX, AutoSSAWindowY)
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
        CheckLifeBellowThan = tk.BooleanVar()
        CheckLifeBellowThan.set(False)
        LifeBellowThan = tk.IntVar()
        LifeBellowThan.set(30)

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

        BackImage = 'images/Fundo.png'
        Back = self.AutoSSA.openImage(BackImage, [150, 45])

        AmuletImg = 'images/Amulets/SSA.png'
        ImageID = self.AutoSSA.openImage(AmuletImg, [64, 64])

        ImgLabel = self.AutoSSA.addLabel('Image To Search', [130, 16, 6], [30, 45])
        self.AutoSSA.addImage(ImageID, [130, 16, 6], [42, 65])

        AmuletLabel = self.AutoSSA.addLabel('Amulet', [130, 16, 6], [190, 50])
        OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [150, 85], width=16)

        ButtonRecapture = self.AutoSSA.addButton('Recapture', Recapture, [88, 24, 33, 139],
                                                 [127, 17, 8], [123, 13, 5])

        DescLabel = self.AutoSSA.addLabel('', [130, 16, 6], [170, 220])

        RButton1 = self.AutoSSA.addRadio('Hotkey', RadioButton, 0, [30, 235], [130, 16, 6], CheckClick)
        RButton2 = self.AutoSSA.addRadio('Position', RadioButton, 1, [30, 255], [130, 16, 6], CheckClick)

        CheckBoxLifeBellowThan = self.AutoSSA.addCheck(CheckLifeBellowThan, [65, 290], [130, 16, 6], 0,
                                                       'Use Only If Life Is Bellow Than')
        LabelLifeBellowThan = self.AutoSSA.addLabel('Life <= ', [130, 16, 6], [95, 325])
        PercentageLifeBellowThan = self.AutoSSA.addOption(LifeBellowThan, percentage, [145, 320])

        def Checking():
            global FoundedImg, Amulet
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoSSA.addImage(Back, [130, 16, 6], [160, 240])
                FoundedImg = False
                HotkeyOption = self.AutoSSA.addOption(HotkeyAmulet, Hotkeys, [165, 250], 10)
                if EnabledAutoSSA:
                    HotkeyOption.configure(state='disabled')
                else:
                    HotkeyOption.configure(state='normal')
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Position To Search')
                self.AutoSSA.addImage(Back, [130, 16, 6], [150, 240])
                FoundedImg = False

                ButtonGetPosition = self.AutoSSA.addButton('GetPosition', ReturnGetPosition, [80, 29, 215, 255],
                                                           [127, 17, 8], [123, 13, 5])

                LabelX = self.AutoSSA.addLabel('X:', [130, 16, 6], [160, 250])
                EntryX = self.AutoSSA.addEntry([175, 250], TextEntryX, width=4)
                TextEntryX.trace("w", ValidateEntryX)
                LabelY = self.AutoSSA.addLabel('Y:', [130, 16, 6], [160, 270])
                EntryY = self.AutoSSA.addEntry([175, 270], TextEntryY, width=4)
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
            if not CheckLifeBellowThan.get():
                LabelLifeBellowThan.configure(state='disabled')
                PercentageLifeBellowThan.configure(state='disabled')
            elif CheckLifeBellowThan.get():
                LabelLifeBellowThan.configure(state='normal')
                PercentageLifeBellowThan.configure(state='normal')

        def CheckingButtons():
            if EnabledAutoSSA:
                DescLabel.configure(state='disabled')
                ImgLabel.configure(state='disabled')
                ButtonRecapture.configure(state='disabled')

                RButton1.configure(state='disabled')
                RButton2.configure(state='disabled')
                AmuletLabel.configure(state='disabled')
                OptionNameAmulet.configure(state='disabled')

                CheckBoxLifeBellowThan.configure(state='disabled')
                LabelLifeBellowThan.configure(state='disabled')
                PercentageLifeBellowThan.configure(state='disabled')
            else:
                DescLabel.configure(state='normal')
                ImgLabel.configure(state='normal')
                ButtonRecapture.configure(state='normal')

                RButton1.configure(state='normal')
                RButton2.configure(state='normal')
                AmuletLabel.configure(state='normal')
                OptionNameAmulet.configure(state='normal')

                CheckBoxLifeBellowThan.configure(state='normal')

                if not CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='disabled')
                    PercentageLifeBellowThan.configure(state='disabled')
                elif CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='normal')
                    PercentageLifeBellowThan.configure(state='normal')

        def ConstantVefify():
            if not EnabledAutoSSA:
                if not CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='disabled')
                    PercentageLifeBellowThan.configure(state='disabled')
                elif CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='normal')
                    PercentageLifeBellowThan.configure(state='normal')

            self.AutoSSA.After(1, ConstantVefify)

        Checking()
        CheckingButtons()

        ConstantVefify()

        self.AutoSSA.loop()
