import time
import keyboard
import pygetwindow

from Conf.Hotkeys import Hotkey
from Conf.Constants import LifeColor, LifeColorFull, Percentage, Amulets

from Core.GUI import *
from Core.GUIManager import *
from Core.GUISetter import GUISetter
from Core.ThreadManager import ThreadManager

from Engine.ScanAmulet import ScanAmulet

GUIChanges = []

ThreadStarted = False

FoundedImg = False
EnabledAutoSSA = False
WaitingForClick = False

Amulet = 'StoneSkinAmulet'
AmuletLocate = [0, 0]
MaxLen = 4


class AutoSSA:
    def __init__(self, root, AmuletPositions, HealthLocation, MOUSE_OPTION, ItemsPath):
        self.AutoSSA = GUI('AutoSSA', 'Module: Auto SSA')
        self.AutoSSA.DefaultWindow('AutoAmulet', [306, 397], [1.2, 2.29])
        self.Setter = GUISetter("AmuletLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadAutoAmulet")

        def SetAutoAmulet():
            global EnabledAutoSSA
            if not EnabledAutoSSA:
                EnabledAutoSSA = True
                ButtonEnabled.configure(text='AutoSSA: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoSSA: ON")
                global Amulet
                Amulet = NameAmulet.get()
                Checking()
                CheckingButtons()
                time.sleep(0.03)
                if not ThreadStarted:
                    self.ThreadManager.NewThread(ScanAutoAmulet)
                else:
                    self.ThreadManager.UnPauseThread()
            else:
                EnabledAutoSSA = False
                ButtonEnabled.configure(text='AutoSSA: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                print("AutoSSA: OFF")
                Checking()
                CheckingButtons()
                self.ThreadManager.PauseThread()

        def ScanAutoAmulet():
            global Amulet
            Amulet = NameAmulet.get()
            if CheckLifeBellowThan.get():
                BellowThan = LifeBellowThan.get()
                from Modules.AutoHeal import EnabledAutoHeal
                if EnabledAutoHeal:
                    while EnabledAutoSSA and EnabledAutoHeal:
                        NoHasAmulet = ScanAmulet(AmuletPositions, Amulet, Amulets[Amulet]["Precision"])

                        from Modules.AutoHeal import Life
                        if NoHasAmulet and Life <= BellowThan:
                            Execute()
                else:
                    from Engine.ScanStages import ScanStages
                    while EnabledAutoSSA:
                        Life = ScanStages('Life From AutoAmulet').ScanStages(HealthLocation, LifeColor, LifeColorFull)

                        if Life is None:
                            Life = 0

                        NoHasAmulet = ScanAmulet(AmuletPositions, Amulet, Amulets[Amulet]["Precision"])

                        if NoHasAmulet and Life < BellowThan:
                            Execute()
            elif not CheckLifeBellowThan.get():
                while EnabledAutoSSA:
                    NoHasAmulet = ScanAmulet(AmuletPositions, Amulet, Amulets[Amulet]["Precision"])

                    if NoHasAmulet:
                        Execute()

        def Execute():
            if RadioButton.get() == 0:
                self.SendToClient.Press(HotkeyAmulet.get())
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
                        if MOUSE_OPTION == 1:
                            MousePosition = self.SendToClient.Position()
                        else:
                            MousePosition = [0, 0]

                        self.SendToClient.DragTo([X, Y], [AmuletPositions[0] + 16, AmuletPositions[1] + 16])

                        if MOUSE_OPTION == 1:
                            self.SendToClient.MoveTo(MousePosition[0], MousePosition[1])

                        print("Amulet Reallocated On: X =", AmuletPositions[0] + 16, "Y =", AmuletPositions[1] + 16,
                              "From: X =",
                              X, "Y =", Y)
                        time.sleep(0.3)
                    else:
                        print("Lower Resolution Than Entered")
                        time.sleep(1)

        def Recapture():
            global WaitingForClick, Amulet
            WaitingForClick = True
            Amulet = NameAmulet.get()
            AutoSSAWindow = pygetwindow.getWindowsWithTitle("Module: Auto SSA")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            AutoSSAWindowX = self.AutoSSA.PositionOfWindow('X')
            AutoSSAWindowY = self.AutoSSA.PositionOfWindow('Y')
            time.sleep(0.1)
            TibiaAuto.minimize()
            AutoSSAWindow.minimize()
            Invisible = GUI('InvisibleWindow', 'InvisibleWindow')
            Invisible.InvisibleWindow('Recapture')
            while WaitingForClick:
                X, Y = GetPosition()
                if keyboard.is_pressed("c"):
                    sX, sY = GetPosition()
                    time.sleep(0.03)
                    from Core.HookWindow import SaveImage
                    SaveImage(ItemsPath + 'Amulets/' + Amulet + '.png', Region=(sX - 6, sY - 28, sX + 6, sY - 16))
                    WaitingForClick = False
                    Invisible.destroyWindow()
                    TibiaAuto.maximize()
                    time.sleep(0.04)
                    AutoSSAWindow.maximize()
                    AutoSSAWindow.moveTo(AutoSSAWindowX, AutoSSAWindowY)
                    break
                Invisible.UpdateWindow(X, Y)

        def AddNewAmulet():
            print('Option In Development...')

        def CheckClick():
            Checking()

        def ReturnGetPosition():
            global WaitingForClick
            WaitingForClick = True
            AutoSSAWindow = pygetwindow.getWindowsWithTitle("Module: Auto SSA")[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
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

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool('CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool('CheckBuff')

        RadioButton, InitiatedRadioButton = self.Setter.Variables.Int('RadioButton')

        NameAmulet, InitiatedNameAmulet = self.Setter.Variables.Str('NameAmulet')
        HotkeyAmulet, InitiatedHotkeyAmulet = self.Setter.Variables.Str('HotkeyAmulet')

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
            CheckingGUI(InitiatedNameAmulet, NameAmulet.get(), 'NameAmulet')
            CheckingGUI(InitiatedHotkeyAmulet, HotkeyAmulet.get(), 'HotkeyAmulet')
            CheckingGUI(InitiatedTextEntryX, TextEntryX.get(), 'TextEntryX')
            CheckingGUI(InitiatedTextEntryY, TextEntryY.get(), 'TextEntryY')
            CheckingGUI(InitiatedLifeBellowThan, CheckLifeBellowThan.get(), 'LifeBellowThan')
            CheckingGUI(InitiatedBellowThan, LifeBellowThan.get(), 'BellowThan')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoSSA.destroyWindow()

        self.AutoSSA.addButton('Ok', Destroy, [73, 21], [115, 365])

        global EnabledAutoSSA
        if not EnabledAutoSSA:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: OFF', SetAutoAmulet, [287, 23], [11, 336])
        else:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: ON', SetAutoAmulet, [287, 23], [11, 336])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoSSA.addCheck(VarCheckPrint, [11, 285], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoSSA.addCheck(VarCheckBuff, [11, 305], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        BackImage = 'images/Fundo.png'
        Back = self.AutoSSA.openImage(BackImage, [150, 45])

        AmuletImages = []
        AmuletName = []
        for NameOfCurrentAmulet in Amulets:
            CurrentAmuletName = ItemsPath + 'Amulets/' + NameOfCurrentAmulet + '.png'
            CurrentAmuletImage = self.AutoSSA.openImage(CurrentAmuletName, [64, 64])

            AmuletImages.append(CurrentAmuletImage)
            AmuletName.append(NameOfCurrentAmulet)

        ImgLabel = self.AutoSSA.addLabel('Image To Search', [16, 22])

        def UpdateImg():
            for XAmulet in Amulets:
                if NameAmulet.get() == XAmulet:
                    self.AutoSSA.addImage(AmuletImages[AmuletName.index(XAmulet)], [28, 43])

            global Amulet
            Amulet = NameAmulet.get()

        UpdateImg()

        WidthScreen, HeightScreen = self.SendToClient.MainWindowSize()

        AmuletLabel = self.AutoSSA.addLabel('Select Name Of Amulet', [135, 55])
        OptionNameAmulet = self.AutoSSA.addOption(NameAmulet, Amulets, [120, 80], width=21)

        ButtonAddNewAmulet = self.AutoSSA.addButton('Add New Amulet', AddNewAmulet, [167, 24], [120, 115])

        ButtonRecapture = self.AutoSSA.addButton('Recapture', Recapture, [88, 24], [22, 115])

        DescLabel = self.AutoSSA.addLabel('', [150, 140])

        RButton1 = self.AutoSSA.addRadio('Hotkey', RadioButton, 0, [22, 155], CheckClick)
        RButton2 = self.AutoSSA.addRadio('Position', RadioButton, 1, [22, 175], CheckClick)

        CheckBoxLifeBellowThan = self.AutoSSA.addCheck(CheckLifeBellowThan, [60, 210], InitiatedLifeBellowThan,
                                                       'Use Only If Life Is Bellow Than')
        LabelLifeBellowThan = self.AutoSSA.addLabel('Life <= ', [90, 245])
        PercentageLifeBellowThan = self.AutoSSA.addOption(LifeBellowThan, Percentage, [140, 240])

        def Checking():
            global FoundedImg, Amulet
            if RadioButton.get() == 0:
                DescLabel.configure(text='Hotkey To Press')
                self.AutoSSA.addImage(Back, [130, 165])
                FoundedImg = False
                HotkeyOption = self.AutoSSA.addOption(HotkeyAmulet, self.SendToClient.Hotkeys, [145, 170], 10)
                if EnabledAutoSSA:
                    HotkeyOption.configure(state='disabled')
                else:
                    HotkeyOption.configure(state='normal')
            elif RadioButton.get() == 1:
                DescLabel.configure(text='Position To Search')
                self.AutoSSA.addImage(Back, [120, 165])
                FoundedImg = False

                ButtonGetPosition = self.AutoSSA.addButton('GetPosition', ReturnGetPosition, [80, 29], [195, 173])

                LabelX = self.AutoSSA.addLabel('X:', [135, 165])
                EntryX = self.AutoSSA.addEntry([150, 165], TextEntryX, width=4)
                TextEntryX.trace("w", ValidateEntryX)
                LabelY = self.AutoSSA.addLabel('Y:', [135, 185])
                EntryY = self.AutoSSA.addEntry([150, 185], TextEntryY, width=4)
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
                Disable(CheckPrint)
                Disable(CheckBuff)

                Disable(DescLabel)
                Disable(ImgLabel)
                Disable(ButtonRecapture)
                Disable(ButtonAddNewAmulet)

                Disable(RButton1)
                Disable(RButton2)
                Disable(AmuletLabel)
                Disable(OptionNameAmulet)

                Disable(CheckBoxLifeBellowThan)
                Disable(LabelLifeBellowThan)
                Disable(PercentageLifeBellowThan)
            else:
                Enable(CheckPrint)
                Enable(CheckBuff)

                Enable(DescLabel)
                Enable(ImgLabel)
                Enable(ButtonRecapture)
                Enable(ButtonAddNewAmulet)

                Enable(RButton1)
                Enable(RButton2)
                Enable(AmuletLabel)
                Enable(OptionNameAmulet)

                Enable(CheckBoxLifeBellowThan)

                if not CheckLifeBellowThan.get():
                    Disable(LabelLifeBellowThan)
                    Disable(PercentageLifeBellowThan)
                elif CheckLifeBellowThan.get():
                    Enable(LabelLifeBellowThan)
                    Enable(PercentageLifeBellowThan)
            ExecGUITrigger()

        def ConstantVerify():
            if not EnabledAutoSSA:
                if not CheckLifeBellowThan.get():
                    Disable(LabelLifeBellowThan)
                    Disable(PercentageLifeBellowThan)
                elif CheckLifeBellowThan.get():
                    Enable(LabelLifeBellowThan)
                    Enable(PercentageLifeBellowThan)

                if NameAmulet.get() != Amulet:
                    UpdateImg()

                ExecGUITrigger()

            self.AutoSSA.After(200, ConstantVerify)

        Checking()
        CheckingButtons()

        ConstantVerify()

        self.AutoSSA.Protocol(Destroy)
        self.AutoSSA.loop()
