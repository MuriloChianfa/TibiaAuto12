from Engine.GUI import *
from Engine.AttackTarget import AttackTarget
from Engine.SetFollow import SetFollow

EnabledAutoAttack = False
target_number = 0


class AutoAttack:
    def __init__(self, root, SQMs, monster, BattlePosition):
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
                AttackTarget(monster, BattlePosition, SQMs, target_number)

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

