import threading

from Engine.GUI import *
from Engine.ScanHur import ScanHur
from Conf.Hotkeys import Hotkey

EnabledAutoHur = False


class AutoHur:
    def __init__(self, root, StatsPositions, MOUSE_OPTION, HOOK_OPTION):
        self.AutoHur = GUI('AutoHur', 'Module: Auto Hur')
        self.AutoHur.DefaultWindow('AutoHur', [224, 258], [1.2, 2.29])
        self.SendToClient = Hotkey(MOUSE_OPTION)

        def SetAutoHur():
            global EnabledAutoHur
            if not EnabledAutoHur:
                EnabledAutoHur = True
                ButtonEnabled.configure(text='AutoHur: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoHur: ON")
                CheckingButtons()
                try:
                    ThreadAutoHur = threading.Thread(target=ScanAutoHur)
                    ThreadAutoHur.start()
                except:
                    print("Error: Unable To Start ThreadAutoHur!")
            else:
                EnabledAutoHur = False
                CheckingButtons()
                print("AutoHur: OFF")
                ButtonEnabled.configure(text='AutoHur: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def ScanAutoHur():
            while EnabledAutoHur:
                try:
                    NeedHur = ScanHur(StatsPositions, HOOK_OPTION)
                except Exception:
                    NeedHur = False
                    pass
                if NeedHur:
                    self.SendToClient.Press(VarHotkeyHur.get())
                    print("Hur Pressed ", VarHotkeyHur.get())

            # if EnabledAutoHur:
            # root.after(500, ScanAutoHur)

        def Recapture():
            print("recapture")

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        VarHotkeyHur = tk.StringVar()
        VarHotkeyHur.set("F6")
        CheckLowMana = tk.BooleanVar()
        CheckLowMana.set(False)

        self.AutoHur.addButton('Ok', self.AutoHur.destroyWindow, [73, 21], [75, 225])

        global EnabledAutoHur
        if not EnabledAutoHur:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: OFF', SetAutoHur, [203, 23], [11, 195])
        else:
            ButtonEnabled = self.AutoHur.addButton('AutoHur: ON', SetAutoHur, [203, 23], [11, 195])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoHur.addCheck(CheckPrint, [11, 150], 0, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoHur.addCheck(LowMana, [11, 170], 0, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        ImgHur = 'images/PlayerStats/Hur.png'
        ImageID = self.AutoHur.openImage(ImgHur, [64, 64])

        ImgLabel = self.AutoHur.addLabel('Image To Search', [16, 14])
        LabelImage = self.AutoHur.addImage(ImageID, [28, 33])

        LabelHotkey = self.AutoHur.addLabel('Hotkey', [135, 48])
        HotkeyHur = self.AutoHur.addOption(VarHotkeyHur, self.SendToClient.Hotkeys, [113, 72], 8)

        ButtonRecapture = self.AutoHur.addButton('Recapture', Recapture, [85, 24], [20, 111])

        CheckBoxLowMana = self.AutoHur.addCheck(CheckLowMana, [118, 103], 0, 'Stop With\nLowMana')

        def CheckingButtons():
            if EnabledAutoHur:
                CheckPrint.configure(state='disabled')
                CheckBuff.configure(state='disabled')

                LabelImage.configure(state='disabled')
                ImgLabel.configure(state='disabled')

                ButtonRecapture.configure(state='disabled')
                CheckBoxLowMana.configure(state='disabled')
                LabelHotkey.configure(state='disabled')
                HotkeyHur.configure(state='disabled')
            else:
                CheckPrint.configure(state='normal')
                CheckBuff.configure(state='normal')

                LabelImage.configure(state='normal')
                ImgLabel.configure(state='normal')

                ButtonRecapture.configure(state='normal')
                CheckBoxLowMana.configure(state='normal')
                LabelHotkey.configure(state='normal')
                HotkeyHur.configure(state='normal')

        CheckingButtons()

        self.AutoHur.loop()

