import time
import threading

from Engine.GUI import *
from Engine.ScanStages import ScanStages
from Conf.Hotkeys import Hotkey


EnabledAutoHeal = False
life = 0

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation, MOUSE_OPTION, HOOK_OPTION):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('AutoHeal2', [306, 372], [1.2, 2.29])
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
                        time.sleep(0.2)
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            self.SendToClient.Press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                            time.sleep(0.2)
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                self.SendToClient.Press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                                time.sleep(0.2)
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            self.SendToClient.Press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                            time.sleep(0.2)
                elif VarCheckStageTwo.get():
                    stage_two = VarPercentageStageTwo.get()
                    if stage_two > life or stage_two == life:
                        self.SendToClient.Press(VarHotkeyStageTwo.get())
                        print("Pressed ", VarHotkeyStageTwo.get())
                        time.sleep(0.2)
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            self.SendToClient.Press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                            time.sleep(0.2)
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                self.SendToClient.Press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                                time.sleep(0.2)
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            self.SendToClient.Press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                            time.sleep(0.2)
                elif VarCheckStageOne.get():
                    stage_one = VarPercentageStageOne.get()
                    if stage_one > life or stage_one == life:
                        self.SendToClient.Press(VarHotkeyStageOne.get())
                        print("Pressed ", VarHotkeyStageOne.get())
                        time.sleep(0.2)
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            self.SendToClient.Press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                            time.sleep(0.2)
                        elif VarCheckStageThree.get():
                            stage_three = VarPercentageStageThree.get()
                            if stage_three > life or stage_three == life:
                                self.SendToClient.Press(VarHotkeyStageThree.get())
                                print("Pressed ", VarHotkeyStageThree.get())
                                time.sleep(0.2)
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            self.SendToClient.Press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                            time.sleep(0.2)
                else:
                    print("Module Not Configured")
                    time.sleep(1)

        VarCheckPrint = tk.BooleanVar()
        VarCheckBuff = tk.BooleanVar()
        VarCheckStageOne = tk.BooleanVar()
        VarCheckStageTwo = tk.BooleanVar()
        VarCheckStageThree = tk.BooleanVar()
        VarCheckCureStats = tk.BooleanVar()
        VarCheckParalyze = tk.BooleanVar()
        VarCheckPoison = tk.BooleanVar()
        VarCheckFire = tk.BooleanVar()
        VarCheckElectrify = tk.BooleanVar()
        VarCheckMort = tk.BooleanVar()
        VarCheckBlood = tk.BooleanVar()
        VarPercentageStageOne = tk.IntVar()
        VarPercentageStageOne.set(90)
        VarHotkeyStageOne = tk.StringVar()
        VarHotkeyStageOne.set("F1")
        VarPercentageStageTwo = tk.IntVar()
        VarPercentageStageTwo.set(75)
        VarHotkeyStageTwo = tk.StringVar()
        VarHotkeyStageTwo.set("F2")
        VarPercentageStageThree = tk.IntVar()
        VarPercentageStageThree.set(35)
        VarHotkeyStageThree = tk.StringVar()
        VarHotkeyStageThree.set("F12")
        ParalyzeImage = ImageTk.PhotoImage(Image.open('images/Stats/paralyze.webp'))
        PoisonImage = ImageTk.PhotoImage(Image.open('images/Stats/poison.webp'))
        FireImage = ImageTk.PhotoImage(Image.open('images/Stats/fire.webp'))
        ElectrifyImage = ImageTk.PhotoImage(Image.open('images/Stats/electrify.webp'))
        MortImage = ImageTk.PhotoImage(Image.open('images/Stats/mort.webp'))
        BloodImage = ImageTk.PhotoImage(Image.open('images/Stats/blood.webp'))

        self.AutoHeal.addButton('Ok', self.AutoHeal.destroyWindow, [73, 21], [115, 340])

        ''' button enable healing '''

        global EnabledAutoHeal
        if not EnabledAutoHeal:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: OFF', SetAutoHeal, [287, 23], [11, 311])
        else:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: ON', SetAutoHeal, [287, 23], [11, 311])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        CheckPrint = self.AutoHeal.addCheck(VarCheckPrint, [11, 260], 0, "Print on Tibia's screen")
        CheckPrint.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))
        CheckBuff = self.AutoHeal.addCheck(VarCheckBuff, [11, 280], 0, "Don't Buff")
        CheckBuff.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114, 94, 48)))

        LabelPercentage = self.AutoHeal.addLabel('% Percentage', [145, 24])
        LabelHotkey = self.AutoHeal.addLabel('HotKey', [230, 24])

        StageOne = self.AutoHeal.addCheck(VarCheckStageOne, [17, 55], 0, "Enable Stage One")
        StageTwo = self.AutoHeal.addCheck(VarCheckStageTwo, [17, 105], 0, "Enable Stage Two")
        StageThree = self.AutoHeal.addCheck(VarCheckStageThree, [17, 155], 0, "Enable Stage Three")
        CheckStats = self.AutoHeal.addCheck(VarCheckCureStats, [95, 192], 0, "Enable Cure Stats")

        Paralyze = self.AutoHeal.addCheck(VarCheckParalyze, [40, 226], 0, '', ParalyzeImage)
        Poison = self.AutoHeal.addCheck(VarCheckPoison, [80, 226], 0, '', PoisonImage)
        Fire = self.AutoHeal.addCheck(VarCheckFire, [120, 226], 0, '', FireImage)
        Electrify = self.AutoHeal.addCheck(VarCheckElectrify, [160, 226], 0, '', ElectrifyImage)
        Mort = self.AutoHeal.addCheck(VarCheckMort, [200, 226], 0, '', MortImage)
        Blood = self.AutoHeal.addCheck(VarCheckBlood, [240, 226], 0, '', BloodImage)

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

            self.AutoHeal.After(1, ConstantVerify)

        CheckingButtons()

        ConstantVerify()

        self.AutoHeal.loop()

