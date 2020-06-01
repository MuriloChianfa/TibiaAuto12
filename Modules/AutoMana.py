import time
import threading

from Engine.GUI import *
from Engine.ScanStages import ScanStages
from Engine.SetGUI import SetGUI
from Conf.Hotkeys import Hotkey

GUIChanges = []

EnabledAutoMana = False

manaColorFull = [45, 45, 105]

manaColor = [83, 80, 218]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoMana:
    def __init__(self, root, ManaLocation, MOUSE_OPTION, HOOK_OPTION):
        self.AutoMana = GUI('AutoMana', 'Module: Auto Mana')
        self.AutoMana.DefaultWindow('AutoMana', [306, 272], [1.2, 2.29])
        self.Setter = SetGUI("ManaLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Scan = ScanStages('Mana', HOOK_OPTION)

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
                    mana = self.Scan.ScanStages(ManaLocation, manaColor, manaColorFull)
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

        VarCheckPrint = tk.BooleanVar()
        InitiatedCheckPrint = self.Setter.GetBoolVar("CheckPrint")
        VarCheckPrint.set(InitiatedCheckPrint)

        VarCheckBuff = tk.BooleanVar()
        InitiatedCheckBuff = self.Setter.GetBoolVar("CheckBuff")
        VarCheckBuff.set(InitiatedCheckBuff)

        VarCheckStageOne = tk.BooleanVar()
        InitiatedCheckStageOne = self.Setter.GetBoolVar("CheckStageOne")
        VarCheckStageOne.set(InitiatedCheckStageOne)

        VarCheckStageTwo = tk.BooleanVar()
        InitiatedCheckStageTwo = self.Setter.GetBoolVar("CheckStageTwo")
        VarCheckStageTwo.set(InitiatedCheckStageTwo)

        VarPercentageStageOne = tk.IntVar()
        InitiatedPercentageStageOne = self.Setter.GetVar("PercentageStageOne")
        VarPercentageStageOne.set(InitiatedPercentageStageOne)

        VarHotkeyStageOne = tk.StringVar()
        InitiatedHotkeyStageOne = self.Setter.GetVar("HotkeyStageOne")
        VarHotkeyStageOne.set(InitiatedHotkeyStageOne)

        VarPercentageStageTwo = tk.IntVar()
        InitiatedPercentageStageTwo = self.Setter.GetVar("PercentageStageTwo")
        VarPercentageStageTwo.set(InitiatedPercentageStageTwo)

        VarHotkeyStageTwo = tk.StringVar()
        InitiatedHotkeyStageTwo = self.Setter.GetVar("HotkeyStageTwo")
        VarHotkeyStageTwo.set(InitiatedHotkeyStageTwo)

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
                    self.Setter.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

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

        PercentageStageOne = self.AutoMana.addOption(VarPercentageStageOne, percentage, [148, 54])
        HotkeyStageOne = self.AutoMana.addOption(VarHotkeyStageOne, self.SendToClient.Hotkeys, [223, 54])

        PercentageStageTwo = self.AutoMana.addOption(VarPercentageStageTwo, percentage, [148, 104])
        HotkeyStageTwo = self.AutoMana.addOption(VarHotkeyStageTwo, self.SendToClient.Hotkeys, [223, 104])

        def CheckingButtons():
            if EnabledAutoMana:
                CheckPrint.configure(state='disabled')
                CheckBuff.configure(state='disabled')
                StageOne.configure(state='disabled')
                StageTwo.configure(state='disabled')
                PercentageStageOne.configure(state='disabled')
                HotkeyStageOne.configure(state='disabled')
                PercentageStageTwo.configure(state='disabled')
                HotkeyStageTwo.configure(state='disabled')
                LabelPercentage.configure(state='disabled')
                LabelHotkey.configure(state='disabled')
            else:
                CheckPrint.configure(state='normal')
                CheckBuff.configure(state='normal')
                StageOne.configure(state='normal')
                StageTwo.configure(state='normal')
                PercentageStageOne.configure(state='normal')
                HotkeyStageOne.configure(state='normal')
                PercentageStageTwo.configure(state='normal')
                HotkeyStageTwo.configure(state='normal')
                LabelPercentage.configure(state='normal')
                LabelHotkey.configure(state='normal')

        CheckingButtons()

        self.AutoMana.Protocol(Destroy)
        self.AutoMana.loop()

