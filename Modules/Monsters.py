from Engine.GUI import *

EnabledMonsters = False


class Monsters:
    def __init__(self, root):
        self.Monsters = GUI('Monsters', 'Module: Monsters')
        self.Monsters.DefaultWindow('DefaultWindow')

        def SetMonsters():
            global EnabledMonsters
            if not EnabledMonsters:
                EnabledMonsters = True
                ButtonEnabled.configure(text='Monsters: ON')
                ScanMonsters()
            else:
                EnabledMonsters = False
                ButtonEnabled.configure(text='Monsters: OFF')

        def ScanMonsters():
            if EnabledMonsters:
                print("Try Lock Monsters")
                print("Try This")

            root.after(300, ScanMonsters)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.Monsters.addButton('Ok', self.Monsters.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledMonsters
        if not EnabledMonsters:
            ButtonEnabled = self.Monsters.addButton('Monsters: OFF', SetMonsters, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.Monsters.addButton('Monsters: ON', SetMonsters, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.Monsters.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.Monsters.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.Monsters.loop()

