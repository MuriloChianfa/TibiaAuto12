import json
import time

from Engine.GUI import *

EnabledCaveBot = False


class CaveBot:
    def __init__(self, root):
        self.CaveBot = GUI('CaveBot', 'Module: Cave Bot')
        self.CaveBot.DefaultWindow('DefaultWindow')

        def SetCaveBot():
            global EnabledCaveBot
            if not EnabledCaveBot:
                EnabledCaveBot = True
                ButtonEnabled.configure(text='CaveBot: ON')
                ScanCaveBot()
            else:
                EnabledCaveBot = False
                ButtonEnabled.configure(text='CaveBot: OFF')

        with open('CaveBot/Scripts/ratThais.json', 'r') as rJson:
            data = json.load(rJson)
            print(len(data))
        print(data)

        def ScanCaveBot():
            if EnabledCaveBot:
                global monster
                for i in range(len(data)):
                    CaveBot().cave_bot(data, i, map_positions, battle_location, monster, SQMs)
                    time.sleep(1)

            if EnabledCaveBot:
                root.after(300, ScanCaveBot)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.CaveBot.addButton('Ok', self.CaveBot.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledCaveBot
        if not EnabledCaveBot:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: OFF', SetCaveBot, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: ON', SetCaveBot, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.CaveBot.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.CaveBot.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.CaveBot.loop()

