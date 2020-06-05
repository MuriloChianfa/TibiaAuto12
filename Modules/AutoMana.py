import time
import threading

from Conf.Hotkeys import Hotkey
from Conf.Constants import GUIChanges, ManaColor, ManaColorFull, Percentage

from Engine.GUI import *
from Engine.GUIManager import *
from Engine.GUISetter import GUISetter

from Engine.ScanStages import ScanStages

EnabledAutoMana = False


class AutoMana:
    def __init__(self, ManaLocation, MOUSE_OPTION):
        self.AutoMana = GUI('AutoMana', 'Module: Auto Mana')
        self.AutoMana.DefaultWindow('AutoMana', [306, 272], [1.2, 2.29])
        self.Setter = GUISetter("ManaLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Scan = ScanStages('Mana')

        def SetAutoMana():
            global EnabledAutoMana
            if not EnabledAutoMana:
                EnabledAutoMana = True
                ButtonEnabled.configure(text='AutoMana: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoMana: ON")
                CheckingButtons()
                try:
                    ThreadAutoMana = threading.Thread(target=ScanAutoMana)
                    ThreadAutoMana.start()
                except:
                    print("Error: Unable To Start ThreadAutoMana!")
            else:
                EnabledAutoMana = False
                print("AutoMana: OFF")
                CheckingButtons()
                ButtonEnabled.configure(text='AutoMana: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def ScanAutoMana():
            while EnabledAutoMana:
                try:
                    mana = self.Scan.ScanStages(ManaLocation, ManaColor, ManaColorFull)
                except Exception:
                    mana = 100
                    pass

                if mana is None:
                    mana = 0

                if VarCheckStageTwo.get():
                    stage_two = VarPercentageStageTwo.get()
                    if stage_two > mana or stage_two == mana:
                        self.SendToClient.Press(VarHotkeyStageTwo.get())
                        print("Pressed ", VarHotkeyStageTwo.get())
                        time.sleep(.1)
                elif VarCheckStageOne.get():
                    stage_one = VarPercentageStageOne.get()
                    if stage_one > mana or stage_one == mana:
                        self.SendToClient.Press(VarHotkeyStageOne.get())
                        print("Pressed ", VarHotkeyStageOne.get())
                        time.sleep(.1)
                else:
                    print("Modulo Not Configured")
                    time.sleep(1)

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool('CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool('CheckBuff')

        VarCheckStageOne, InitiatedCheckStageOne = self.Setter.Variables.Bool('CheckStageOne')
        VarCheckStageTwo, InitiatedCheckStageTwo = self.Setter.Variables.Bool('CheckStageTwo')

        VarPercentageStageOne, InitiatedPercentageStageOne = self.Setter.Variables.Int('PercentageStageOne')
        VarHotkeyStageOne, InitiatedHotkeyStageOne = self.Setter.Variables.Str('HotkeyStageOne')

        VarPercentageStageTwo, InitiatedPercentageStageTwo = self.Setter.Variables.Int('PercentageStageTwo')
        VarHotkeyStageTwo, InitiatedHotkeyStageTwo = self.Setter.Variables.Str('HotkeyStageTwo')

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint, VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff, VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedCheckStageOne, VarCheckStageOne.get(), 'CheckStageOne')
            CheckingGUI(InitiatedCheckStageTwo, VarCheckStageTwo.get(), 'CheckStageTwo')
            CheckingGUI(InitiatedPercentageStageOne, VarPercentageStageOne.get(), 'PercentageStageOne')
            CheckingGUI(InitiatedHotkeyStageOne, VarHotkeyStageOne.get(), 'HotkeyStageOne')
            CheckingGUI(InitiatedPercentageStageTwo, VarPercentageStageTwo.get(), 'PercentageStageTwo')
            CheckingGUI(InitiatedHotkeyStageTwo, VarHotkeyStageTwo.get(), 'HotkeyStageTwo')

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

        StageOne = self.AutoMana.addCheck(VarCheckStageOne, [17, 55], InitiatedCheckStageOne, "Enable Stage One")
        StageTwo = self.AutoMana.addCheck(VarCheckStageTwo, [17, 105], InitiatedCheckStageTwo, "Enable Stage Two")

        PercentageStageOne = self.AutoMana.addOption(VarPercentageStageOne, Percentage, [148, 54])
        HotkeyStageOne = self.AutoMana.addOption(VarHotkeyStageOne, self.SendToClient.Hotkeys, [223, 54])

        PercentageStageTwo = self.AutoMana.addOption(VarPercentageStageTwo, Percentage, [148, 104])
        HotkeyStageTwo = self.AutoMana.addOption(VarHotkeyStageTwo, self.SendToClient.Hotkeys, [223, 104])

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
