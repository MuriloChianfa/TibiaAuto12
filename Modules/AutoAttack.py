from Engine.GUI import *
from Engine.GetTargetPosition import AutoAttack2

EnabledAutoAttack = False


class AutoAttack:
    def __init__(self, root, Target, SQMs, monster, BattlePosition):
        self.AutoAttack = GUI('AutoAttack', 'Module: Auto Attack')
        self.AutoAttack.DefaultWindow('DefaultWindow')

        def SetAutoAttack():
            global EnabledAutoAttack
            if not EnabledAutoAttack:
                EnabledAutoAttack = True
                ButtonEnabled.configure(text='AutoAttack: ON')
                ScanAutoAttack()
            else:
                EnabledAutoAttack = False
                ButtonEnabled.configure(text='AutoAttack: OFF')

        def ScanAutoAttack():
            if EnabledAutoAttack:
                AutoAttack2().auto_attack(monster, BattlePosition, SQMs, 0)

            if EnabledAutoAttack:
                root.after(300, ScanAutoAttack)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoAttack.addButton('Ok', self.AutoAttack.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoAttack
        if not EnabledAutoAttack:
            ButtonEnabled = self.AutoAttack.addButton('AutoAttack: OFF', SetAutoAttack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoAttack.addButton('AutoAttack: ON', SetAutoAttack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoAttack.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoAttack.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoAttack.loop()

