import time
import keyboard
import pygetwindow

from conf.Hotkeys import Hotkey
from conf.Constants import LifeColor, LifeColorFull, Percentage, Rings

from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter
from core.ThreadManager import ThreadManager

from engine.ScanRing import ScanRing

GUIChanges = []

FoundedImg = False
EnabledAutoRing = False
WaitingForClick = False
ThreadStarted = False

Ring = 'MightRing'
RingLocate = [0, 0]
MaxLen = 4
RingsPath = None


class AutoRing:
    def __init__(self, root, RingPositions, HealthLocation, MOUSE_OPTION, ItemsPath):
        self.AutoRing = GUI('AutoRing', 'Module: Auto Ring')
        self.AutoRing.DefaultWindow('AutoRing', [306, 397], [1.2, 2.29])
        self.Setter = GUISetter("RingLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadAutoRing")

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
                if not ThreadStarted:
                    self.ThreadManager.NewThread(ScanAutoRing)
                else:
                    self.ThreadManager.UnPauseThread()
            else:
                EnabledAutoRing = False
                print('AutoRing: OFF')
                ButtonEnabled.configure(text='AutoRing: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                Checking()
                CheckingButtons()
                self.ThreadManager.PauseThread()

        def ScanAutoRing():
            global Ring
            Ring = NameRing.get()
            if CheckLifeBellowThan.get():
                BellowThan = LifeBellowThan.get()
                from Modules.AutoHeal import EnabledAutoHeal
                if EnabledAutoHeal:
                    while EnabledAutoRing and EnabledAutoHeal:
                        NoHasRing = ScanRing(RingPositions)

                        from Modules.AutoHeal import Life
                        if NoHasRing and Life <= BellowThan:
                            Execute()
                else:
                    from Engine.ScanStages import ScanStages
                    while EnabledAutoRing:
                        Life = ScanStages('Life From AutoRing').ScanStages(HealthLocation, LifeColor, LifeColorFull)

                        if Life is None:
                            Life = 0

                        NoHasRing = ScanRing(RingPositions)

                        if NoHasRing and Life < BellowThan:
                            Execute()
            else:
                while EnabledAutoRing:
                    NoHasRing = ScanRing(RingPositions)

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
                except Exception:
                    X = None
                    Y = None
                    print("Error To Get Type Of Position")
                    time.sleep(1)
                if X and Y is not None:
                    if X < WidthScreen and Y < HeightScreen:

                        if MOUSE_OPTION == 1:
                            MousePosition = self.SendToClient.Position()
                        else:
                            MousePosition = [0, 0]

                        self.SendToClient.DragTo([X, Y], [RingPositions[0] + 16, RingPositions[1] + 16])

                        if MOUSE_OPTION == 1:
                            self.SendToClient.MoveTo(MousePosition[0], MousePosition[1])

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
                    from Core.HookWindow import SaveImage
                    SaveImage(ItemsPath + 'Rings/' + Ring + '.png', Region=(sX - 6, sY - 28, sX + 6, sY - 16))
                    WaitingForClick = False
                    Invisible.destroyWindow()
                    TibiaAuto.maximize()
                    time.sleep(0.04)
                    AutoRingWindow.maximize()
                    AutoRingWindow.moveTo(AutoRingWindowX, AutoRingWindowY)

                    UpdateImg()
                    break
                Invisible.UpdateWindow(X, Y)

        def AddNewAmulet():
            print('Option In Development...')

        def CheckClick():
            Checking()

        def ReturnGetPosition():
            global WaitingForClick
            WaitingForClick = True
            AutoRingWindow = pygetwindow.getWindowsWithTitle("Module: Auto Ring")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
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

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool('CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool('CheckBuff')

        RadioButton, InitiatedRadioButton = self.Setter.Variables.Int('RadioButton')

        NameRing, InitiatedNameRing = self.Setter.Variables.Str('NameRing')
        HotkeyRing, InitiatedHotkeyRing = self.Setter.Variables.Str('HotkeyRing')

        TextEntryX, InitiatedTextEntryX = self.Setter.Variables.Str('TextEntryX')
        TextEntryY, InitiatedTextEntryY = self.Setter.Variables.Str('TextEntryY')

        CheckLifeBellowThan, InitiatedLifeBellowThan = self.Setter.Variables.Bool('LifeBellowThan')
        LifeBellowThan, InitiatedBellowThan = self.Setter.Variables.Int('BellowThan')

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint, VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff, VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedRadioButton, RadioButton.get(), 'RadioButton')
            CheckingGUI(InitiatedNameRing, NameRing.get(), 'NameRing')
            CheckingGUI(InitiatedHotkeyRing, HotkeyRing.get(), 'HotkeyRing')
            CheckingGUI(InitiatedTextEntryX, TextEntryX.get(), 'TextEntryX')
            CheckingGUI(InitiatedTextEntryY, TextEntryY.get(), 'TextEntryY')
            CheckingGUI(InitiatedLifeBellowThan, CheckLifeBellowThan.get(), 'LifeBellowThan')
            CheckingGUI(InitiatedBellowThan, LifeBellowThan.get(), 'BellowThan')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoRing.destroyWindow()

        self.AutoRing.addButton('Ok', Destroy, [73, 21], [115, 365])

        global EnabledAutoRing
        if not EnabledAutoRing:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: OFF', SetAutoRing, [287, 23], [11, 336])
        else:
            ButtonEnabled = self.AutoRing.addButton('AutoRing: ON', SetAutoRing, [287, 23], [11, 336])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoRing.addCheck(VarCheckPrint, [11, 285], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoRing.addCheck(VarCheckBuff, [11, 305], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        BackImage = 'images/Fundo.png'
        Back = self.AutoRing.openImage(BackImage, [150, 45])

        RingImages = []
        RingName = []
        for NameOfCurrentRing in Rings:
            CurrentRingName = ItemsPath + 'Rings/' + NameOfCurrentRing + '.png'
            CurrentRingImage = self.AutoRing.openImage(CurrentRingName, [64, 64])

            RingImages.append(CurrentRingImage)
            RingName.append(NameOfCurrentRing)

        ImgLabel = self.AutoRing.addLabel('Image To Search', [16, 22])

        def UpdateImg():
            for XRing in Rings:
                if NameRing.get() == XRing:
                    self.AutoRing.addImage(RingImages[RingName.index(XRing)], [28, 43])

            global Ring
            Ring = NameRing.get()

        UpdateImg()

        WidthScreen, HeightScreen = self.SendToClient.MainWindowSize()

        RingLabel = self.AutoRing.addLabel('Select Name Of Ring', [135, 55])
        OptionNameRing = self.AutoRing.addOption(NameRing, Rings, [120, 80], width=21)

        ButtonAddNewRing = self.AutoRing.addButton('Add New Ring', AddNewAmulet, [167, 24], [120, 115])

        ButtonRecapture = self.AutoRing.addButton('Recapture', Recapture, [88, 24], [22, 115])

        DescLabel = self.AutoRing.addLabel('', [150, 140])

        RButton1 = self.AutoRing.addRadio('Hotkey', RadioButton, 0, [22, 155], CheckClick)
        RButton2 = self.AutoRing.addRadio('Position', RadioButton, 1, [22, 175], CheckClick)

        CheckBoxLifeBellowThan = self.AutoRing.addCheck(CheckLifeBellowThan, [60, 210], InitiatedLifeBellowThan,
                                                        'Use Only If Life Is Bellow Than')
        LabelLifeBellowThan = self.AutoRing.addLabel('Life <= ', [90, 245])
        PercentageLifeBellowThan = self.AutoRing.addOption(LifeBellowThan, Percentage, [140, 240])

        def Checking():
            global FoundedImg, Ring
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoRing.addImage(Back, [130, 165])
                FoundedImg = False
                HotkeyOption = self.AutoRing.addOption(HotkeyRing, self.SendToClient.Hotkeys, [145, 170], 10)
                if EnabledAutoRing:
                    Disable(HotkeyOption)
                else:
                    Enable(HotkeyOption)
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
                    Disable(ButtonGetPosition)

                    Disable(LabelX)
                    Disable(EntryX)
                    Disable(LabelY)
                    Disable(EntryY)
                else:
                    Enable(ButtonGetPosition)

                    Enable(LabelX)
                    Enable(EntryX)
                    Enable(LabelY)
                    Enable(EntryY)
            if not CheckLifeBellowThan.get():
                Disable(LabelLifeBellowThan)
                Disable(PercentageLifeBellowThan)
            elif CheckLifeBellowThan.get():
                Enable(LabelLifeBellowThan)
                Enable(PercentageLifeBellowThan)
            ExecGUITrigger()

        def CheckingButtons():
            if EnabledAutoRing:
                Disable(CheckPrint)
                Disable(CheckBuff)

                Disable(DescLabel)
                Disable(ImgLabel)
                Disable(ButtonRecapture)
                Disable(ButtonAddNewRing)

                Disable(RButton1)
                Disable(RButton2)
                Disable(RingLabel)
                Disable(OptionNameRing)

                Disable(CheckBoxLifeBellowThan)
                Disable(LabelLifeBellowThan)
                Disable(PercentageLifeBellowThan)
            else:
                Enable(CheckPrint)
                Enable(CheckBuff)

                Enable(DescLabel)
                Enable(ImgLabel)
                Enable(ButtonRecapture)
                Enable(ButtonAddNewRing)

                Enable(RButton1)
                Enable(RButton2)
                Enable(RingLabel)
                Enable(OptionNameRing)

                Enable(CheckBoxLifeBellowThan)

                if not CheckLifeBellowThan.get():
                    Disable(LabelLifeBellowThan)
                    Disable(PercentageLifeBellowThan)
                elif CheckLifeBellowThan.get():
                    Enable(LabelLifeBellowThan)
                    Enable(PercentageLifeBellowThan)
            ExecGUITrigger()

        def ConstantVerify():
            if not EnabledAutoRing:
                if not CheckLifeBellowThan.get():
                    Disable(LabelLifeBellowThan)
                    Disable(PercentageLifeBellowThan)
                elif CheckLifeBellowThan.get():
                    Enable(LabelLifeBellowThan)
                    Enable(PercentageLifeBellowThan)

                if NameRing.get() != Ring:
                    UpdateImg()

                ExecGUITrigger()

            self.AutoRing.After(200, ConstantVerify)

        Checking()
        CheckingButtons()

        ConstantVerify()

        self.AutoRing.Protocol(Destroy)
        self.AutoRing.loop()
