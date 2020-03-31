from Engine.GUI import *

EnabledHealerFriend = False


class HealerFriend:
    def __init__(self, root):
        self.HealerFriend = GUI('HealerFriend', 'Module: Healer Friend')
        self.HealerFriend.DefaultWindow('DefaultWindow')

        def SetHealerFriend():
            global EnabledHealerFriend
            if not EnabledHealerFriend:
                EnabledHealerFriend = True
                ButtonEnabled.configure(text='HealerFriend: ON')
                ScanHealerFriend()
            else:
                EnabledHealerFriend = False
                ButtonEnabled.configure(text='HealerFriend: OFF')

        def ScanHealerFriend():
            if EnabledHealerFriend:
                print("Try Lock HealerFriend")
                print("Try This")

            root.after(300, ScanHealerFriend)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.HealerFriend.addButton('Ok', self.HealerFriend.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledHealerFriend
        if not EnabledHealerFriend:
            ButtonEnabled = self.HealerFriend.addButton('HealerFriend: OFF', SetHealerFriend, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.HealerFriend.addButton('HealerFriend: ON', SetHealerFriend, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.HealerFriend.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.HealerFriend.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.HealerFriend.loop()

