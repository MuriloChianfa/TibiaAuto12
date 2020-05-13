import time

import keyboard
import threading
import pygetwindow

from Engine.GUI import *
from Engine.ScanRing import ScanRing, SearchForRing
from Conf.Hotkeys import Hotkey

FoundedImg = False
EnabledAutoRing = False
WaitingForClick = False
Rings = [
    'MightRing',
    'EnergyRing'
]
Ring = 'MightRing'
RingLocate = [0, 0]
percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
lifeColorFull = [194, 74, 74]
lifeColor = [219, 79, 79]
MaxLen = 4


class AutoRing:
    def __init__(self, root, RingPositions, HealthLocation, MOUSE_OPTION, HOOK_OPTION):
        self.AutoRing = GUI('AutoRing', 'Module: Auto Ring')
        self.AutoRing.DefaultWindow('AutoRing', [306, 397], [1.2, 2.29])
        self.SendToClient = Hotkey(MOUSE_OPTION)

        def SetAutoRing():
            global EnabledAutoRing
            if not EnabledAutoRing:
                EnabledAutoRing = True
                ButtonEnabled.configure(text='AutoRing: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoRing: ON")
                global Ring
                Ring = NameRing.get()
                Checking()
                CheckingButtons()
                time.sleep(0.03)
                ThreadAutoRing = threading.Thread(target=ScanAutoRing)
                ThreadAutoRing.start()
            else:
                EnabledAutoRing = False
                print('AutoRing: OFF')
                ButtonEnabled.configure(text='AutoRing: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                Checking()
                CheckingButtons()

        def ScanAutoRing():
            if CheckLifeBellowThan.get():
                BellowThan = LifeBellowThan.get()
                from Modules.AutoHeal import EnabledAutoHeal
                if EnabledAutoHeal:
                    while EnabledAutoRing and EnabledAutoHeal:
                        try:
                            NoHasRing = ScanRing(RingPositions, HOOK_OPTION)
                        except Exception:
                            NoHasRing = False
                            pass

                        from Modules.AutoHeal import life
                        if NoHasRing and life <= BellowThan:
                            Execute()
                else:
                    from Engine.ScanStages import ScanStages
                    while EnabledAutoRing:
                        try:
                            life = ScanStages('Life From AutoRing', HOOK_OPTION).ScanStages(HealthLocation, lifeColor, lifeColorFull)
                        except Exception:
                            life = 100
                            pass

                        if life is None:
                            life = 0
                        try:
                            NoHasRing = ScanRing(RingPositions, HOOK_OPTION)
                        except Exception:
                            NoHasRing = False
                            pass

                        if NoHasRing and life < BellowThan:
                            Execute()
            else:
                while EnabledAutoRing:
                    try:
                        NoHasRing = ScanRing(RingPositions, HOOK_OPTION)
                    except Exception:
                        NoHasRing = False
                        pass

                    if NoHasRing:
                        Execute()

        def Execute():
            if RadioButton.get() == 0:
                self.SendToClient.Press(HotkeyRing.get())
                print("Pressed ", HotkeyRing.get(), " To Reallocated Your Ring")
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
                        pyautogui.moveTo(RingPositions[0] + 16, RingPositions[1] + 16)
                        pyautogui.mouseUp(button='left')
                        pyautogui.moveTo(MousePosition)
                        print("Ring Reallocated On: X =", RingPositions[0] + 16, "Y =", RingPositions[1] + 16,
                              "From: X =",
                              X, "Y =", Y)
                        time.sleep(0.3)
                    else:
                        print("Lower Resolution Than Entered")
                        time.sleep(1)

        def Recapture():
            global WaitingForClick, Ring
            WaitingForClick = True
            Ring = NameRing.get()
            AutoRingWindow = pygetwindow.getWindowsWithTitle("Module: Auto Ring")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            RootWindowX = root.winfo_x()
            RootWindowY = root.winfo_y()
            AutoRingWindowX = self.AutoRing.PositionOfWindow('X')
            AutoRingWindowY = self.AutoRing.PositionOfWindow('Y')
            time.sleep(0.1)
            TibiaAuto.minimize()
            AutoRingWindow.minimize()
            Invisible = GUI('InvisibleWindow', 'InvisibleWindow')
            Invisible.InvisibleWindow('Recapture')
            while WaitingForClick:
                X, Y = GetPosition()
                if keyboard.is_pressed("c"):
                    sX, sY = GetPosition()
                    time.sleep(0.03)
                    pyautogui.screenshot('images/Rings/' + Ring + '.png',
                                         region=(sX - 5, sY - 5, 12, 12))
                    WaitingForClick = False
                    Invisible.destroyWindow()
                    TibiaAuto.maximize()
                    TibiaAuto.moveTo(RootWindowX, RootWindowY)
                    time.sleep(0.04)
                    AutoRingWindow.maximize()
                    AutoRingWindow.moveTo(AutoRingWindowX, AutoRingWindowY)
                    break
                Invisible.UpdateWindow(X, Y)

        def AddNewAmulet():
            print('....')

        def CheckClick():
            Checking()

        def ReturnGetPosition():
            global WaitingForClick
            WaitingForClick = True
            AutoRingWindow = pygetwindow.getWindowsWithTitle("Module: Auto Ring")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            RootWindowX = root.winfo_x()
            RootWindowY = root.winfo_y()
            AutoRingWindowX = self.AutoRing.PositionOfWindow('X')
            AutoRingWindowY = self.AutoRing.PositionOfWindow('Y')
            time.sleep(0.1)
            TibiaAuto.minimize()
            AutoRingWindow.minimize()
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
                    AutoRingWindow.maximize()
                    AutoRingWindow.moveTo(AutoRingWindowX, AutoRingWindowY)
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
        NameRing = tk.StringVar()
        NameRing.set('MightRing')
        HotkeyRing = tk.StringVar()
        HotkeyRing.set("Shift + F3")
        TextEntryX = tk.StringVar()
        TextEntryY = tk.StringVar()
        CheckLifeBellowThan = tk.BooleanVar()
        CheckLifeBellowThan.set(False)
        LifeBellowThan = tk.IntVar()
        LifeBellowThan.set(30)

        self.AutoRing.addButton('Ok', self.AutoRing.destroyWindow, [73, 21], [115, 365])

        global EnabledAutoRing
        if not EnabledAutoRing:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: OFF', SetAutoRing, [287, 23], [11, 336])
        else:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: ON', SetAutoRing, [287, 23], [11, 336])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoRing.addCheck(CheckPrint, [11, 285], 0, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoRing.addCheck(LowMana, [11, 305], 0, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        BackImage = 'images/Fundo.png'
        Back = self.AutoRing.openImage(BackImage, [150, 45])

        RingImg = 'images/Rings/MightRing.png'
        ImageID = self.AutoRing.openImage(RingImg, [64, 64])

        ImgLabel = self.AutoRing.addLabel('Image To Search', [16, 22])
        self.AutoRing.addImage(ImageID, [28, 43])

        RingLabel = self.AutoRing.addLabel('Select Name Of Ring', [135, 55])
        OptionNameRing = self.AutoRing.addOption(NameRing, Rings, [120, 80], width=21)

        ButtonAddNewRing = self.AutoRing.addButton('Add New Ring', AddNewAmulet, [167, 24], [120, 115])

        ButtonRecapture = self.AutoRing.addButton('Recapture', Recapture, [88, 24], [22, 115])

        DescLabel = self.AutoRing.addLabel('', [150, 140])

        RButton1 = self.AutoRing.addRadio('Hotkey', RadioButton, 0, [22, 155], CheckClick)
        RButton2 = self.AutoRing.addRadio('Position', RadioButton, 1, [22, 175], CheckClick)

        CheckBoxLifeBellowThan = self.AutoRing.addCheck(CheckLifeBellowThan, [60, 210], 0,
                                                        'Use Only If Life Is Bellow Than')
        LabelLifeBellowThan = self.AutoRing.addLabel('Life <= ', [90, 245])
        PercentageLifeBellowThan = self.AutoRing.addOption(LifeBellowThan, percentage, [140, 240])

        def Checking():
            global FoundedImg, Ring
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoRing.addImage(Back, [130, 165])
                FoundedImg = False
                HotkeyOption = self.AutoRing.addOption(HotkeyRing, self.SendToClient.Hotkeys, [145, 170], 10)
                if EnabledAutoRing:
                    HotkeyOption.configure(state='disabled')
                else:
                    HotkeyOption.configure(state='normal')
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Position To Search')
                self.AutoRing.addImage(Back, [120, 165])
                FoundedImg = False

                ButtonGetPosition = self.AutoRing.addButton('GetPosition', ReturnGetPosition, [80, 29], [195, 173])

                LabelX = self.AutoRing.addLabel('X:', [135, 165])
                EntryX = self.AutoRing.addEntry([150, 165], TextEntryX, width=4)
                TextEntryX.trace("w", ValidateEntryX)
                LabelY = self.AutoRing.addLabel('Y:', [135, 185])
                EntryY = self.AutoRing.addEntry([150, 185], TextEntryY, width=4)
                TextEntryY.trace("w", ValidateEntryY)
                if EnabledAutoRing:
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
            if EnabledAutoRing:
                CheckPrint.configure(state='disabled')
                CheckBuff.configure(state='disabled')

                DescLabel.configure(state='disabled')
                ImgLabel.configure(state='disabled')
                ButtonRecapture.configure(state='disabled')
                ButtonAddNewRing.configure(state='disabled')

                RButton1.configure(state='disabled')
                RButton2.configure(state='disabled')
                RingLabel.configure(state='disabled')
                OptionNameRing.configure(state='disabled')

                CheckBoxLifeBellowThan.configure(state='disabled')
                LabelLifeBellowThan.configure(state='disabled')
                PercentageLifeBellowThan.configure(state='disabled')
            else:
                CheckPrint.configure(state='normal')
                CheckBuff.configure(state='normal')

                DescLabel.configure(state='normal')
                ImgLabel.configure(state='normal')
                ButtonRecapture.configure(state='normal')
                ButtonAddNewRing.configure(state='normal')

                RButton1.configure(state='normal')
                RButton2.configure(state='normal')
                RingLabel.configure(state='normal')
                OptionNameRing.configure(state='normal')

                CheckBoxLifeBellowThan.configure(state='normal')

                if not CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='disabled')
                    PercentageLifeBellowThan.configure(state='disabled')
                elif CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='normal')
                    PercentageLifeBellowThan.configure(state='normal')

        def ConstantVerify():
            if not EnabledAutoRing:
                if not CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='disabled')
                    PercentageLifeBellowThan.configure(state='disabled')
                elif CheckLifeBellowThan.get():
                    LabelLifeBellowThan.configure(state='normal')
                    PercentageLifeBellowThan.configure(state='normal')

            self.AutoRing.After(1, ConstantVerify)

        Checking()
        CheckingButtons()

        ConstantVerify()

        self.AutoRing.loop()

