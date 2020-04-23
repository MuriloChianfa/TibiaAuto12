from Engine.GUI import *
from Engine.ScanStages import ScanStages
from Conf.Hotkeys import Hotkeys, PressHotkey

EnabledAutoMana = False

manaColorFull = [45, 45, 105]

manaColor = [83, 80, 218]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoMana:
    def __init__(self, root, ManaLocation):
        self.AutoMana = GUI('AutoMana', 'Module: Auto Mana')
        self.AutoMana.DefaultWindow('DefaultWindow')

        def SetAutoMana():
            global EnabledAutoMana
            if not EnabledAutoMana:
                EnabledAutoMana = True
                ButtonEnabled.configure(text='AutoMana: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoMana: ON")
                CheckingButtons()
                ScanAutoMana()
            else:
                EnabledAutoMana = False
                print("AutoMana: OFF")
                CheckingButtons()
                ButtonEnabled.configure(text='AutoMana: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def ScanAutoMana():
            mana = ScanStages('Mana').ScanStages(ManaLocation, manaColor, manaColorFull)

            if mana is None:
                mana = 0

            if VarCheckStageTwo.get():
                stage_two = VarPercentageStageTwo.get()
                if stage_two > mana or stage_two == mana:
                    PressHotkey(VarHotkeyStageTwo.get())
                    print("Pressed ", VarHotkeyStageTwo.get())
            elif VarCheckStageOne.get():
                stage_one = VarPercentageStageOne.get()
                if stage_one > mana or stage_one == mana:
                    PressHotkey(VarHotkeyStageOne.get())
                    print("Pressed ", VarHotkeyStageOne.get())
            else:
                print("Modulo Not Configured")

            if EnabledAutoMana:
                root.after(200, ScanAutoMana)

        VarCheckPrint = tk.BooleanVar()
        VarCheckBuff = tk.BooleanVar()
        VarCheckStageOne = tk.BooleanVar()
        VarCheckStageTwo = tk.BooleanVar()
        VarPercentageStageOne = tk.IntVar()
        VarPercentageStageOne.set(60)
        VarHotkeyStageOne = tk.StringVar()
        VarHotkeyStageOne.set("f3")
        VarPercentageStageTwo = tk.IntVar()
        VarPercentageStageTwo.set(45)
        VarHotkeyStageTwo = tk.StringVar()
        VarHotkeyStageTwo.set("f4")

        self.AutoMana.addButton('Ok', self.AutoMana.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        ''' button enable healing '''

        global EnabledAutoMana
        if not EnabledAutoMana:
            ButtonEnabled = self.AutoMana.addButton('AutoMana: OFF', SetAutoMana, [328, 29, 12, 469],
                                                    [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoMana.addButton('AutoMana: ON', SetAutoMana, [328, 29, 12, 469],
                                                    [127, 17, 8], [123, 13, 5])

        self.AutoMana.addLabel('Mana', [120, 98, 51], [32, 3])
        LabelPercentage = self.AutoMana.addLabel('% Percentage', [130, 16, 6], [153, 54])
        LabelHotkey = self.AutoMana.addLabel('HotKey', [130, 16, 6], [259, 54])

        self.AutoMana.addCheck(VarCheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        self.AutoMana.addCheck(VarCheckBuff, [10, 440], [120, 98, 51], 0, "Don't Buff")

        StageOne = self.AutoMana.addCheck(VarCheckStageOne, [32, 94], [130, 16, 6], 0, "Enable Stage One")
        StageTwo = self.AutoMana.addCheck(VarCheckStageTwo, [32, 144], [130, 16, 6], 0, "Enable Stage Two")

        PercentageStageOne = self.AutoMana.addOption(VarPercentageStageOne, percentage, [165, 90])
        HotkeyStageOne = self.AutoMana.addOption(VarHotkeyStageOne, Hotkeys, [250, 90])

        PercentageStageTwo = self.AutoMana.addOption(VarPercentageStageTwo, percentage, [165, 140])
        HotkeyStageTwo = self.AutoMana.addOption(VarHotkeyStageTwo, Hotkeys, [250, 140])

        def CheckingButtons():
            if EnabledAutoMana:
                StageOne.configure(state='disabled')
                StageTwo.configure(state='disabled')
                PercentageStageOne.configure(state='disabled')
                HotkeyStageOne.configure(state='disabled')
                PercentageStageTwo.configure(state='disabled')
                HotkeyStageTwo.configure(state='disabled')
                LabelPercentage.configure(state='disabled')
                LabelHotkey.configure(state='disabled')
            else:
                StageOne.configure(state='normal')
                StageTwo.configure(state='normal')
                PercentageStageOne.configure(state='normal')
                HotkeyStageOne.configure(state='normal')
                PercentageStageTwo.configure(state='normal')
                HotkeyStageTwo.configure(state='normal')
                LabelPercentage.configure(state='normal')
                LabelHotkey.configure(state='normal')

        CheckingButtons()

        self.AutoMana.loop()

