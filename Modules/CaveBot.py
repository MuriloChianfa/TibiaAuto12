import json
import time
import threading

from Engine.GUI import *
from Engine.EngineCaveBot import EngineCaveBot

EnabledCaveBot = False

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

Scripts = [
    "ratThais",
    "StonerefinerVenore"
]

DefaultScript = 'ratThais'

data = None


class CaveBot:
    def __init__(self, root, MapPositions, BattlePositions, SQMs):
        self.CaveBot = GUI('CaveBot', 'Module: Cave Bot')
        self.CaveBot.DefaultWindow('CaveBot', [830, 634], [1.2, 2.29])

        def SetCaveBot():
            global EnabledCaveBot
            if not EnabledCaveBot:
                EnabledCaveBot = True
                ButtonEnabled.configure(text='CaveBot: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                CheckingButtons()
                InitScan()
            else:
                EnabledCaveBot = False
                CheckingButtons()
                ButtonEnabled.configure(text='CaveBot: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def InitScan():
            with open('Scripts/' + Script.get() + '.json', 'r') as rJson:
                global data, monster
                data = json.load(rJson)
                print("The Script " + Script.get() + ".json Have a", len(data), "Marks")

                monster = monster2.get()
                try:
                    ThreadCaveBot = threading.Thread(target=ScanCaveBot)
                    ThreadCaveBot.start()
                except:
                    print("Error: Unable To Start ThreadCaveBot!")

        def ScanCaveBot():
            global data, monster
            while EnabledCaveBot:
                for i in range(len(data)):
                    EngineCaveBot(data, i, MapPositions, BattlePositions, monster, SQMs)
                    time.sleep(1)

            # if EnabledCaveBot:
                # root.after(300, ScanCaveBot)

        global monster
        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        AttackOne = tk.BooleanVar()
        monster2 = tk.StringVar()
        monster2.set(monster)
        PriorityOne = tk.IntVar()
        PriorityOne.set(1)

        Script = tk.StringVar()
        Script.set(DefaultScript)

        self.CaveBot.addButton('Ok', self.CaveBot.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledCaveBot
        if not EnabledCaveBot:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: OFF', SetCaveBot, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: ON', SetCaveBot, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])

        self.CaveBot.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")
        self.CaveBot.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        LabelScript = self.CaveBot.addLabel('Script To Load', [127, 17, 8], [32, 70])
        OptionScript = self.CaveBot.addOption(Script, Scripts, [155, 70], 18)

        CheckAttackOne = self.CaveBot.addCheck(AttackOne, [32, 114], [130, 16, 6], 1, 'Monster One')
        OptionMonstersOne = self.CaveBot.addOption(monster2, monsters, [155, 110])
        PriorityMonstersOne = self.CaveBot.addOption(PriorityOne, priority, [240, 110])

        def CheckingButtons():
            if EnabledCaveBot:
                LabelScript.configure(state='disabled')
                OptionScript.configure(state='disabled')
                CheckAttackOne.configure(state='disabled')
                OptionMonstersOne.configure(state='disabled')
                PriorityMonstersOne.configure(state='disabled')
            else:
                LabelScript.configure(state='normal')
                OptionScript.configure(state='normal')
                CheckAttackOne.configure(state='normal')
                OptionMonstersOne.configure(state='normal')
                PriorityMonstersOne.configure(state='normal')

        CheckingButtons()

        self.CaveBot.loop()
