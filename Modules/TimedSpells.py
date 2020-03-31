from Engine.GUI import *

EnabledTimedSpells = False


class TimedSpells:
    def __init__(self, root):
        self.TimedSpells = GUI('TimedSpells', 'Module: Timed Spells')
        self.TimedSpells.DefaultWindow('DefaultWindow')

        def SetTimedSpells():
            global EnabledTimedSpells
            if not EnabledTimedSpells:
                EnabledTimedSpells = True
                ButtonEnabled.configure(text='TimedSpells: ON')
                ScanTimedSpells()
            else:
                EnabledTimedSpells = False
                ButtonEnabled.configure(text='TimedSpells: OFF')

        def ScanTimedSpells():
            if EnabledTimedSpells:
                print("Try Lock TimedSpells")
                print("Try This")

            root.after(300, ScanTimedSpells)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.TimedSpells.addButton('Ok', self.TimedSpells.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledTimedSpells
        if not EnabledTimedSpells:
            ButtonEnabled = self.TimedSpells.addButton('TimedSpells: OFF', SetTimedSpells, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.TimedSpells.addButton('TimedSpells: ON', SetTimedSpells, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.TimedSpells.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.TimedSpells.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.TimedSpells.loop()

