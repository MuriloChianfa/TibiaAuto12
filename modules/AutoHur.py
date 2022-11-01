import time
from datetime import datetime
from tkinter import RAISED, SUNKEN

from pynput.keyboard import Listener as KeyboardListener
from conf.Constants import Percentage

from conf.Hotkeys import Hotkey

from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter
from core.ThreadManager import ThreadManager

from engine.Scanners.ScanHur import ScanHur

EnabledAutoHur = False
ThreadStarted = False

GUIChanges = []


class AutoHur:
    def __init__(self, StatsPositions, SetScanningHPMP, MOUSE_OPTION):
        self.AutoHur = GUI('AutoHur', 'Module: Auto Hur')
        self.Setter = GUISetter("HurLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadAutoHur")
        self.OtherThreadManager = ThreadManager("OtherThread")
        self.AutoHur.DefaultWindow(
            'AutoHur', [224, 278], [1.2, 2.29])

        def ToggleState():
            global EnabledAutoHur
            if not EnabledAutoHur:
                EnabledAutoHur = True
                ButtonEnabled.configure(
                    text='AutoHur: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoHur: ON")
                CheckingButtons()
                SetScanningHPMP('AutoHur', 'on')
                self.ThreadManager.NewThread(Scan)
            else:
                EnabledAutoHur = False
                CheckingButtons()
                print("AutoHur: OFF")
                ButtonEnabled.configure(
                    text='AutoHur: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                SetScanningHPMP('AutoHur', 'off')
                self.ThreadManager.StopThread()

        def Scan():
            while EnabledAutoHur:
                from modules.Root import Mana

                NeedHur = ScanHur(
                    StatsPositions, VarCheckPZ.get(), CheckLowMana.get(), Mana, ManaLessThan.get())

                if NeedHur:
                    self.SendToClient.Press(VarHotkeyHur.get())
                    print("Hur Pressed ", VarHotkeyHur.get())
                    time.sleep(3)

        def Recapture():
            print("recapture")

        VarCheckPrint, InitiatedCheckPrint = self.Setter.Variables.Bool(
            'CheckPrint')
        VarCheckBuff, InitiatedCheckBuff = self.Setter.Variables.Bool(
            'CheckBuff')
        VarCheckPZ, InitiatedCheckPZ = self.Setter.Variables.Bool(
            'CheckPZ')

        VarHotkeyHur, InitiatedHotkeyHur = self.Setter.Variables.Str(
            'HotkeyHur')

        CheckLowMana, InitiatedCheckLowMana = self.Setter.Variables.Bool(
            'CheckLowMana')

        ManaLessThan, InitiatedManaLessThan = self.Setter.Variables.Int(
            'ManaLessThan')

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint,
                        VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff,
                        VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedCheckPZ, VarCheckPZ.get(), 'CheckPZ')
            CheckingGUI(InitiatedHotkeyHur,
                        VarHotkeyHur.get(), 'HotkeyHur')
            CheckingGUI(InitiatedCheckLowMana,
                        CheckLowMana.get(), 'CheckLowMana')
            CheckingGUI(InitiatedManaLessThan,
                        ManaLessThan.get(), 'ManaLessThan')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(
                        GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoHur.destroyWindow()

        self.AutoHur.addButton('OK', Destroy, [74, 23], [75, 245])

        global EnabledAutoHur
        if not EnabledAutoHur:
            ButtonEnabled = self.AutoHur.addButton(
                'AutoHur: OFF', ToggleState, [203, 24], [11, 215])
        else:
            ButtonEnabled = self.AutoHur.addButton(
                'AutoHur: ON', ToggleState, [203, 24], [11, 215])
            ButtonEnabled.configure(
                relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoHur.addCheck(
            VarCheckPrint, [11, 150], InitiatedCheckPrint, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb(
            (114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoHur.addCheck(
            VarCheckBuff, [11, 170], InitiatedCheckBuff, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb(
            (114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckPZ = self.AutoHur.addCheck(
            VarCheckPZ, [11, 190], InitiatedCheckPZ, "Hur only outside PZ")
        CheckPZ.configure(bg=rgb((114, 94, 48)), activebackground=rgb(
            (114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        ImgHur = 'images/PlayerStats/Hur.png'
        ImageID = self.AutoHur.openImage(ImgHur, [64, 64])

        ImgLabel = self.AutoHur.addLabel('Image To Search', [16, 14])
        LabelImage = self.AutoHur.addImage(ImageID, [28, 33])

        LabelHotkey = self.AutoHur.addLabel('Hotkey', [135, 14])
        HotkeyHur = self.AutoHur.addOption(
            VarHotkeyHur, self.SendToClient.Hotkeys, [113, 34], 8)

        ButtonRecapture = self.AutoHur.addButton(
            'Recapture', Recapture, [85, 24], [20, 111])

        CheckBoxLowMana = self.AutoHur.addCheck(
            CheckLowMana, [108, 60], InitiatedCheckLowMana, 'Stop when\nMana is less\nthan (%)')

        OptionManaLessThan = self.AutoHur.addOption(
            ManaLessThan, Percentage, [128, 110])

        def CheckingButtons():
            if EnabledAutoHur:
                Disable(CheckPrint)
                Disable(CheckBuff)
                Disable(CheckPZ)

                Disable(LabelImage)
                Disable(ImgLabel)

                Disable(ButtonRecapture)
                Disable(CheckBoxLowMana)
                Disable(OptionManaLessThan)
                Disable(LabelHotkey)
                Disable(HotkeyHur)
            else:
                Enable(CheckPrint)
                Enable(CheckBuff)
                Enable(CheckPZ)

                Enable(LabelImage)
                Enable(ImgLabel)

                Enable(ButtonRecapture)
                Enable(CheckBoxLowMana)
                Enable(OptionManaLessThan)
                Enable(LabelHotkey)
                Enable(HotkeyHur)
            ExecGUITrigger()

        CheckingButtons()

        self.AutoHur.Protocol(Destroy)
        self.AutoHur.loop()
