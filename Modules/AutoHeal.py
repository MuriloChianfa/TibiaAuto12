import time
import threading

from Conf.Hotkeys import Hotkey
from Conf.Constants import LifeColor, LifeColorFull, Percentage, ImageStats, Stats

from Engine.GUI import *
from Engine.GUIManager import *
from Engine.GUISetter import GUISetter

from Engine.ScanStages import ScanStages


EnabledAutoHeal = False
GUIChanges = []
Life = 0


class AutoHeal:
    def __init__(self, HealthLocation, MOUSE_OPTION):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('AutoHeal2', [306, 372], [1.2, 2.29])
        self.Setter = GUISetter("HealthLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Scan = ScanStages('Life')

        def SetAutoHeal():
            global EnabledAutoHeal
            if not EnabledAutoHeal:
                EnabledAutoHeal = True
                ButtonEnabled.configure(text='AutoHealing: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoHealing: ON")
                CheckingButtons()
                try:
                    ThreadCaveBot = threading.Thread(target=scanning_auto_life)
                    ThreadCaveBot.start()
                except:
                    print("Error: Unable To Start ThreadCaveBot!")
            else:
                EnabledAutoHeal = False
                print("AutoHealing: OFF")
                CheckingButtons()
                ButtonEnabled.configure(text='AutoHealing: OFF', relief=RAISED, bg=rgb((114, 0, 0)))

        def scanning_auto_life():
            while EnabledAutoHeal:
                global Life
                try:
                    Life = self.Scan.ScanStages(HealthLocation, LifeColor, LifeColorFull)
                except Exception:
                    Life = 100
                    pass

                if Life is None:
                    Life = 0

                if LifeCheckStageThree.get():
                    stage_three = LifePercentageStageThree.get()
                    if stage_three > Life or stage_three == Life:
                        self.SendToClient.Press(LifeHotkeyStageThree.get())
                        print("Pressed ", LifeHotkeyStageThree.get())
                        time.sleep(.15)
                    elif LifeCheckStageTwo.get():
                        stage_two = LifePercentageStageTwo.get()
                        if stage_two > Life or stage_two == Life:
                            self.SendToClient.Press(LifeHotkeyStageTwo.get())
                            print("Pressed ", LifeHotkeyStageTwo.get())
                            time.sleep(.15)
                        elif LifeCheckStageOne.get():
                            stage_one = LifePercentageStageOne.get()
                            if stage_one > Life or stage_one == Life:
                                self.SendToClient.Press(LifeHotkeyStageOne.get())
                                print("Pressed ", LifeHotkeyStageOne.get())
                                time.sleep(.15)
                    elif LifeCheckStageOne.get():
                        stage_one = LifePercentageStageOne.get()
                        if stage_one > Life or stage_one == Life:
                            self.SendToClient.Press(LifeHotkeyStageOne.get())
                            print("Pressed ", LifeHotkeyStageOne.get())
                            time.sleep(.15)
                elif LifeCheckStageTwo.get():
                    stage_two = LifePercentageStageTwo.get()
                    if stage_two > Life or stage_two == Life:
                        self.SendToClient.Press(LifeHotkeyStageTwo.get())
                        print("Pressed ", LifeHotkeyStageTwo.get())
                        time.sleep(.15)
                    elif LifeCheckStageThree.get():
                        stage_three = LifePercentageStageThree.get()
                        if stage_three > Life or stage_three == Life:
                            self.SendToClient.Press(LifeHotkeyStageThree.get())
                            print("Pressed ", LifeHotkeyStageThree.get())
                            time.sleep(.15)
                        elif LifeCheckStageOne.get():
                            stage_one = LifePercentageStageOne.get()
                            if stage_one > Life or stage_one == Life:
                                self.SendToClient.Press(LifeHotkeyStageOne.get())
                                print("Pressed ", LifeHotkeyStageOne.get())
                                time.sleep(.15)
                    elif LifeCheckStageOne.get():
                        stage_one = LifePercentageStageOne.get()
                        if stage_one > Life or stage_one == Life:
                            self.SendToClient.Press(LifeHotkeyStageOne.get())
                            print("Pressed ", LifeHotkeyStageOne.get())
                            time.sleep(.15)
                elif LifeCheckStageOne.get():
                    stage_one = LifePercentageStageOne.get()
                    if stage_one > Life or stage_one == Life:
                        self.SendToClient.Press(LifeHotkeyStageOne.get())
                        print("Pressed ", LifeHotkeyStageOne.get())
                        time.sleep(.15)
                    elif LifeCheckStageTwo.get():
                        stage_two = LifePercentageStageTwo.get()
                        if stage_two > Life or stage_two == Life:
                            self.SendToClient.Press(LifeHotkeyStageTwo.get())
                            print("Pressed ", LifeHotkeyStageTwo.get())
                            time.sleep(.15)
                        elif LifeCheckStageThree.get():
                            stage_three = LifePercentageStageThree.get()
                            if stage_three > Life or stage_three == Life:
                                self.SendToClient.Press(LifeHotkeyStageThree.get())
                                print("Pressed ", LifeHotkeyStageThree.get())
                                time.sleep(.15)
                    elif LifeCheckStageThree.get():
                        stage_three = LifePercentageStageThree.get()
                        if stage_three > Life or stage_three == Life:
                            self.SendToClient.Press(LifeHotkeyStageThree.get())
                            print("Pressed ", LifeHotkeyStageThree.get())
                            time.sleep(.15)
                else:
                    print("Module Not Configured")
                    time.sleep(1)

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool('CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool('CheckBuff')

        LifeCheckStageOne, InitiatedLifeCheckStageOne = self.Setter.Variables.Bool('LifeCheckStageOne')
        LifeCheckStageTwo, InitiatedLifeCheckStageTwo = self.Setter.Variables.Bool('LifeCheckStageTwo')
        LifeCheckStageThree, InitiatedLifeCheckStageThree = self.Setter.Variables.Bool('LifeCheckStageThree')

        VarCheckCureStats, InitiatedCheckCureStats = self.Setter.Variables.Bool('CheckCureStats')

        VarCheckParalyze, InitiatedCheckParalyze = self.Setter.Variables.Bool('CheckParalyze')
        VarCheckPoison, InitiatedCheckPoison = self.Setter.Variables.Bool('CheckPoison')
        VarCheckFire, InitiatedCheckFire = self.Setter.Variables.Bool('CheckFire')
        VarCheckElectrify, InitiatedCheckElectrify = self.Setter.Variables.Bool('CheckElectrify')
        VarCheckMort, InitiatedCheckMort = self.Setter.Variables.Bool('CheckMort')
        VarCheckBlood, InitiatedCheckBlood = self.Setter.Variables.Bool('CheckBlood')

        LifePercentageStageOne, InitiatedLifePercentageStageOne = self.Setter.Variables.Int('LifePercentageStageOne')
        LifeHotkeyStageOne, InitiatedLifeHotkeyStageOne = self.Setter.Variables.Str('LifeHotkeyStageOne')

        LifePercentageStageTwo, InitiatedLifePercentageStageTwo = self.Setter.Variables.Int('LifePercentageStageTwo')
        LifeHotkeyStageTwo, InitiatedLifeHotkeyStageTwo = self.Setter.Variables.Str('LifeHotkeyStageTwo')

        LifePercentageStageThree, InitiatedLifePercentageStageThree = self.Setter.Variables.Int('LifePercentageStageThree')
        LifeHotkeyStageThree, InitiatedLifeHotkeyStageThree = self.Setter.Variables.Str('LifeHotkeyStageThree')

        for i in range(len(Stats)):
            ImageStatus = Image.open('images/Stats/' + Stats[i] + '.webp')
            ImageStatus = ImageStatus.resize((13, 13), Image.ANTIALIAS)
            ImageStatus = ImageTk.PhotoImage(ImageStatus)
            ImageStats.append(ImageStatus)

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint, VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff, VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedLifeCheckStageOne, LifeCheckStageOne.get(), 'LifeCheckStageOne')
            CheckingGUI(InitiatedLifeCheckStageTwo, LifeCheckStageTwo.get(), 'LifeCheckStageTwo')
            CheckingGUI(InitiatedLifeCheckStageThree, LifeCheckStageThree.get(), 'LifeCheckStageThree')
            CheckingGUI(InitiatedCheckCureStats, VarCheckCureStats.get(), 'CheckCureStats')
            CheckingGUI(InitiatedCheckParalyze, VarCheckParalyze.get(), 'CheckParalyze')
            CheckingGUI(InitiatedCheckPoison, VarCheckPoison.get(), 'CheckPoison')
            CheckingGUI(InitiatedCheckFire, VarCheckFire.get(), 'CheckFire')
            CheckingGUI(InitiatedCheckElectrify, VarCheckElectrify.get(), 'CheckElectrify')
            CheckingGUI(InitiatedCheckMort, VarCheckMort.get(), 'CheckMort')
            CheckingGUI(InitiatedCheckBlood, VarCheckBlood.get(), 'CheckBlood')
            CheckingGUI(InitiatedLifePercentageStageOne, LifePercentageStageOne.get(), 'LifePercentageStageOne')
            CheckingGUI(InitiatedLifeHotkeyStageOne, LifeHotkeyStageOne.get(), 'LifeHotkeyStageOne')
            CheckingGUI(InitiatedLifePercentageStageTwo, LifePercentageStageTwo.get(), 'LifePercentageStageTwo')
            CheckingGUI(InitiatedLifeHotkeyStageTwo, LifeHotkeyStageTwo.get(), 'LifeHotkeyStageTwo')
            CheckingGUI(InitiatedLifePercentageStageThree, LifePercentageStageThree.get(), 'LifePercentageStageThree')
            CheckingGUI(InitiatedLifeHotkeyStageThree, LifeHotkeyStageThree.get(), 'LifeHotkeyStageThree')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoHeal.destroyWindow()

        self.AutoHeal.addButton('Ok', Destroy, [73, 21], [115, 340])

        ''' button enable healing '''

        global EnabledAutoHeal
        if not EnabledAutoHeal:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: OFF', SetAutoHeal, [287, 23], [11, 311])
        else:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: ON', SetAutoHeal, [287, 23], [11, 311])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoHeal.addCheck(VarCheckPrint, [11, 260], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoHeal.addCheck(VarCheckBuff, [11, 280], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        LabelPercentage = self.AutoHeal.addLabel('% Percentage', [145, 24])
        LabelHotkey = self.AutoHeal.addLabel('HotKey', [230, 24])

        StageOne = self.AutoHeal.addCheck(LifeCheckStageOne, [17, 55], InitiatedLifeCheckStageOne, "Enable Stage One")
        StageTwo = self.AutoHeal.addCheck(LifeCheckStageTwo, [17, 105], InitiatedLifeCheckStageTwo, "Enable Stage Two")
        StageThree = self.AutoHeal.addCheck(LifeCheckStageThree, [17, 155], InitiatedLifeCheckStageThree, "Enable Stage Three")
        CheckStats = self.AutoHeal.addCheck(VarCheckCureStats, [95, 192], InitiatedCheckCureStats, "Enable Cure Stats")

        Paralyze = self.AutoHeal.addCheck(VarCheckParalyze, [40, 226], InitiatedCheckParalyze, '', ImageStats[0])
        Poison = self.AutoHeal.addCheck(VarCheckPoison, [80, 226], InitiatedCheckPoison, '', ImageStats[1])
        Fire = self.AutoHeal.addCheck(VarCheckFire, [120, 226], InitiatedCheckFire, '', ImageStats[2])
        Electrify = self.AutoHeal.addCheck(VarCheckElectrify, [160, 226], InitiatedCheckElectrify, '', ImageStats[3])
        Mort = self.AutoHeal.addCheck(VarCheckMort, [200, 226], InitiatedCheckMort, '', ImageStats[4])
        Blood = self.AutoHeal.addCheck(VarCheckBlood, [240, 226], InitiatedCheckBlood, '', ImageStats[5])

        PercentageStageOne = self.AutoHeal.addOption(LifePercentageStageOne, Percentage, [148, 54])
        HotkeyStageOne = self.AutoHeal.addOption(LifeHotkeyStageOne, self.SendToClient.Hotkeys, [223, 54])

        PercentageStageTwo = self.AutoHeal.addOption(LifePercentageStageTwo, Percentage, [148, 104])
        HotkeyStageTwo = self.AutoHeal.addOption(LifeHotkeyStageTwo, self.SendToClient.Hotkeys, [223, 104])

        PercentageStageThree = self.AutoHeal.addOption(LifePercentageStageThree, Percentage, [148, 154])
        HotkeyStageThree = self.AutoHeal.addOption(LifeHotkeyStageThree, self.SendToClient.Hotkeys, [223, 154])

        def CheckingButtons():
            if EnabledAutoHeal:
                Disable(CheckStats)
                Disable(StageThree)
                Disable(StageTwo)
                Disable(StageOne)
                Disable(LabelHotkey)
                Disable(LabelPercentage)
                Disable(PercentageStageOne)
                Disable(HotkeyStageOne)
                Disable(PercentageStageTwo)
                Disable(HotkeyStageTwo)
                Disable(PercentageStageThree)
                Disable(HotkeyStageThree)
                Disable(Paralyze)
                Disable(Poison)
                Disable(Fire)
                Disable(Electrify)
                Disable(Mort)
                Disable(Blood)
                Disable(CheckPrint)
                Disable(CheckBuff)
            else:
                Enable(CheckStats)
                Enable(StageThree)
                Enable(StageTwo)
                Enable(StageOne)
                Enable(LabelHotkey)
                Enable(LabelPercentage)
                Enable(PercentageStageOne)
                Enable(HotkeyStageOne)
                Enable(PercentageStageTwo)
                Enable(HotkeyStageTwo)
                Enable(PercentageStageThree)
                Enable(HotkeyStageThree)
                Enable(CheckPrint)
                Enable(CheckBuff)
                if not VarCheckCureStats.get():
                    Disable(Paralyze)
                    Disable(Poison)
                    Disable(Fire)
                    Disable(Electrify)
                    Disable(Mort)
                    Disable(Blood)
                elif VarCheckCureStats.get():
                    Enable(Paralyze)
                    Enable(Poison)
                    Enable(Fire)
                    Enable(Electrify)
                    Enable(Mort)
                    Enable(Blood)
            ExecGUITrigger()

        def ConstantVerify():
            if not EnabledAutoHeal:
                if not VarCheckCureStats.get():
                    Disable(Paralyze)
                    Disable(Poison)
                    Disable(Fire)
                    Disable(Electrify)
                    Disable(Mort)
                    Disable(Blood)
                elif VarCheckCureStats.get():
                    Enable(Paralyze)
                    Enable(Poison)
                    Enable(Fire)
                    Enable(Electrify)
                    Enable(Mort)
                    Enable(Blood)
                ExecGUITrigger()

            self.AutoHeal.After(30, ConstantVerify)

        CheckingButtons()

        ConstantVerify()

        self.AutoHeal.Protocol(Destroy)
        self.AutoHeal.loop()
