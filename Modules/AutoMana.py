import time

from Conf.Hotkeys import Hotkey
from Conf.Constants import ManaColor, ManaColorFull, Percentage

from Core.GUI import *
from Core.GUIManager import *
from Core.GUISetter import GUISetter
from Core.ThreadManager import ThreadManager

from Engine.ScanStages import ScanStages

EnabledAutoMana = False
ThreadStarted = False

GUIChanges = []


class AutoMana:
    def __init__(self, ManaLocation, MOUSE_OPTION):
        self.AutoMana = GUI('AutoMana', 'Module: Auto Mana')
        self.AutoMana.DefaultWindow('AutoMana', [306, 272], [1.2, 2.29])
        self.Setter = GUISetter("ManaLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Scan = ScanStages('Mana')
        self.ThreadManager = ThreadManager("ThreadAutoMana")

        def SetAutoMana():
            global EnabledAutoMana
            if not EnabledAutoMana:
                ButtonEnabled.configure(text='AutoMana: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoMana: ON")
                EnabledAutoMana = True
                CheckingButtons()
                if not ThreadStarted:
                    self.ThreadManager.NewThread(ScanAutoMana)
                else:
                    self.ThreadManager.UnPauseThread()
            else:
                print("AutoMana: OFF")
                EnabledAutoMana = False
                CheckingButtons()
                ButtonEnabled.configure(text='AutoMana: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                self.ThreadManager.PauseThread()

        def ScanAutoMana():
            while EnabledAutoMana:
                Mana = self.Scan.ScanStages(ManaLocation, ManaColor, ManaColorFull)

                if Mana is None:
                    Mana = 0

                if ManaCheckStageTwo.get():
                    stage_two = ManaPercentageStageTwo.get()
                    if stage_two > Mana or stage_two == Mana:
                        self.SendToClient.Press(ManaHotkeyStageTwo.get())
                        print("Pressed ", ManaHotkeyStageTwo.get())
                        time.sleep(.1)
                elif ManaCheckStageOne.get():
                    stage_one = ManaPercentageStageOne.get()
                    if stage_one > Mana or stage_one == Mana:
                        self.SendToClient.Press(ManaHotkeyStageOne.get())
                        print("Pressed ", ManaHotkeyStageOne.get())
                        time.sleep(.1)
                else:
                    print("Modulo Not Configured")
                    time.sleep(1)

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool('CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool('CheckBuff')

        ManaCheckStageOne, InitiatedManaCheckStageOne = self.Setter.Variables.Bool('ManaCheckStageOne')
        ManaCheckStageTwo, InitiatedManaCheckStageTwo = self.Setter.Variables.Bool('ManaCheckStageTwo')

        ManaPercentageStageOne, InitiatedManaPercentageStageOne = self.Setter.Variables.Int('ManaPercentageStageOne')
        ManaHotkeyStageOne, InitiatedManaHotkeyStageOne = self.Setter.Variables.Str('ManaHotkeyStageOne')

        ManaPercentageStageTwo, InitiatedManaPercentageStageTwo = self.Setter.Variables.Int('ManaPercentageStageTwo')
        ManaHotkeyStageTwo, InitiatedManaHotkeyStageTwo = self.Setter.Variables.Str('ManaHotkeyStageTwo')

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint, VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff, VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedManaCheckStageOne, ManaCheckStageOne.get(), 'ManaCheckStageOne')
            CheckingGUI(InitiatedManaCheckStageTwo, ManaCheckStageTwo.get(), 'ManaCheckStageTwo')
            CheckingGUI(InitiatedManaPercentageStageOne, ManaPercentageStageOne.get(), 'ManaPercentageStageOne')
            CheckingGUI(InitiatedManaHotkeyStageOne, ManaHotkeyStageOne.get(), 'ManaHotkeyStageOne')
            CheckingGUI(InitiatedManaPercentageStageTwo, ManaPercentageStageTwo.get(), 'ManaPercentageStageTwo')
            CheckingGUI(InitiatedManaHotkeyStageTwo, ManaHotkeyStageTwo.get(), 'ManaHotkeyStageTwo')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoMana.destroyWindow()

        self.AutoMana.addButton('Ok', Destroy, [73, 21], [115, 240])

        ''' button enable healing '''

        global EnabledAutoMana
        if not EnabledAutoMana:
            ButtonEnabled = self.AutoMana.addButton('AutoMana: OFF', SetAutoMana, [287, 23], [11, 211])
        else:
            ButtonEnabled = self.AutoMana.addButton('AutoMana: ON', SetAutoMana, [287, 23], [11, 211])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        LabelPercentage = self.AutoMana.addLabel('% Percentage', [145, 24])
        LabelHotkey = self.AutoMana.addLabel('HotKey', [230, 24])

        CheckPrint = self.AutoMana.addCheck(VarCheckPrint, [11, 160], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoMana.addCheck(VarCheckBuff, [11, 180], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        StageOne = self.AutoMana.addCheck(ManaCheckStageOne, [17, 55], InitiatedManaCheckStageOne, "Enable Stage One")
        StageTwo = self.AutoMana.addCheck(ManaCheckStageTwo, [17, 105], InitiatedManaCheckStageTwo, "Enable Stage Two")

        PercentageStageOne = self.AutoMana.addOption(ManaPercentageStageOne, Percentage, [148, 54])
        HotkeyStageOne = self.AutoMana.addOption(ManaHotkeyStageOne, self.SendToClient.Hotkeys, [223, 54])

        PercentageStageTwo = self.AutoMana.addOption(ManaPercentageStageTwo, Percentage, [148, 104])
        HotkeyStageTwo = self.AutoMana.addOption(ManaHotkeyStageTwo, self.SendToClient.Hotkeys, [223, 104])

        def CheckingButtons():
            if EnabledAutoMana:
                Disable(CheckPrint)
                Disable(CheckBuff)
                Disable(StageOne)
                Disable(StageTwo)
                Disable(PercentageStageOne)
                Disable(HotkeyStageOne)
                Disable(PercentageStageTwo)
                Disable(HotkeyStageTwo)
                Disable(LabelPercentage)
                Disable(LabelHotkey)
            else:
                Enable(CheckPrint)
                Enable(CheckBuff)
                Enable(StageOne)
                Enable(StageTwo)
                Enable(PercentageStageOne)
                Enable(HotkeyStageOne)
                Enable(PercentageStageTwo)
                Enable(HotkeyStageTwo)
                Enable(LabelPercentage)
                Enable(LabelHotkey)
            ExecGUITrigger()

        CheckingButtons()

        self.AutoMana.Protocol(Destroy)
        self.AutoMana.loop()
