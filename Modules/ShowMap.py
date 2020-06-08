from Core.GUI import *

from Engine.AttackTarget import AttackTarget
from Engine.SetFollow import SetFollow

EnabledAutoAttack = False
TargetNumber = 0
priority = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monsters = [
    "Rat",
    "CaveRat",
    "Orc",
    "OrcWarrior",
    "OrcSpearman",
    "Cyclops",
    "Rotworm",
    "AnyCorym",
    "CorymCharlatan",
    "CorymSkirmisher",
    "CorymVanguard",
    "Stonerefiner"
]

monster = 'Rat'


class ShowMap:
    def __init__(self, root, SQMs, BattlePosition):
        self.ShowMap = GUI('AutoAttack', 'Module: Auto Attack')
        self.ShowMap.DefaultWindow('DefaultWindow')

        def SetAutoAttack():
            global EnabledAutoAttack
            if not EnabledAutoAttack:
                EnabledAutoAttack = True
                ButtonEnabled.configure(text='AutoAttack: ON')
                combine_funcs(ScanAutoAttack(), ScanFollowMode())
            else:
                EnabledAutoAttack = False
                ButtonEnabled.configure(text='AutoAttack: OFF')

        def ScanAutoAttack():
            if EnabledAutoAttack:
                global TargetNumber
                monster = monster2.get()
                TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber)

            if EnabledAutoAttack:
                root.after(300, ScanAutoAttack)

        def ScanFollowMode():
            if EnabledAutoAttack:
                follow_x_pos, follow_y_pos = SetFollow()

                if follow_x_pos != 0 and follow_y_pos != 0:
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(follow_x_pos, follow_y_pos)
                    pyautogui.moveTo(past_mouse_position)

            if EnabledAutoAttack:
                root.after(3000, ScanFollowMode)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        AttackOne = tk.BooleanVar()
        monster2 = tk.StringVar()
        monster2.set(monster)
        PriorityOne = tk.IntVar()
        PriorityOne.set(1)

        self.ShowMap.addButton('Ok', self.ShowMap.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoAttack
        if not EnabledAutoAttack:
            ButtonEnabled = self.ShowMap.addButton('AutoAttack: OFF', SetAutoAttack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.ShowMap.addButton('AutoAttack: ON', SetAutoAttack, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.ShowMap.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.ShowMap.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        CheckAttackOne = self.ShowMap.addCheck(AttackOne, [32, 74], [130, 16, 6], 1, 'Monster One')

        OptionMonstersOne = self.ShowMap.addOption(monster2, monsters, [155, 70])

        PriorityMonstersOne = self.ShowMap.addOption(PriorityOne, priority, [240, 70])

        self.ShowMap.loop()

