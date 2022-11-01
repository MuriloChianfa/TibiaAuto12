from multiprocessing import Process
from time import sleep
from tkinter.constants import RAISED, SUNKEN

from conf.Hotkeys import Hotkey
from conf.Constants import LifeColor, LifeColorFull, ManaColor, ManaColorFull, HealingType, Percentage, ImageStats, Stats


from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter
from core.ThreadManager import ThreadManager


EnabledAutoHeal = False
ThreadStarted = False
Stages = []

GUIChanges = []


class AutoHeal:
    def __init__(self, SetScanningHPMP, MOUSE_OPTION):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('AutoHeal2', [446, 509], [1.2, 2.29])
        self.Setter = GUISetter("HealLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadAutoHeal")

        def ToggleState():
            global EnabledAutoHeal
            if not EnabledAutoHeal:
                EnabledAutoHeal = True
                ButtonEnabled.configure(
                    text='AutoHealing: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoHealing: ON")
                CheckingButtons()
                SetScanningHPMP('AutoHeal', 'on')
                self.ThreadManager.NewThread(Scan)
            else:
                EnabledAutoHeal = False
                print("AutoHealing: OFF")
                CheckingButtons()
                ButtonEnabled.configure(
                    text='AutoHealing: OFF', relief=RAISED, bg=rgb((114, 0, 0)))
                SetScanningHPMP('AutoHeal', 'off')
                self.ThreadManager.StopThread()

        def Scan():
            while EnabledAutoHeal:
                from modules.Root import Life, Mana
                for StageChecked, StagePercentage, StageType, StageHotkey in Stages:
                    if StageChecked.get() and StagePercentage.get() >= locals()[StageType.get()]:
                        self.SendToClient.Press(StageHotkey.get())
                        print(
                            f'{StageType.get()} is less than {StagePercentage.get()}.')
                        print(f"Pressed {StageHotkey.get()}")
                        sleep(.7)
                        break

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool(
            'CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool(
            'CheckBuff')

        LifeCheckStageOne, InitiatedLifeCheckStageOne = self.Setter.Variables.Bool(
            'LifeCheckStageOne')
        LifeCheckStageTwo, InitiatedLifeCheckStageTwo = self.Setter.Variables.Bool(
            'LifeCheckStageTwo')
        LifeCheckStageThree, InitiatedLifeCheckStageThree = self.Setter.Variables.Bool(
            'LifeCheckStageThree')
        LifeCheckStageFour, InitiatedLifeCheckStageFour = self.Setter.Variables.Bool(
            'LifeCheckStageFour')
        LifeCheckStageFive, InitiatedLifeCheckStageFive = self.Setter.Variables.Bool(
            'LifeCheckStageFive')
        LifeCheckStageSix, InitiatedLifeCheckStageSix = self.Setter.Variables.Bool(
            'LifeCheckStageSix')

        VarCheckCureStats, InitiatedCheckCureStats = self.Setter.Variables.Bool(
            'CheckCureStats')

        VarCheckParalyze, InitiatedCheckParalyze = self.Setter.Variables.Bool(
            'CheckParalyze')
        VarCheckPoison, InitiatedCheckPoison = self.Setter.Variables.Bool(
            'CheckPoison')
        VarCheckFire, InitiatedCheckFire = self.Setter.Variables.Bool(
            'CheckFire')
        VarCheckElectrify, InitiatedCheckElectrify = self.Setter.Variables.Bool(
            'CheckElectrify')
        VarCheckMort, InitiatedCheckMort = self.Setter.Variables.Bool(
            'CheckMort')
        VarCheckBlood, InitiatedCheckBlood = self.Setter.Variables.Bool(
            'CheckBlood')

        LifePercentageStageOne, InitiatedLifePercentageStageOne = self.Setter.Variables.Int(
            'LifePercentageStageOne')
        LifeHotkeyStageOne, InitiatedLifeHotkeyStageOne = self.Setter.Variables.Str(
            'LifeHotkeyStageOne')
        TypeStageOne, InitiatedTypeStageOne = self.Setter.Variables.Str(
            'TypeStageOne')

        LifePercentageStageTwo, InitiatedLifePercentageStageTwo = self.Setter.Variables.Int(
            'LifePercentageStageTwo')
        LifeHotkeyStageTwo, InitiatedLifeHotkeyStageTwo = self.Setter.Variables.Str(
            'LifeHotkeyStageTwo')
        TypeStageTwo, InitiatedTypeStageTwo = self.Setter.Variables.Str(
            'TypeStageTwo')

        LifePercentageStageThree, InitiatedLifePercentageStageThree = self.Setter.Variables.Int(
            'LifePercentageStageThree')
        LifeHotkeyStageThree, InitiatedLifeHotkeyStageThree = self.Setter.Variables.Str(
            'LifeHotkeyStageThree')
        TypeStageThree, InitiatedTypeStageThree = self.Setter.Variables.Str(
            'TypeStageThree')

        LifePercentageStageFour, InitiatedLifePercentageStageFour = self.Setter.Variables.Int(
            'LifePercentageStageFour')
        LifeHotkeyStageFour, InitiatedLifeHotkeyStageFour = self.Setter.Variables.Str(
            'LifeHotkeyStageFour')
        TypeStageFour, InitiatedTypeStageFour = self.Setter.Variables.Str(
            'TypeStageFour')

        LifePercentageStageFive, InitiatedLifePercentageStageFive = self.Setter.Variables.Int(
            'LifePercentageStageFive')
        LifeHotkeyStageFive, InitiatedLifeHotkeyStageFive = self.Setter.Variables.Str(
            'LifeHotkeyStageFive')
        TypeStageFive, InitiatedTypeStageFive = self.Setter.Variables.Str(
            'TypeStageFive')

        LifePercentageStageSix, InitiatedLifePercentageStageSix = self.Setter.Variables.Int(
            'LifePercentageStageSix')
        LifeHotkeyStageSix, InitiatedLifeHotkeyStageSix = self.Setter.Variables.Str(
            'LifeHotkeyStageSix')
        TypeStageSix, InitiatedTypeStageSix = self.Setter.Variables.Str(
            'TypeStageSix')

        global Stages
        Stages = [
            (
                LifeCheckStageOne,
                LifePercentageStageOne,
                TypeStageOne,
                LifeHotkeyStageOne
            ),
            (
                LifeCheckStageTwo,
                LifePercentageStageTwo,
                TypeStageTwo,
                LifeHotkeyStageTwo
            ),
            (
                LifeCheckStageThree,
                LifePercentageStageThree,
                TypeStageThree,
                LifeHotkeyStageThree
            ),
            (
                LifeCheckStageFour,
                LifePercentageStageFour,
                TypeStageFour,
                LifeHotkeyStageFour
            ),
            (
                LifeCheckStageFive,
                LifePercentageStageFive,
                TypeStageFive,
                LifeHotkeyStageFive
            ),
            (
                LifeCheckStageSix,
                LifePercentageStageSix,
                TypeStageSix,
                LifeHotkeyStageSix
            ),

        ]

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
            CheckingGUI(InitiatedLifeCheckStageOne,
                        LifeCheckStageOne.get(), 'LifeCheckStageOne')
            CheckingGUI(InitiatedLifeCheckStageTwo,
                        LifeCheckStageTwo.get(), 'LifeCheckStageTwo')
            CheckingGUI(InitiatedLifeCheckStageThree,
                        LifeCheckStageThree.get(), 'LifeCheckStageThree')
            CheckingGUI(InitiatedLifeCheckStageFour,
                        LifeCheckStageFour.get(), 'LifeCheckStageFour')
            CheckingGUI(InitiatedLifeCheckStageFive,
                        LifeCheckStageFive.get(), 'LifeCheckStageFive')
            CheckingGUI(InitiatedLifeCheckStageSix,
                        LifeCheckStageSix.get(), 'LifeCheckStageSix')
            CheckingGUI(InitiatedCheckCureStats,
                        VarCheckCureStats.get(), 'CheckCureStats')
            CheckingGUI(InitiatedCheckParalyze,
                        VarCheckParalyze.get(), 'CheckParalyze')
            CheckingGUI(InitiatedCheckPoison,
                        VarCheckPoison.get(), 'CheckPoison')
            CheckingGUI(InitiatedCheckFire, VarCheckFire.get(), 'CheckFire')
            CheckingGUI(InitiatedCheckElectrify,
                        VarCheckElectrify.get(), 'CheckElectrify')
            CheckingGUI(InitiatedCheckMort, VarCheckMort.get(), 'CheckMort')
            CheckingGUI(InitiatedCheckBlood, VarCheckBlood.get(), 'CheckBlood')
            CheckingGUI(InitiatedLifePercentageStageOne,
                        LifePercentageStageOne.get(), 'LifePercentageStageOne')
            CheckingGUI(InitiatedLifeHotkeyStageOne,
                        LifeHotkeyStageOne.get(), 'LifeHotkeyStageOne')
            CheckingGUI(InitiatedTypeStageOne,
                        TypeStageOne.get(), 'TypeStageOne')
            CheckingGUI(InitiatedLifePercentageStageTwo,
                        LifePercentageStageTwo.get(), 'LifePercentageStageTwo')
            CheckingGUI(InitiatedLifeHotkeyStageTwo,
                        LifeHotkeyStageTwo.get(), 'LifeHotkeyStageTwo')
            CheckingGUI(InitiatedTypeStageTwo,
                        TypeStageTwo.get(), 'TypeStageTwo')
            CheckingGUI(InitiatedLifePercentageStageThree,
                        LifePercentageStageThree.get(), 'LifePercentageStageThree')
            CheckingGUI(InitiatedLifeHotkeyStageThree,
                        LifeHotkeyStageThree.get(), 'LifeHotkeyStageThree')
            CheckingGUI(InitiatedTypeStageThree,
                        TypeStageThree.get(), 'TypeStageThree')
            CheckingGUI(InitiatedLifePercentageStageFour,
                        LifePercentageStageFour.get(), 'LifePercentageStageFour')
            CheckingGUI(InitiatedLifeHotkeyStageFour,
                        LifeHotkeyStageFour.get(), 'LifeHotkeyStageFour')
            CheckingGUI(InitiatedTypeStageFour,
                        TypeStageFour.get(), 'TypeStageFour')
            CheckingGUI(InitiatedLifePercentageStageFive,
                        LifePercentageStageFive.get(), 'LifePercentageStageFive')
            CheckingGUI(InitiatedLifeHotkeyStageFive,
                        LifeHotkeyStageFive.get(), 'LifeHotkeyStageFive')
            CheckingGUI(InitiatedTypeStageFive,
                        TypeStageFive.get(), 'TypeStageFive')
            CheckingGUI(InitiatedLifePercentageStageSix,
                        LifePercentageStageSix.get(), 'LifePercentageStageSix')
            CheckingGUI(InitiatedLifeHotkeyStageSix,
                        LifeHotkeyStageSix.get(), 'LifeHotkeyStageSix')
            CheckingGUI(InitiatedTypeStageSix,
                        TypeStageSix.get(), 'TypeStageSix')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(
                        GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoHeal.destroyWindow()

        self.AutoHeal.addButton('OK', Destroy, [75, 23], [196, 480])

        ''' Button enable auto healing '''

        global EnabledAutoHeal
        if not EnabledAutoHeal:
            ButtonEnabled = self.AutoHeal.addButton(
                'AutoHealing: OFF', ToggleState, [287, 23], [91, 452])
        else:
            ButtonEnabled = self.AutoHeal.addButton(
                'AutoHealing: ON', ToggleState, [287, 23], [91, 452])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoHeal.addCheck(
            VarCheckPrint, [11, 402], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb(
            (114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoHeal.addCheck(
            VarCheckBuff, [11, 422], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb(
            (114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        LabelType = self.AutoHeal.addLabel('Type', [144, 24])
        LabelPercentage = self.AutoHeal.addLabel('% Perc.', [228, 24])
        LabelHotkey = self.AutoHeal.addLabel('Hotkey', [312, 24])

        StageOne = self.AutoHeal.addCheck(
            LifeCheckStageOne, [17, 55], InitiatedLifeCheckStageOne, "Enable Stage One")
        StageTwo = self.AutoHeal.addCheck(
            LifeCheckStageTwo, [17, 105], InitiatedLifeCheckStageTwo, "Enable Stage Two")
        StageThree = self.AutoHeal.addCheck(LifeCheckStageThree, [
                                            17, 155], InitiatedLifeCheckStageThree, "Enable Stage Three")
        StageFour = self.AutoHeal.addCheck(
            LifeCheckStageFour, [17, 205], InitiatedLifeCheckStageFour, "Enable Stage Four")
        StageFive = self.AutoHeal.addCheck(
            LifeCheckStageFive, [17, 255], InitiatedLifeCheckStageFive, "Enable Stage Five")
        StageSix = self.AutoHeal.addCheck(
            LifeCheckStageSix, [17, 305], InitiatedLifeCheckStageSix, "Enable Stage Six")
        CheckStats = self.AutoHeal.addCheck(
            VarCheckCureStats, [170, 339], InitiatedCheckCureStats, "Enable Cure Stats")

        Paralyze = self.AutoHeal.addCheck(
            VarCheckParalyze, [114, 364], InitiatedCheckParalyze, '', ImageStats[0])
        Poison = self.AutoHeal.addCheck(
            VarCheckPoison, [155, 364], InitiatedCheckPoison, '', ImageStats[1])
        Fire = self.AutoHeal.addCheck(
            VarCheckFire, [195, 364], InitiatedCheckFire, '', ImageStats[2])
        Electrify = self.AutoHeal.addCheck(
            VarCheckElectrify, [235, 364], InitiatedCheckElectrify, '', ImageStats[3])
        Mort = self.AutoHeal.addCheck(
            VarCheckMort, [275, 364], InitiatedCheckMort, '', ImageStats[4])
        Blood = self.AutoHeal.addCheck(
            VarCheckBlood, [315, 364], InitiatedCheckBlood, '', ImageStats[5])

        TypeStageOneOption = self.AutoHeal.addOption(
            TypeStageOne, HealingType, [148, 54], width=6)
        PercentageStageOneOption = self.AutoHeal.addOption(
            LifePercentageStageOne, Percentage, [232, 54], width=6)
        HotkeyStageOneOption = self.AutoHeal.addOption(
            LifeHotkeyStageOne, self.SendToClient.Hotkeys, [316, 54], width=6)

        TypeStageTwoOption = self.AutoHeal.addOption(
            TypeStageTwo, HealingType, [148, 104], width=6)
        PercentageStageTwoOption = self.AutoHeal.addOption(
            LifePercentageStageTwo, Percentage, [232, 104], width=6)
        HotkeyStageTwoOption = self.AutoHeal.addOption(
            LifeHotkeyStageTwo, self.SendToClient.Hotkeys, [316, 104], width=6)

        TypeStageThreeOption = self.AutoHeal.addOption(
            TypeStageThree, HealingType, [148, 154], width=6)
        PercentageStageThreeOption = self.AutoHeal.addOption(
            LifePercentageStageThree, Percentage, [232, 154], width=6)
        HotkeyStageThreeOption = self.AutoHeal.addOption(
            LifeHotkeyStageThree, self.SendToClient.Hotkeys, [316, 154], width=6)

        TypeStageFourOption = self.AutoHeal.addOption(
            TypeStageFour, HealingType, [148, 204], width=6)
        PercentageStageFourOption = self.AutoHeal.addOption(
            LifePercentageStageFour, Percentage, [232, 204], width=6)
        HotkeyStageFourOption = self.AutoHeal.addOption(
            LifeHotkeyStageFour, self.SendToClient.Hotkeys, [316, 204], width=6)

        TypeStageFiveOption = self.AutoHeal.addOption(
            TypeStageFive, HealingType, [148, 254], width=6)
        PercentageStageFiveOption = self.AutoHeal.addOption(
            LifePercentageStageFive, Percentage, [232, 254], width=6)
        HotkeyStageFiveOption = self.AutoHeal.addOption(
            LifeHotkeyStageFive, self.SendToClient.Hotkeys, [316, 254], width=6)

        TypeStageSixOption = self.AutoHeal.addOption(
            TypeStageSix, HealingType, [148, 304], width=6)
        PercentageStageSixOption = self.AutoHeal.addOption(
            LifePercentageStageSix, Percentage, [232, 304], width=6)
        HotkeyStageSixOption = self.AutoHeal.addOption(
            LifeHotkeyStageSix, self.SendToClient.Hotkeys, [316, 304], width=6)

        def CheckingButtons():
            if EnabledAutoHeal:
                Disable(CheckStats)
                Disable(StageSix)
                Disable(StageFive)
                Disable(StageFour)
                Disable(StageThree)
                Disable(StageTwo)
                Disable(StageOne)
                Disable(LabelHotkey)
                Disable(LabelPercentage)
                Disable(LabelType)
                Disable(TypeStageOneOption)
                Disable(PercentageStageOneOption)
                Disable(HotkeyStageOneOption)
                Disable(TypeStageTwoOption)
                Disable(PercentageStageTwoOption)
                Disable(HotkeyStageTwoOption)
                Disable(TypeStageThreeOption)
                Disable(PercentageStageThreeOption)
                Disable(HotkeyStageThreeOption)
                Disable(TypeStageFourOption)
                Disable(PercentageStageFourOption)
                Disable(HotkeyStageFourOption)
                Disable(TypeStageFiveOption)
                Disable(PercentageStageFiveOption)
                Disable(HotkeyStageFiveOption)
                Disable(TypeStageSixOption)
                Disable(PercentageStageSixOption)
                Disable(HotkeyStageSixOption)
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
                Enable(StageSix)
                Enable(StageFive)
                Enable(StageFour)
                Enable(StageThree)
                Enable(StageTwo)
                Enable(StageOne)
                Enable(LabelHotkey)
                Enable(LabelPercentage)
                Enable(LabelType)
                Enable(TypeStageOneOption)
                Enable(PercentageStageOneOption)
                Enable(HotkeyStageOneOption)
                Enable(TypeStageTwoOption)
                Enable(PercentageStageTwoOption)
                Enable(HotkeyStageTwoOption)
                Enable(TypeStageThreeOption)
                Enable(PercentageStageThreeOption)
                Enable(HotkeyStageThreeOption)
                Enable(TypeStageFourOption)
                Enable(PercentageStageFourOption)
                Enable(HotkeyStageFourOption)
                Enable(TypeStageFiveOption)
                Enable(PercentageStageFiveOption)
                Enable(HotkeyStageFiveOption)
                Enable(TypeStageSixOption)
                Enable(PercentageStageSixOption)
                Enable(HotkeyStageSixOption)
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
