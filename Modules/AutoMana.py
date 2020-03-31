from Engine.GUI import *
from Engine.ScanStages import ScanStages

EnabledAutoMana = False

manaColorFull = [45, 45, 105]

manaColor = [83, 80, 218]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoMana:
    def __init__(self, root, ManaLocation):
        self.AutoMana = GUI('AutoMana', 'Module: Auto Mana')
        self.AutoMana.DefaultWindow('DefaultWindow')

        def SetAutoMana():
            global EnabledAutoMana
            if not EnabledAutoMana:
                EnabledAutoMana = True
                ButtonEnabled.configure(text='AutoMana: ON')
                print("AutoMana: ON")
                ScanAutoMana()
            else:
                EnabledAutoMana = False
                print("AutoMana: OFF")
                ButtonEnabled.configure(text='AutoMana: OFF')

        def ScanAutoMana():
            mana = ScanStages('Mana').ScanStages(ManaLocation, manaColor, manaColorFull)

            if VarCheckStageTwo.get():
                stage_two = VarPercentageStageTwo.get()
                if stage_two > mana or stage_two == mana:
                    pyautogui.press(VarHotkeyStageTwo.get())
                    print("Pressed ", VarHotkeyStageTwo.get())
            elif VarCheckStageOne.get():
                stage_one = VarPercentageStageOne.get()
                if stage_one > mana or stage_one == mana:
                    pyautogui.press(VarHotkeyStageOne.get())
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
        self.AutoMana.addLabel('% Percentage', [130, 16, 6], [153, 54])
        self.AutoMana.addLabel('HotKey', [130, 16, 6], [259, 54])

        CheckPrint = self.AutoMana.addCheck(VarCheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        CheckBuff = self.AutoMana.addCheck(VarCheckBuff, [10, 440], [120, 98, 51], 0, "Don't Buff")
        StageOne = self.AutoMana.addCheck(VarCheckStageOne, [32, 94], [130, 16, 6], 0, "Enable Stage One")
        StageTwo = self.AutoMana.addCheck(VarCheckStageTwo, [32, 144], [130, 16, 6], 0, "Enable Stage Two")

        PercentageStageOne = self.AutoMana.addOption(VarPercentageStageOne, percentage, [165, 90])
        HotkeyStageOne = self.AutoMana.addOption(VarHotkeyStageOne, hotkeys, [250, 90])

        PercentageStageTwo = self.AutoMana.addOption(VarPercentageStageTwo, percentage, [165, 140])
        HotkeyStageTwo = self.AutoMana.addOption(VarHotkeyStageTwo, hotkeys, [250, 140])

        self.AutoMana.loop()

