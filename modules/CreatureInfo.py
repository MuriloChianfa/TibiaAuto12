from engine.GUI import *

EnabledCreatureInfo = False


class CreatureInfo:
    def __init__(self, root):
        self.CreatureInfo = GUI('CreatureInfo', 'Module: Creature Info')
        self.CreatureInfo.DefaultWindow('DefaultWindow')

        def SetCreatureInfo():
            global EnabledCreatureInfo
            if not EnabledCreatureInfo:
                EnabledCreatureInfo = True
                ButtonEnabled.configure(text='CreatureInfo: ON')
                ScanCreatureInfo()
            else:
                EnabledCreatureInfo = False
                ButtonEnabled.configure(text='CreatureInfo: OFF')

        def ScanCreatureInfo():
            if EnabledCreatureInfo:
                print("Try Lock CreatureInfo")
                print("Try This")

            root.after(300, ScanCreatureInfo)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.CreatureInfo.addButton('Ok', self.CreatureInfo.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledCreatureInfo
        if not EnabledCreatureInfo:
            ButtonEnabled = self.CreatureInfo.addButton('CreatureInfo: OFF', SetCreatureInfo, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.CreatureInfo.addButton('CreatureInfo: ON', SetCreatureInfo, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.CreatureInfo.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.CreatureInfo.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.CreatureInfo.loop()

