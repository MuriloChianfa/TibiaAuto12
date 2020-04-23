from Engine.GUI import *
from Engine.ScanHur import ScanHur
from Conf.Hotkeys import Hotkeys, PressHotkey

EnabledAutoHur = False


class AutoHur:
    def __init__(self, root, StatsPositions):
        self.AutoHur = GUI('AutoHur', 'Module: Auto Hur')
        self.AutoHur.DefaultWindow('DefaultWindow')

        def SetAutoHur():
            global EnabledAutoHur
            if not EnabledAutoHur:
                EnabledAutoHur = True
                ButtonEnabled.configure(text='AutoHur: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoHur: ON")
                CheckingButtons()
                ScanAutoHur()
            else:
                EnabledAutoHur = False
                CheckingButtons()
                print("AutoHur: OFF")
                ButtonEnabled.configure(text='AutoHur: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def ScanAutoHur():
            if EnabledAutoHur:
                if VarCheckHur.get():
                    NeedHur = ScanHur(StatsPositions)
                    if NeedHur:
                        PressHotkey(VarHotkeyHur.get())
                        print("Hur Pressed ", VarHotkeyHur.get())

            if EnabledAutoHur:
                root.after(500, ScanAutoHur)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        VarCheckHur = tk.BooleanVar()
        VarHotkeyHur = tk.StringVar()
        VarHotkeyHur.set("F6")

        self.AutoHur.addButton('Ok', self.AutoHur.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoHur
        if not EnabledAutoHur:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: OFF', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: ON', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        self.AutoHur.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        self.AutoHur.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        LabelHotkey = self.AutoHur.addLabel('Hotkey', [130, 16, 6], [218, 60])
        CheckHur = self.AutoHur.addCheck(VarCheckHur, [45, 94], [130, 16, 6], 1, "Enable Auto Hur")
        HotkeyHur = self.AutoHur.addOption(VarHotkeyHur, Hotkeys, [195, 90], 8)

        def CheckingButtons():
            if EnabledAutoHur:
                LabelHotkey.configure(state='disabled')
                CheckHur.configure(state='disabled')
                HotkeyHur.configure(state='disabled')
            else:
                LabelHotkey.configure(state='normal')
                CheckHur.configure(state='normal')
                HotkeyHur.configure(state='normal')

        CheckingButtons()

        self.AutoHur.loop()

