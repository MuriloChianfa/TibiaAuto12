import threading

from Engine.GUI import *
from Engine.ScanStages import ScanStages

EnabledAutoHeal = False

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('DefaultWindow')

        def SetAutoHeal():
            global EnabledAutoHeal
            if not EnabledAutoHeal:
                EnabledAutoHeal = True
                ButtonEnabled.configure(text='AutoHealing: ON')
                print("AutoHealing: ON")
                try:
                    ThreadCaveBot = threading.Thread(target=scanning_auto_life)
                    ThreadCaveBot.start()
                except:
                    print("Error: Unable To Start ThreadCaveBot!")
            else:
                EnabledAutoHeal = False
                print("AutoHealing: OFF")
                ButtonEnabled.configure(text='AutoHealing: OFF')

        def scanning_auto_life():
            while EnabledAutoHeal:
                life = ScanStages('Life').ScanStages(HealthLocation, lifeColor, lifeColorFull)

                if life is None:
                    life = 0

                if VarCheckStageThree.get():
                    stage_three = VarPercentageStageThree.get()
                    if stage_three > life or stage_three == life:
                        pyautogui.press(VarHotkeyStageThree.get())
                        print("Pressed ", VarHotkeyStageThree.get())
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            pyautogui.press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                pyautogui.press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            pyautogui.press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                elif VarCheckStageTwo.get():
                    stage_two = VarPercentageStageTwo.get()
                    if stage_two > life or stage_two == life:
                        pyautogui.press(VarHotkeyStageTwo.get())
                        print("Pressed ", VarHotkeyStageTwo.get())
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            pyautogui.press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                        elif VarCheckStageOne.get():
                            stage_one = VarPercentageStageOne.get()
                            if stage_one > life or stage_one == life:
                                pyautogui.press(VarHotkeyStageOne.get())
                                print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageOne.get():
                        stage_one = VarPercentageStageOne.get()
                        if stage_one > life or stage_one == life:
                            pyautogui.press(VarHotkeyStageOne.get())
                            print("Pressed ", VarHotkeyStageOne.get())
                elif VarCheckStageOne.get():
                    stage_one = VarPercentageStageOne.get()
                    if stage_one > life or stage_one == life:
                        pyautogui.press(VarHotkeyStageOne.get())
                        print("Pressed ", VarHotkeyStageOne.get())
                    elif VarCheckStageTwo.get():
                        stage_two = VarPercentageStageTwo.get()
                        if stage_two > life or stage_two == life:
                            pyautogui.press(VarHotkeyStageTwo.get())
                            print("Pressed ", VarHotkeyStageTwo.get())
                        elif VarCheckStageThree.get():
                            stage_three = VarPercentageStageThree.get()
                            if stage_three > life or stage_three == life:
                                pyautogui.press(VarHotkeyStageThree.get())
                                print("Pressed ", VarHotkeyStageThree.get())
                    elif VarCheckStageThree.get():
                        stage_three = VarPercentageStageThree.get()
                        if stage_three > life or stage_three == life:
                            pyautogui.press(VarHotkeyStageThree.get())
                            print("Pressed ", VarHotkeyStageThree.get())
                else:
                    print("Modulo Not Configured")

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
        VarHotkeyStageOne.set("f1")
        VarPercentageStageTwo = tk.IntVar()
        VarPercentageStageTwo.set(75)
        VarHotkeyStageTwo = tk.StringVar()
        VarHotkeyStageTwo.set("f2")
        VarPercentageStageThree = tk.IntVar()
        VarPercentageStageThree.set(35)
        VarHotkeyStageThree = tk.StringVar()
        VarHotkeyStageThree.set("f12")
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
                                                   [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: ON', SetAutoHeal, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])
    
        self.AutoHeal.addLabel('Healing', [120, 98, 51], [32, 3])
        self.AutoHeal.addLabel('% Percentage', [130, 16, 6], [153, 54])
        self.AutoHeal.addLabel('HotKey', [130, 16, 6], [259, 54])
        
        CheckPrint = self.AutoHeal.addCheck(VarCheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        CheckBuff = self.AutoHeal.addCheck(VarCheckBuff, [10, 440], [120, 98, 51], 0, "Don't Buff")
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
        HotkeyStageOne = self.AutoHeal.addOption(VarHotkeyStageOne, hotkeys, [250, 90])

        PercentageStageTwo = self.AutoHeal.addOption(VarPercentageStageTwo, percentage, [165, 140])
        HotkeyStageTwo = self.AutoHeal.addOption(VarHotkeyStageTwo, hotkeys, [250, 140])

        PercentageStageThree = self.AutoHeal.addOption(VarPercentageStageThree, percentage, [165, 190])
        HotkeyStageThree = self.AutoHeal.addOption(VarHotkeyStageThree, hotkeys, [250, 190])

        self.AutoHeal.loop()

