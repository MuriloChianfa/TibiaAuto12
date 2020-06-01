import time
import threading

from Engine.GUI import *
from Engine.ScanStages import ScanStages
from Engine.SetGUI import SetGUI
from Conf.Hotkeys import Hotkey

GUIChanges = []

EnabledAutoHeal = False

life = 0

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation, MOUSE_OPTION, HOOK_OPTION):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('AutoHeal2', [306, 372], [1.2, 2.29])
        self.Setter = SetGUI("HealthLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Scan = ScanStages('Life', HOOK_OPTION)

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
                global life
                try:
                    life = self.Scan.ScanStages(HealthLocation, lifeColor, lifeColorFull)
                except Exception:
                    life = 100
                    pass

                if life is None:
                    life = 0

                if VarCheckStageThree.get():
                    stage_three = VarPercentageStageThree.get()
                    if stage_three > life or stage_three == life:
                        self.SendToClient.Press(VarHotkeyStageThree.get())
                        print("Pressed ", VarHotkeyStageThree.get())
                        time.sleep(.15)
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            self.SendToClient.Press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                            time.sleep(.15)
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                self.SendToClient.Press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                                time.sleep(.15)
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            self.SendToClient.Press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                            time.sleep(.15)
                elif VarCheckStageTwo.get():
                    stage_two = VarPercentageStageTwo.get()
                    if stage_two > life or stage_two == life:
                        self.SendToClient.Press(VarHotkeyStageTwo.get())
                        print("Pressed ", VarHotkeyStageTwo.get())
                        time.sleep(.15)
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            self.SendToClient.Press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                            time.sleep(.15)
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                self.SendToClient.Press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                                time.sleep(.15)
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            self.SendToClient.Press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                            time.sleep(.15)
                elif VarCheckStageOne.get():
                    stage_one = VarPercentageStageOne.get()
                    if stage_one > life or stage_one == life:
                        self.SendToClient.Press(VarHotkeyStageOne.get())
                        print("Pressed ", VarHotkeyStageOne.get())
                        time.sleep(.15)
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            self.SendToClient.Press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                            time.sleep(.15)
                        elif VarCheckStageThree.get():
                            stage_three = VarPercentageStageThree.get()
                            if stage_three > life or stage_three == life:
                                self.SendToClient.Press(VarHotkeyStageThree.get())
                                print("Pressed ", VarHotkeyStageThree.get())
                                time.sleep(.15)
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            self.SendToClient.Press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                            time.sleep(.15)
                else:
                    print("Module Not Configured")
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

        VarCheckStageThree = tk.BooleanVar()
        InitiatedCheckStageThree = self.Setter.GetBoolVar("CheckStageThree")
        VarCheckStageThree.set(InitiatedCheckStageThree)

        VarCheckCureStats = tk.BooleanVar()
        InitiatedCheckCureStats = self.Setter.GetBoolVar("CheckCureStats")
        VarCheckCureStats.set(InitiatedCheckCureStats)

        VarCheckParalyze = tk.BooleanVar()
        InitiatedCheckParalyze = self.Setter.GetBoolVar("CheckParalyze")
        VarCheckParalyze.set(InitiatedCheckParalyze)

        VarCheckPoison = tk.BooleanVar()
        InitiatedCheckPoison = self.Setter.GetBoolVar("CheckPoison")
        VarCheckPoison.set(InitiatedCheckPoison)

        VarCheckFire = tk.BooleanVar()
        InitiatedCheckFire = self.Setter.GetBoolVar("CheckFire")
        VarCheckFire.set(InitiatedCheckFire)

        VarCheckElectrify = tk.BooleanVar()
        InitiatedCheckElectrify = self.Setter.GetBoolVar("CheckElectrify")
        VarCheckElectrify.set(InitiatedCheckElectrify)

        VarCheckMort = tk.BooleanVar()
        InitiatedCheckMort = self.Setter.GetBoolVar("CheckMort")
        VarCheckMort.set(InitiatedCheckMort)

        VarCheckBlood = tk.BooleanVar()
        InitiatedCheckBlood = self.Setter.GetBoolVar("CheckBlood")
        VarCheckBlood.set(InitiatedCheckBlood)

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

        VarPercentageStageThree = tk.IntVar()
        InitiatedPercentageStageThree = self.Setter.GetVar("PercentageStageThree")
        VarPercentageStageThree.set(InitiatedPercentageStageThree)

        VarHotkeyStageThree = tk.StringVar()
        InitiatedHotkeyStageThree = self.Setter.GetVar("HotkeyStageThree")
        VarHotkeyStageThree.set(InitiatedHotkeyStageThree)

        ParalyzeImage = ImageTk.PhotoImage(Image.open('images/Stats/paralyze.webp'))
        PoisonImage = ImageTk.PhotoImage(Image.open('images/Stats/poison.webp'))
        FireImage = ImageTk.PhotoImage(Image.open('images/Stats/fire.webp'))
        ElectrifyImage = ImageTk.PhotoImage(Image.open('images/Stats/electrify.webp'))
        MortImage = ImageTk.PhotoImage(Image.open('images/Stats/mort.webp'))
        BloodImage = ImageTk.PhotoImage(Image.open('images/Stats/blood.webp'))

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedCheckPrint, VarCheckPrint.get(), 'CheckPrint')
            CheckingGUI(InitiatedCheckBuff, VarCheckBuff.get(), 'CheckBuff')
            CheckingGUI(InitiatedCheckStageOne, VarCheckStageOne.get(), 'CheckStageOne')
            CheckingGUI(InitiatedCheckStageTwo, VarCheckStageTwo.get(), 'CheckStageTwo')
            CheckingGUI(InitiatedCheckStageThree, VarCheckStageThree.get(), 'CheckStageThree')
            CheckingGUI(InitiatedCheckCureStats, VarCheckCureStats.get(), 'CheckCureStats')
            CheckingGUI(InitiatedCheckParalyze, VarCheckParalyze.get(), 'CheckParalyze')
            CheckingGUI(InitiatedCheckPoison, VarCheckPoison.get(), 'CheckPoison')
            CheckingGUI(InitiatedCheckFire, VarCheckFire.get(), 'CheckFire')
            CheckingGUI(InitiatedCheckElectrify, VarCheckElectrify.get(), 'CheckElectrify')
            CheckingGUI(InitiatedCheckMort, VarCheckMort.get(), 'CheckMort')
            CheckingGUI(InitiatedCheckBlood, VarCheckBlood.get(), 'CheckBlood')
            CheckingGUI(InitiatedPercentageStageOne, VarPercentageStageOne.get(), 'PercentageStageOne')
            CheckingGUI(InitiatedHotkeyStageOne, VarHotkeyStageOne.get(), 'HotkeyStageOne')
            CheckingGUI(InitiatedPercentageStageTwo, VarPercentageStageTwo.get(), 'PercentageStageTwo')
            CheckingGUI(InitiatedHotkeyStageTwo, VarHotkeyStageTwo.get(), 'HotkeyStageTwo')
            CheckingGUI(InitiatedPercentageStageThree, VarPercentageStageThree.get(), 'PercentageStageThree')
            CheckingGUI(InitiatedHotkeyStageThree, VarHotkeyStageThree.get(), 'HotkeyStageThree')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

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

        StageOne = self.AutoHeal.addCheck(VarCheckStageOne, [17, 55], InitiatedCheckStageOne, "Enable Stage One")
        StageTwo = self.AutoHeal.addCheck(VarCheckStageTwo, [17, 105], InitiatedCheckStageTwo, "Enable Stage Two")
        StageThree = self.AutoHeal.addCheck(VarCheckStageThree, [17, 155], InitiatedCheckStageThree, "Enable Stage Three")
        CheckStats = self.AutoHeal.addCheck(VarCheckCureStats, [95, 192], InitiatedCheckCureStats, "Enable Cure Stats")

        Paralyze = self.AutoHeal.addCheck(VarCheckParalyze, [40, 226], InitiatedCheckParalyze, '', ParalyzeImage)
        Poison = self.AutoHeal.addCheck(VarCheckPoison, [80, 226], InitiatedCheckPoison, '', PoisonImage)
        Fire = self.AutoHeal.addCheck(VarCheckFire, [120, 226], InitiatedCheckFire, '', FireImage)
        Electrify = self.AutoHeal.addCheck(VarCheckElectrify, [160, 226], InitiatedCheckElectrify, '', ElectrifyImage)
        Mort = self.AutoHeal.addCheck(VarCheckMort, [200, 226], InitiatedCheckMort, '', MortImage)
        Blood = self.AutoHeal.addCheck(VarCheckBlood, [240, 226], InitiatedCheckBlood, '', BloodImage)

        PercentageStageOne = self.AutoHeal.addOption(VarPercentageStageOne, percentage, [148, 54])
        HotkeyStageOne = self.AutoHeal.addOption(VarHotkeyStageOne, self.SendToClient.Hotkeys, [223, 54])

        PercentageStageTwo = self.AutoHeal.addOption(VarPercentageStageTwo, percentage, [148, 104])
        HotkeyStageTwo = self.AutoHeal.addOption(VarHotkeyStageTwo, self.SendToClient.Hotkeys, [223, 104])

        PercentageStageThree = self.AutoHeal.addOption(VarPercentageStageThree, percentage, [148, 154])
        HotkeyStageThree = self.AutoHeal.addOption(VarHotkeyStageThree, self.SendToClient.Hotkeys, [223, 154])

        def CheckingButtons():
            if EnabledAutoHeal:
                CheckStats.configure(state='disabled')
                StageThree.configure(state='disabled')
                StageTwo.configure(state='disabled')
                StageOne.configure(state='disabled')
                LabelHotkey.configure(state='disabled')
                LabelPercentage.configure(state='disabled')
                PercentageStageOne.configure(state='disabled')
                HotkeyStageOne.configure(state='disabled')
                PercentageStageTwo.configure(state='disabled')
                HotkeyStageTwo.configure(state='disabled')
                PercentageStageThree.configure(state='disabled')
                HotkeyStageThree.configure(state='disabled')
                Paralyze.configure(state='disabled')
                Poison.configure(state='disabled')
                Fire.configure(state='disabled')
                Electrify.configure(state='disabled')
                Mort.configure(state='disabled')
                Blood.configure(state='disabled')
                CheckPrint.configure(state='disabled')
                CheckBuff.configure(state='disabled')
            else:
                CheckStats.configure(state='normal')
                StageThree.configure(state='normal')
                StageTwo.configure(state='normal')
                StageOne.configure(state='normal')
                LabelHotkey.configure(state='normal')
                LabelPercentage.configure(state='normal')
                PercentageStageOne.configure(state='normal')
                HotkeyStageOne.configure(state='normal')
                PercentageStageTwo.configure(state='normal')
                HotkeyStageTwo.configure(state='normal')
                PercentageStageThree.configure(state='normal')
                HotkeyStageThree.configure(state='normal')
                CheckPrint.configure(state='normal')
                CheckBuff.configure(state='normal')
                if not VarCheckCureStats.get():
                    Paralyze.configure(state='disabled')
                    Poison.configure(state='disabled')
                    Fire.configure(state='disabled')
                    Electrify.configure(state='disabled')
                    Mort.configure(state='disabled')
                    Blood.configure(state='disabled')
                elif VarCheckCureStats.get():
                    Paralyze.configure(state='normal')
                    Poison.configure(state='normal')
                    Fire.configure(state='normal')
                    Electrify.configure(state='normal')
                    Mort.configure(state='normal')
                    Blood.configure(state='normal')

        def ConstantVerify():
            if not EnabledAutoHeal:
                if not VarCheckCureStats.get():
                    Paralyze.configure(state='disabled')
                    Poison.configure(state='disabled')
                    Fire.configure(state='disabled')
                    Electrify.configure(state='disabled')
                    Mort.configure(state='disabled')
                    Blood.configure(state='disabled')
                elif VarCheckCureStats.get():
                    Paralyze.configure(state='normal')
                    Poison.configure(state='normal')
                    Fire.configure(state='normal')
                    Electrify.configure(state='normal')
                    Mort.configure(state='normal')
                    Blood.configure(state='normal')

            self.AutoHeal.After(30, ConstantVerify)

        CheckingButtons()

        ConstantVerify()

        self.AutoHeal.Protocol(Destroy)
        self.AutoHeal.loop()

