from Engine.GUI import *
from Engine.Defaults import *
from Engine.ScanStages import ScanStages


rgb = Defaults()
bool_life = False

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation):
        self.AutoHeal = GUI('AutoHeal', 'Module: Auto Heal')
        self.AutoHeal.DefaultWindow('DefaultWindow')

        def func_auto_life():
            global bool_life
            if not bool_life:
                bool_life = True
                ButtonEnabled.configure(text='AutoHealing: ON')
                print("AutoHealing: ON")
                scanning_auto_life()
            else:
                bool_life = False
                print("AutoHealing: OFF")
                ButtonEnabled.configure(text='AutoHealing: OFF')

        def scanning_auto_life():
            life = ScanStages('Life').ScanStages(HealthLocation, lifeColor, lifeColorFull)

            if VarCheckStageThree.get():
                stage_three = var_dropdown_stage_five.get()
                if int(stage_three) > life or int(stage_three) == life:
                    pyautogui.press(var_dropdown_stage_six.get())
                    print("Pressed ", var_dropdown_stage_six.get())
            elif VarCheckStageTwo.get() == "on":
                stage_two = var_dropdown_stage_three.get()
                if int(stage_two) > life or int(stage_two) == life:
                    pyautogui.press(var_dropdown_stage_four.get())
                    print("Pressed ", var_dropdown_stage_four.get())
            elif VarCheckStageOne.get() == "on":
                stage_one = var_dropdown_stage_one.get()
                if int(stage_one) > life or int(stage_one) == life:
                    pyautogui.press(var_dropdown_stage_two.get())
                    print("Pressed ", var_dropdown_stage_two.get())
            else:
                print("Modulo Not Configured")

            if bool_life:
                root.after(200, scanning_auto_life)

        VarCheckPrint = tk.IntVar()
        VarCheckBuff = tk.IntVar()
        VarCheckStageOne = tk.IntVar()
        VarCheckStageTwo = tk.IntVar()
        VarCheckStageThree = tk.IntVar()
        VarCheckCureStats = tk.IntVar()
        VarCheckParalyze = tk.IntVar()
        VarCheckPoison = tk.IntVar()
        VarCheckFire = tk.IntVar()
        VarCheckElectrify = tk.IntVar()
        VarCheckMort = tk.IntVar()
        VarCheckBlood = tk.IntVar()
        var_dropdown_stage_one = tk.StringVar()
        var_dropdown_stage_one.set(90)
        var_dropdown_stage_two = tk.StringVar()
        var_dropdown_stage_two.set("f1")
        var_dropdown_stage_three = tk.StringVar()
        var_dropdown_stage_three.set(75)
        var_dropdown_stage_four = tk.StringVar()
        var_dropdown_stage_four.set("f2")
        var_dropdown_stage_five = tk.StringVar()
        var_dropdown_stage_five.set(35)
        var_dropdown_stage_six = tk.StringVar()
        var_dropdown_stage_six.set("f12")
        ParalyzeImage = ImageTk.PhotoImage(Image.open('images/Stats/paralyze.webp'))
        PoisonImage = ImageTk.PhotoImage(Image.open('images/Stats/poison.webp'))
        FireImage = ImageTk.PhotoImage(Image.open('images/Stats/fire.webp'))
        ElectrifyImage = ImageTk.PhotoImage(Image.open('images/Stats/electrify.webp'))
        MortImage = ImageTk.PhotoImage(Image.open('images/Stats/mort.webp'))
        BloodImage = ImageTk.PhotoImage(Image.open('images/Stats/blood.webp'))

        self.AutoHeal.addButton('Ok', self.AutoHeal.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        ''' button enable healing '''

        global bool_life
        if not bool_life:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: OFF', func_auto_life, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoHeal.addButton('AutoHealing: ON', func_auto_life, [328, 29, 12, 469],
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

        Paralyze = self.AutoHeal.addCheck(VarCheckParalyze, [52, 364], [130, 16, 6], 0, ParalyzeImage)
        Poison = self.AutoHeal.addCheck(VarCheckPoison, [92, 364], [130, 16, 6], 0, PoisonImage)
        Fire = self.AutoHeal.addCheck(VarCheckFire, [132, 364], [130, 16, 6], 0, FireImage)
        Electrify = self.AutoHeal.addCheck(VarCheckElectrify, [172, 364], [130, 16, 6], 0, ElectrifyImage)
        Mort = self.AutoHeal.addCheck(VarCheckMort, [212, 364], [130, 16, 6], 0, MortImage)
        Blood = self.AutoHeal.addCheck(VarCheckBlood, [252, 364], [130, 16, 6], 0, BloodImage)

        dropdown_stage_one = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_one, *percentage)
        dropdown_stage_one["fg"] = 'white'
        dropdown_stage_one["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_one["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_one["width"] = 4
        dropdown_stage_one.place(x=165, y=90)

        dropdown_stage_two = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_two, *hotkeys)
        dropdown_stage_two["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_two["fg"] = 'white'
        dropdown_stage_two["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_two["width"] = 4
        dropdown_stage_two.place(x=250, y=90)

        dropdown_stage_three = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_three, *percentage)
        dropdown_stage_three["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_three["fg"] = 'white'
        dropdown_stage_three["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_three["width"] = 4
        dropdown_stage_three.place(x=165, y=140)

        dropdown_stage_four = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_four, *hotkeys)
        dropdown_stage_four["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_four["fg"] = 'white'
        dropdown_stage_four["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_four["width"] = 4
        dropdown_stage_four.place(x=250, y=140)

        dropdown_stage_five = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_five, *percentage)
        dropdown_stage_five["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_five["fg"] = 'white'
        dropdown_stage_five["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_five["width"] = 4
        dropdown_stage_five.place(x=165, y=190)

        dropdown_stage_six = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_six, *hotkeys)
        dropdown_stage_six["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_six["fg"] = 'white'
        dropdown_stage_six["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_six["width"] = 4
        dropdown_stage_six.place(x=250, y=190)

        self.AutoHeal.mainloop()
