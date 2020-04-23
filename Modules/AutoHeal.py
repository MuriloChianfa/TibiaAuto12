import threading

from Engine.GUI import *
from Engine.ScanStages import ScanStages
from Conf.Hotkeys import Hotkeys, PressHotkey

EnabledAutoHeal = False
life = 0

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('DefaultWindow')

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
                ButtonEnabled.configure(text='AutoHealing: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def scanning_auto_life():
            while EnabledAutoHeal:
                global life
                life = ScanStages('Life').ScanStages(HealthLocation, lifeColor, lifeColorFull)

                if life is None:
                    life = 0

                if VarCheckStageThree.get():
                    stage_three = VarPercentageStageThree.get()
                    if stage_three > life or stage_three == life:
                        PressHotkey(VarHotkeyStageThree.get())
                        print("Pressed ", VarHotkeyStageThree.get())
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            PressHotkey(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                PressHotkey(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            PressHotkey(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                elif VarCheckStageTwo.get():
                    stage_two = VarPercentageStageTwo.get()
                    if stage_two > life or stage_two == life:
                        PressHotkey(VarHotkeyStageTwo.get())
                        print("Pressed ", VarHotkeyStageTwo.get())
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            PressHotkey(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                PressHotkey(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            PressHotkey(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                elif VarCheckStageOne.get():
                    stage_one = VarPercentageStageOne.get()
                    if stage_one > life or stage_one == life:
                        PressHotkey(VarHotkeyStageOne.get())
                        print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            PressHotkey(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                        elif VarCheckStageThree.get():
                            stage_three = VarPercentageStageThree.get()
                            if stage_three > life or stage_three == life:
                                PressHotkey(VarHotkeyStageThree.get())
                                print("Pressed ", VarHotkeyStageThree.get())
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            PressHotkey(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                else:
                    print("Module Not Configured")

            # if EnabledAutoHeal:
                # root.after(200, scanning_auto_life)

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

        self.AutoHeal.addButton('Ok', self.AutoHeal.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        ''' button enable healing '''

        global EnabledAutoHeal
        if not EnabledAutoHeal:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: OFF', SetAutoHeal, [328, 29, 12, 469],
                                                   [127, 17, 8], [103, 13, 5])
        else:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: ON', SetAutoHeal, [328, 29, 12, 469],
                                                   [127, 17, 8], [103, 13, 5])
    
        self.AutoHeal.addLabel('Healing', [120, 98, 51], [32, 3])
        LabelPercentage = self.AutoHeal.addLabel('% Percentage', [130, 16, 6], [153, 54])
        LabelHotkey = self.AutoHeal.addLabel('HotKey', [130, 16, 6], [259, 54])
        
        self.AutoHeal.addCheck(VarCheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        self.AutoHeal.addCheck(VarCheckBuff, [10, 440], [120, 98, 51], 0, "Don't Buff")
        StageOne = self.AutoHeal.addCheck(VarCheckStageOne, [32, 94], [130, 16, 6], 0, "Enable Stage One")
        StageTwo = self.AutoHeal.addCheck(VarCheckStageTwo, [32, 144], [130, 16, 6], 0, "Enable Stage Two")
        StageThree = self.AutoHeal.addCheck(VarCheckStageThree, [32, 194], [130, 16, 6], 0, "Enable Stage Three")
        CheckStats = self.AutoHeal.addCheck(VarCheckCureStats, [105, 334], [130, 16, 6], 0, "Enable Cure Stats")

        Paralyze = self.AutoHeal.addCheck(VarCheckParalyze, [52, 364], [130, 16, 6], 0, '', ParalyzeImage)
        Poison = self.AutoHeal.addCheck(VarCheckPoison, [92, 364], [130, 16, 6], 0, '', PoisonImage)
        Fire = self.AutoHeal.addCheck(VarCheckFire, [132, 364], [130, 16, 6], 0, '', FireImage)
        Electrify = self.AutoHeal.addCheck(VarCheckElectrify, [172, 364], [130, 16, 6], 0, '', ElectrifyImage)
        Mort = self.AutoHeal.addCheck(VarCheckMort, [212, 364], [130, 16, 6], 0, '', MortImage)
        Blood = self.AutoHeal.addCheck(VarCheckBlood, [252, 364], [130, 16, 6], 0, '', BloodImage)

        PercentageStageOne = self.AutoHeal.addOption(VarPercentageStageOne, percentage, [165, 90])
        HotkeyStageOne = self.AutoHeal.addOption(VarHotkeyStageOne, Hotkeys, [250, 90])

        PercentageStageTwo = self.AutoHeal.addOption(VarPercentageStageTwo, percentage, [165, 140])
        HotkeyStageTwo = self.AutoHeal.addOption(VarHotkeyStageTwo, Hotkeys, [250, 140])

        PercentageStageThree = self.AutoHeal.addOption(VarPercentageStageThree, percentage, [165, 190])
        HotkeyStageThree = self.AutoHeal.addOption(VarHotkeyStageThree, Hotkeys, [250, 190])

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

