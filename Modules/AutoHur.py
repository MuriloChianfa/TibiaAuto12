from Engine.GUI import *
from Engine.ScanHur import ScanHur

EnabledAutoHur = False

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]


class AutoHur:
    def __init__(self, root, StatsPositions):
        self.AutoHur = GUI('AutoHur', 'Module: Auto Hur')
        self.AutoHur.DefaultWindow('DefaultWindow')

        def SetAutoHur():
            global EnabledAutoHur
            if not EnabledAutoHur:
                EnabledAutoHur = True
                ButtonEnabled.configure(text='AutoHur: ON')
                ScanAutoHur()
            else:
                EnabledAutoHur = False
                ButtonEnabled.configure(text='AutoHur: OFF')

        def ScanAutoHur():
            if EnabledAutoHur:
                if VarCheckHur.get():
                    NeedHur = ScanHur(StatsPositions)
                    if NeedHur:
                        pyautogui.press(VarHotkeyHur.get())
                        print("Hur Pressed ", VarHotkeyHur.get())

            if EnabledAutoHur:
                root.after(500, ScanAutoHur)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        VarCheckHur = tk.BooleanVar()
        VarHotkeyHur = tk.StringVar()
        VarHotkeyHur.set("f6")

        self.AutoHur.addButton('Ok', self.AutoHur.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoHur
        if not EnabledAutoHur:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: OFF', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: ON', SetAutoHur, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoHur.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        ButtonLowMana = self.AutoHur.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoHur.addLabel('Hotkey', [130, 16, 6], [218, 60])
        CheckHur = self.AutoHur.addCheck(VarCheckHur, [45, 94], [130, 16, 6], 1, "Enable Auto Hur")
        HotkeyHur = self.AutoHur.addOption(VarHotkeyHur, hotkeys, [195, 90], 8)

        self.AutoHur.loop()

