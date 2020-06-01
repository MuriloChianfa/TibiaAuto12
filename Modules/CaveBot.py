import json
import time
import threading

from Engine.GUI import *
from Engine.EngineCaveBot import EngineCaveBot
from Engine.SetGUI import SetGUI

GUIChanges = []

EnabledCaveBot = False

Hotkeys = [
    'Page Up'
]
priority = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
AttackModes = [
    'Full Attack',
    'Balance',
    'Full Defence'
]
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

DefaultScript = 'StonerefinerVenore'
data = None


class CaveBot:
    def __init__(self, root, MapPositions, BattlePositions, SQMs, MOUSE_OPTION, HOOK_OPTION):
        self.CaveBot = GUI('CaveBot', 'Module: Cave Bot')
        self.CaveBot.DefaultWindow('CaveBot', [830, 634], [1.2, 2.29])
        self.Setter = SetGUI("CaveBotLoader")

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
            global data, monster

            with open('Scripts/' + Script.get() + '.json', 'r') as rJson:
                data = json.load(rJson)
            print("The Script " + Script.get() + ".json Have a", len(data), "Marks")

            monster = SelectedMonster.get()
            try:
                ThreadCaveBot = threading.Thread(target=ScanCaveBot)
                ThreadCaveBot.start()
            except:
                print("Error: Unable To Start ThreadCaveBot!")

        def ScanCaveBot():
            global data, monster
            while EnabledCaveBot:
                for i in range(len(data)):
                    EngineCaveBot(data, i, MapPositions, BattlePositions, monster, SQMs, MOUSE_OPTION, HOOK_OPTION, Script.get())
                    time.sleep(1)

        def CheckClick():
            Checking()

        CheckDebugging = tk.BooleanVar()
        InitiatedDebugging = self.Setter.GetBoolVar("Debugging")
        CheckDebugging.set(InitiatedDebugging)

        CheckHotkeyPause = tk.BooleanVar()
        InitiatedHotkeyPause = self.Setter.GetBoolVar("HotkeyPause")
        CheckHotkeyPause.set(InitiatedHotkeyPause)

        HotkeyToPause = tk.StringVar()
        InitiatedHotkeyToPause = self.Setter.GetVar("HotkeyToPause")
        HotkeyToPause.set(InitiatedHotkeyToPause)

        Script = tk.StringVar()
        Script.set(DefaultScript)

        BackImage = 'images/Fundo.png'
        Back = self.CaveBot.openImage(BackImage, [210, 60])
        Back2 = self.CaveBot.openImage(BackImage, [210, 100])

        global EnabledCaveBot
        if not EnabledCaveBot:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: OFF', SetCaveBot, [810, 26], [10, 570])
        else:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: ON', SetCaveBot, [810, 26], [10, 570])

        CheckboxDebugging = self.CaveBot.addCheck(CheckDebugging, [434, 484], InitiatedDebugging, "Enable Cavebot Debugging")

        CheckboxHotkeyPause = self.CaveBot.addCheck(CheckHotkeyPause, [434, 526], InitiatedHotkeyPause,
                                                    'Enable Hotkey To Break a  Cavebot')
        CheckboxHotkeyPause.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                      selectcolor=rgb((114, 94, 48)))

        ButtonHotkeyPause = self.CaveBot.addOption(HotkeyToPause, Hotkeys, [644, 526], 8)

        # region Functions Walker

        def ValidateRadius(*args):
            s = Radius.get()
            if len(s) > 2:
                if not s[-1].isdigit():
                    Radius.set(s[:-1])
                else:
                    Radius.set(s[:2])

        def ValidateDelay(*args):
            s = Delay.get()
            if len(s) > 1:
                if not s[-1].isdigit():
                    Delay.set(s[:-1])
                else:
                    Delay.set(s[:1])

        def ValidateWaypoint_X(*args):
            s = Waypoint_X.get()
            if len(s) > 5:
                if not s[-1].isdigit():
                    Waypoint_X.set(s[:-1])
                else:
                    Waypoint_X.set(s[:5])

        def ValidateWaypoint_Y(*args):
            s = Waypoint_Y.get()
            if len(s) > 5:
                if not s[-1].isdigit():
                    Waypoint_Y.set(s[:-1])
                else:
                    Waypoint_Y.set(s[:5])

        def ValidateWaypoint_Z(*args):
            s = Waypoint_Z.get()
            if len(s) > 2:
                if not s[-1].isdigit():
                    Waypoint_Z.set(s[:-1])
                else:
                    Waypoint_Z.set(s[:2])

        def ValidateStand(*args):
            s = Stand.get()
            if len(s) > 1:
                if not s[-1].isdigit():
                    Stand.set(s[:-1])
                else:
                    Stand.set(s[:1])

        def SetResearchMap():
            if not ResearchMap.get():
                ResearchMap.set(True)
                ButtonResearchMap.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
            else:
                ResearchMap.set(False)
                ButtonResearchMap.configure(relief=RAISED, bg=rgb((127, 17, 8)))

        def RemoveWalker():
            print('Clicked on remove wlaker')

        def AddWalker():
            print('Clicked on add walker')

        def CheckMarkClick():
            print('Check Mark Click')

        # endregion

        # region Functions MonstersAttacking

        def AddMonsterAttack():
            print('AddMonsterAttack')

        def RemoveMonsterAttack():
            print('RemoveMonsterAttack')

        def AddMonsterIgnore():
            print('AddMonsterIgnore')

        def RemoveMonsterIgnore():
            print('RemoveMonsterIgnore')

        def UpMonsterAttack():
            print('UpMonsterAttack')

        def DownMonsterAttack():
            print('DownMonsterAttack')

        def ValidateSuspendAfter(*args):
            s = SuspendAfter.get()
            if len(s) > 2:
                if not s[-1].isdigit():
                    SuspendAfter.set(s[:-1])
                else:
                    SuspendAfter.set(s[:2])

        def ValidateMonstersRange(*args):
            s = MonstersRange.get()
            if len(s) > 2:
                if not s[-1].isdigit():
                    MonstersRange.set(s[:-1])
                else:
                    MonstersRange.set(s[:2])

        # endregion

        # region Functions DepotWalker

        def SetLoadAutoSeller():
            if not LoadAutoSeller.get():
                LoadAutoSeller.set(True)
                ButtonAutoSeller.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
            else:
                LoadAutoSeller.set(False)
                ButtonAutoSeller.configure(relief=RAISED, bg=rgb((127, 17, 8)))

        def SetLoadAutoBanker():
            if not LoadAutoBanker.get():
                LoadAutoBanker.set(True)
                ButtonAutoBanker.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
            else:
                LoadAutoBanker.set(False)
                ButtonAutoBanker.configure(relief=RAISED, bg=rgb((127, 17, 8)))

        def SetLoadSortLoot():
            if not LoadSortLoot.get():
                LoadSortLoot.set(True)
                ButtonSortLoot.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
            else:
                LoadSortLoot.set(False)
                ButtonSortLoot.configure(relief=RAISED, bg=rgb((127, 17, 8)))

        # endregion

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedDebugging, CheckDebugging.get(), 'Debugging')
            CheckingGUI(InitiatedHotkeyPause, CheckHotkeyPause.get(), 'HotkeyPause')
            CheckingGUI(InitiatedHotkeyToPause, HotkeyToPause.get(), 'HotkeyToPause')
            CheckingGUI(InitiatedPriorityOne, PriorityOne.get(), 'PriorityOne')
            CheckingGUI(InitiatedPriorityTwo, PriorityTwo.get(), 'PriorityTwo')
            CheckingGUI(InitiatedPriorityThree, PriorityThree.get(), 'PriorityThree')
            CheckingGUI(InitiatedPriorityFour, PriorityFour.get(), 'PriorityFour')
            CheckingGUI(InitiatedSelectedMonster, SelectedMonster.get(), 'SelectedMonster')
            CheckingGUI(InitiatedSelectedMonster2, SelectedMonster2.get(), 'SelectedMonster2')
            CheckingGUI(InitiatedSelectedMonster3, SelectedMonster3.get(), 'SelectedMonster3')
            CheckingGUI(InitiatedSelectedMonster4, SelectedMonster4.get(), 'SelectedMonster4')
            CheckingGUI(InitiatedSelectedAttackMode, SelectedAttackMode.get(), 'SelectedAttackMode')
            CheckingGUI(InitiatedAttackOne, CheckAttackOne.get(), 'AttackOne')
            CheckingGUI(InitiatedAttackTwo, CheckAttackTwo.get(), 'AttackTwo')
            CheckingGUI(InitiatedAttackThree, CheckAttackThree.get(), 'AttackThree')
            CheckingGUI(InitiatedAttackFour, CheckAttackFour.get(), 'AttackFour')
            CheckingGUI(InitiatedFollow, CheckFollow.get(), 'Follow')
            CheckingGUI(InitiatedCantAttack, CheckCantAttack.get(), 'CantAttack')
            CheckingGUI(InitiatedAttackPlayers, CheckAttackPlayers.get(), 'AttackPlayers')
            CheckingGUI(InitiatedPlayerSeen, CheckPlayerSeen.get(), 'PlayerSeen')
            CheckingGUI(InitiatedAttackingYou, CheckAttackingYou.get(), 'AttackingYou')
            CheckingGUI(InitiatedForceAttack, CheckForceAttack.get(), 'ForceAttack')
            CheckingGUI(InitiatedSuspendAfter, SuspendAfter.get(), 'SuspendAfter')
            CheckingGUI(InitiatedMonstersRange, MonstersRange.get(), 'MonstersRange')
            CheckingGUI(InitiatedCavebotMode, RadioCavebotMode.get(), 'CavebotMode')
            CheckingGUI(InitiatedRadius, Radius.get(), 'Radius')
            CheckingGUI(InitiatedDelay, Delay.get(), 'Delay')
            CheckingGUI(InitiatedWaypoint_X, Waypoint_X.get(), 'Waypoint_X')
            CheckingGUI(InitiatedWaypoint_Y, Waypoint_Y.get(), 'Waypoint_Y')
            CheckingGUI(InitiatedWaypoint_Z, Waypoint_Z.get(), 'Waypoint_Z')
            CheckingGUI(InitiatedStand, Stand.get(), 'Stand')
            CheckingGUI(InitiatedResearchMap, ResearchMap.get(), 'ResearchMap')
            CheckingGUI(InitiatedMarkValue, RadioMarkValue.get(), 'MarkValue')
            CheckingGUI(InitiatedDropItems, CheckDropItems.get(), 'DropItems')
            CheckingGUI(InitiatedLoadAutoSeller, LoadAutoSeller.get(), 'LoadAutoSeller')
            CheckingGUI(InitiatedLoadAutoBanker, LoadAutoBanker.get(), 'LoadAutoBanker')
            CheckingGUI(InitiatedLoadSortLoot, LoadSortLoot.get(), 'LoadSortLoot')
            CheckingGUI(InitiatedCapBelowThan, CapBelowThan.get(), 'CapBelowThan')
            CheckingGUI(InitiatedLootWhileKilling, CheckLootWhileKilling.get(), 'LootWhileKilling')
            CheckingGUI(InitiatedTibiaCustomLoot, CheckTibiaCustomLoot.get(), 'TibiaCustomLoot')
            CheckingGUI(InitiatedSQM1, CheckSQM1.get(), 'SQM1')
            CheckingGUI(InitiatedSQM2, CheckSQM2.get(), 'SQM2')
            CheckingGUI(InitiatedSQM3, CheckSQM3.get(), 'SQM3')
            CheckingGUI(InitiatedSQM4, CheckSQM4.get(), 'SQM4')
            CheckingGUI(InitiatedSQM5, CheckSQM5.get(), 'SQM5')
            CheckingGUI(InitiatedSQM6, CheckSQM6.get(), 'SQM6')
            CheckingGUI(InitiatedSQM7, CheckSQM7.get(), 'SQM7')
            CheckingGUI(InitiatedSQM8, CheckSQM8.get(), 'SQM8')
            CheckingGUI(InitiatedSQM9, CheckSQM9.get(), 'SQM9')
            CheckingGUI(InitiatedCapLimit, CapLimit.get(), 'CapLimit')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.CaveBot.destroyWindow()


        # region Variables MonsterAttacking

        PriorityOne = tk.IntVar()
        InitiatedPriorityOne = self.Setter.GetVar("PriorityOne")
        PriorityOne.set(InitiatedPriorityOne)

        PriorityTwo = tk.IntVar()
        InitiatedPriorityTwo = self.Setter.GetVar("PriorityTwo")
        PriorityTwo.set(InitiatedPriorityTwo)

        PriorityThree = tk.IntVar()
        InitiatedPriorityThree = self.Setter.GetVar("PriorityThree")
        PriorityThree.set(InitiatedPriorityThree)

        PriorityFour = tk.IntVar()
        InitiatedPriorityFour = self.Setter.GetVar("PriorityFour")
        PriorityFour.set(InitiatedPriorityFour)

        SelectedMonster = tk.StringVar()
        InitiatedSelectedMonster = self.Setter.GetVar("SelectedMonster")
        SelectedMonster.set(InitiatedSelectedMonster)

        SelectedMonster2 = tk.StringVar()
        InitiatedSelectedMonster2 = self.Setter.GetVar("SelectedMonster2")
        SelectedMonster2.set(InitiatedSelectedMonster2)

        SelectedMonster3 = tk.StringVar()
        InitiatedSelectedMonster3 = self.Setter.GetVar("SelectedMonster3")
        SelectedMonster3.set(InitiatedSelectedMonster3)

        SelectedMonster4 = tk.StringVar()
        InitiatedSelectedMonster4 = self.Setter.GetVar("SelectedMonster4")
        SelectedMonster4.set(InitiatedSelectedMonster4)

        SelectedAttackMode = tk.StringVar()
        InitiatedSelectedAttackMode = self.Setter.GetVar("SelectedAttackMode")
        SelectedAttackMode.set(InitiatedSelectedAttackMode)

        CheckAttackOne = tk.BooleanVar()
        InitiatedAttackOne = self.Setter.GetBoolVar("AttackOne")
        CheckAttackOne.set(InitiatedAttackOne)

        CheckAttackTwo = tk.BooleanVar()
        InitiatedAttackTwo = self.Setter.GetBoolVar("AttackTwo")
        CheckAttackTwo.set(InitiatedAttackTwo)

        CheckAttackThree = tk.BooleanVar()
        InitiatedAttackThree = self.Setter.GetBoolVar("AttackThree")
        CheckAttackThree.set(InitiatedAttackThree)

        CheckAttackFour = tk.BooleanVar()
        InitiatedAttackFour = self.Setter.GetBoolVar("AttackFour")
        CheckAttackFour.set(InitiatedAttackFour)

        CheckFollow = tk.BooleanVar()
        InitiatedFollow = self.Setter.GetBoolVar("Follow")
        CheckFollow.set(InitiatedFollow)

        CheckCantAttack = tk.BooleanVar()
        InitiatedCantAttack = self.Setter.GetBoolVar("CantAttack")
        CheckCantAttack.set(InitiatedCantAttack)

        CheckAttackPlayers = tk.BooleanVar()
        InitiatedAttackPlayers = self.Setter.GetBoolVar("AttackPlayers")
        CheckAttackPlayers.set(InitiatedAttackPlayers)

        CheckPlayerSeen = tk.BooleanVar()
        InitiatedPlayerSeen = self.Setter.GetBoolVar("PlayerSeen")
        CheckPlayerSeen.set(InitiatedPlayerSeen)

        CheckAttackingYou = tk.BooleanVar()
        InitiatedAttackingYou = self.Setter.GetBoolVar("AttackingYou")
        CheckAttackingYou.set(InitiatedAttackingYou)

        CheckForceAttack = tk.BooleanVar()
        InitiatedForceAttack = self.Setter.GetBoolVar("ForceAttack")
        CheckForceAttack.set(InitiatedForceAttack)

        SuspendAfter = tk.StringVar()
        InitiatedSuspendAfter = self.Setter.GetVar("SuspendAfter")
        SuspendAfter.set(InitiatedSuspendAfter)

        MonstersRange = tk.StringVar()
        InitiatedMonstersRange = self.Setter.GetVar("MonstersRange")
        MonstersRange.set(InitiatedMonstersRange)

        # endregion

        # region Variables Walker

        RadioCavebotMode = tk.IntVar()
        InitiatedCavebotMode = self.Setter.GetVar("CavebotMode")
        RadioCavebotMode.set(InitiatedCavebotMode)

        Radius = tk.StringVar()
        InitiatedRadius = self.Setter.GetVar("Radius")
        Radius.set(InitiatedRadius)

        Delay = tk.StringVar()
        InitiatedDelay = self.Setter.GetVar("Delay")
        Delay.set(InitiatedDelay)

        Waypoint_X = tk.StringVar() # Lembrar de setar posição atual do player
        InitiatedWaypoint_X = self.Setter.GetVar("Waypoint_X")
        Waypoint_X.set(InitiatedWaypoint_X)

        Waypoint_Y = tk.StringVar() # Lembrar de setar posição atual do player
        InitiatedWaypoint_Y = self.Setter.GetVar("Waypoint_Y")
        Waypoint_Y.set(InitiatedWaypoint_Y)

        Waypoint_Z = tk.StringVar() # Lembrar de setar posição atual do player
        InitiatedWaypoint_Z = self.Setter.GetVar("Waypoint_Z")
        Waypoint_Z.set(InitiatedWaypoint_Z)

        Stand = tk.StringVar()
        InitiatedStand = self.Setter.GetVar("Stand")
        Stand.set(InitiatedStand)

        ResearchMap = tk.BooleanVar()
        InitiatedResearchMap = self.Setter.GetBoolVar("ResearchMap")
        ResearchMap.set(InitiatedResearchMap)

        ImageMark1 = ImageTk.PhotoImage(Image.open('images/MapSettings/CheckMark.png'))
        ImageMark2 = ImageTk.PhotoImage(Image.open('images/MapSettings/QuestionMark.png'))
        ImageMark3 = ImageTk.PhotoImage(Image.open('images/MapSettings/ExclimationMark.png'))
        ImageMark4 = ImageTk.PhotoImage(Image.open('images/MapSettings/Star.png'))
        ImageMark5 = ImageTk.PhotoImage(Image.open('images/MapSettings/Cross.png'))
        ImageMark6 = ImageTk.PhotoImage(Image.open('images/MapSettings/Church.png'))
        ImageMark7 = ImageTk.PhotoImage(Image.open('images/MapSettings/Mouth.png'))
        ImageMark8 = ImageTk.PhotoImage(Image.open('images/MapSettings/Shovel.png'))
        ImageMark9 = ImageTk.PhotoImage(Image.open('images/MapSettings/Sword.png'))
        ImageMark10 = ImageTk.PhotoImage(Image.open('images/MapSettings/Flag.png'))
        ImageMark11 = ImageTk.PhotoImage(Image.open('images/MapSettings/Lock.png'))
        ImageMark12 = ImageTk.PhotoImage(Image.open('images/MapSettings/Bag.png'))
        ImageMark13 = ImageTk.PhotoImage(Image.open('images/MapSettings/Skull.png'))
        ImageMark14 = ImageTk.PhotoImage(Image.open('images/MapSettings/Money.png'))
        ImageMark15 = ImageTk.PhotoImage(Image.open('images/MapSettings/ArrowUp.png'))
        ImageMark16 = ImageTk.PhotoImage(Image.open('images/MapSettings/ArrowDown.png'))
        ImageMark17 = ImageTk.PhotoImage(Image.open('images/MapSettings/ArrowRight.png'))
        ImageMark18 = ImageTk.PhotoImage(Image.open('images/MapSettings/ArrowLeft.png'))
        ImageMark19 = ImageTk.PhotoImage(Image.open('images/MapSettings/Above.png'))
        ImageMark20 = ImageTk.PhotoImage(Image.open('images/MapSettings/Bellow.png'))

        RadioMarkValue = tk.IntVar()
        InitiatedMarkValue = self.Setter.GetVar("MarkValue")
        RadioMarkValue.set(InitiatedMarkValue)

        # endregion

        # region Variables DepotWalker

        CheckDropItems = tk.BooleanVar()
        InitiatedDropItems = self.Setter.GetBoolVar("DropItems")
        CheckDropItems.set(InitiatedDropItems)

        LoadAutoSeller = tk.BooleanVar()
        InitiatedLoadAutoSeller = self.Setter.GetBoolVar("LoadAutoSeller")
        LoadAutoSeller.set(InitiatedLoadAutoSeller)

        LoadAutoBanker = tk.BooleanVar()
        InitiatedLoadAutoBanker = self.Setter.GetBoolVar("LoadAutoBanker")
        LoadAutoBanker.set(InitiatedLoadAutoBanker)

        LoadSortLoot = tk.BooleanVar()
        InitiatedLoadSortLoot = self.Setter.GetBoolVar("LoadSortLoot")
        LoadSortLoot.set(InitiatedLoadSortLoot)

        CapBelowThan = tk.StringVar()
        InitiatedCapBelowThan = self.Setter.GetVar("CapBelowThan")
        CapBelowThan.set(InitiatedCapBelowThan)

        # endregion

        # region Variables CorpseLooting

        CheckLootWhileKilling = tk.BooleanVar()
        InitiatedLootWhileKilling = self.Setter.GetBoolVar("LootWhileKilling")
        CheckLootWhileKilling.set(InitiatedLootWhileKilling)

        CheckTibiaCustomLoot = tk.BooleanVar()
        InitiatedTibiaCustomLoot = self.Setter.GetBoolVar("TibiaCustomLoot")
        CheckTibiaCustomLoot.set(InitiatedTibiaCustomLoot)

        CheckSQM1 = tk.BooleanVar()
        InitiatedSQM1 = self.Setter.GetBoolVar("SQM1")
        CheckSQM1.set(InitiatedSQM1)

        CheckSQM2 = tk.BooleanVar()
        InitiatedSQM2 = self.Setter.GetBoolVar("SQM2")
        CheckSQM2.set(InitiatedSQM2)

        CheckSQM3 = tk.BooleanVar()
        InitiatedSQM3 = self.Setter.GetBoolVar("SQM3")
        CheckSQM3.set(InitiatedSQM3)

        CheckSQM4 = tk.BooleanVar()
        InitiatedSQM4 = self.Setter.GetBoolVar("SQM4")
        CheckSQM4.set(InitiatedSQM4)

        CheckSQM5 = tk.BooleanVar()
        InitiatedSQM5 = self.Setter.GetBoolVar("SQM5")
        CheckSQM5.set(InitiatedSQM5)

        CheckSQM6 = tk.BooleanVar()
        InitiatedSQM6 = self.Setter.GetBoolVar("SQM6")
        CheckSQM6.set(InitiatedSQM6)

        CheckSQM7 = tk.BooleanVar()
        InitiatedSQM7 = self.Setter.GetBoolVar("SQM7")
        CheckSQM7.set(InitiatedSQM7)

        CheckSQM8 = tk.BooleanVar()
        InitiatedSQM8 = self.Setter.GetBoolVar("SQM8")
        CheckSQM8.set(InitiatedSQM8)

        CheckSQM9 = tk.BooleanVar()
        InitiatedSQM9 = self.Setter.GetBoolVar("SQM9")
        CheckSQM9.set(InitiatedSQM9)

        CapLimit = tk.StringVar()
        InitiatedCapLimit = self.Setter.GetVar("CapLimit")
        CapLimit.set(InitiatedCapLimit)

        # endregion

        self.CaveBot.addButton('Ok', Destroy, [74, 22], [378, 601])

        # region GUI MonsterAttacking

        OptionAttackMode = self.CaveBot.addOption(SelectedAttackMode, AttackModes, [103, 328], 10)

        CheckboxAttackOne = self.CaveBot.addCheck(CheckAttackOne, [25, 40], InitiatedAttackOne, 'Monster One')
        OptionMonstersOne = self.CaveBot.addOption(SelectedMonster, monsters, [155, 40], 16)
        PriorityMonstersOne = self.CaveBot.addOption(PriorityOne, priority, [300, 40])

        CheckboxAttackTwo = self.CaveBot.addCheck(CheckAttackTwo, [25, 80], InitiatedAttackTwo, 'Monster Two')
        OptionMonstersTwo = self.CaveBot.addOption(SelectedMonster2, monsters, [155, 80], 16)
        PriorityMonstersTwo = self.CaveBot.addOption(PriorityTwo, priority, [300, 80])

        CheckboxAttackThree = self.CaveBot.addCheck(CheckAttackThree, [25, 120], InitiatedAttackThree, 'Monster Three')
        OptionMonstersThree = self.CaveBot.addOption(SelectedMonster3, monsters, [155, 120], 16)
        PriorityMonstersThree = self.CaveBot.addOption(PriorityThree, priority, [300, 120])

        CheckboxAttackFour = self.CaveBot.addCheck(CheckAttackFour, [25, 160], InitiatedAttackFour, 'Monster Four')
        OptionMonstersFour = self.CaveBot.addOption(SelectedMonster4, monsters, [155, 160], 16)
        PriorityMonstersFour = self.CaveBot.addOption(PriorityFour, priority, [300, 160])

        CheckBoxFollow = self.CaveBot.addCheck(CheckFollow, [20, 200], InitiatedFollow, 'Auto Follow Mode')
        CheckBoxCantAttack = self.CaveBot.addCheck(CheckCantAttack, [20, 220], InitiatedCantAttack, "Suspend When Can't Attack")
        CheckBoxAttackPlayers = self.CaveBot.addCheck(CheckAttackPlayers, [20, 240], InitiatedAttackPlayers, "Don't Attack Players")
        CheckBoxPlayerSeen = self.CaveBot.addCheck(CheckPlayerSeen, [195, 200], InitiatedPlayerSeen, 'Reduced Attack When Player Seen')
        CheckBoxAttackingYou = self.CaveBot.addCheck(CheckAttackingYou, [183, 240], InitiatedAttackingYou, 'Attack Only Monsters Attacking You')
        CheckBoxForceAttack = self.CaveBot.addCheck(CheckForceAttack, [195, 220], InitiatedForceAttack, 'Force Attack When Attacked')

        LabelSuspendAfter = self.CaveBot.addLabel('Suspend After Unreachable:', [100, 280])
        LabelMonstersRange = self.CaveBot.addLabel('Consider Monsters In Range:', [100, 300])
        LabelAttackMode = self.CaveBot.addLabel('Attack Mode:', [20, 331])

        EntrySuspendAfter = self.CaveBot.addEntry([270, 280], SuspendAfter, 5)
        SuspendAfter.trace("w", ValidateSuspendAfter)
        EntryMonstersRange = self.CaveBot.addEntry([270, 300], MonstersRange, 5)
        MonstersRange.trace("w", ValidateMonstersRange)

        # endregion

        # region GUI Walker

        RadioWaypoint = self.CaveBot.addRadio('Waypoints', RadioCavebotMode, 0, [26, 414], CheckClick)
        RadioMark = self.CaveBot.addRadio('Marks', RadioCavebotMode, 1, [115, 414], CheckClick)

        LabelStand = self.CaveBot.addLabel('Stand Still After Reaching Waypoint For:', [24, 520])

        ButtonResearchMap = self.CaveBot.addButton('Auto Research Map', SetResearchMap, [130, 37], [268, 513])

        # endregion

        # region GUI DepotWalker

        CheckboxDropItems = self.CaveBot.addCheck(CheckDropItems, [425, 28], InitiatedDropItems, 'Drop Items Instead Of Deposit')
        LabelGoDepot = self.CaveBot.addLabel('Go To Depot When Cap Below Than:', [480, 50])

        EntryCapBelowThan = self.CaveBot.addEntry([680, 50], CapBelowThan, 5)

        ButtonAutoSeller = self.CaveBot.addButton('Load AutoSeller', SetLoadAutoSeller, [110, 28], [450, 80])
        ButtonAutoBanker = self.CaveBot.addButton('Load AutoBanker', SetLoadAutoBanker, [120, 28], [570, 80])
        ButtonSortLoot = self.CaveBot.addButton('Load SortLoot', SetLoadSortLoot, [100, 28], [700, 80])

        # endregion

        # region GUI CorpseLooting

        LabelCapLimit = self.CaveBot.addLabel('Loot Capacity Limit:', [435, 150])
        EntryCapLimit = self.CaveBot.addEntry([551, 148], CapLimit, 5)

        CheckBoxLootWhileKilling = self.CaveBot.addCheck(CheckLootWhileKilling, [435, 180], InitiatedLootWhileKilling, 'Loot While Killing')
        CheckBoxTibiaCustomLoot = self.CaveBot.addCheck(CheckTibiaCustomLoot, [585, 180], InitiatedTibiaCustomLoot, 'Loot From Tibia Custom Loot')

        LabelLootAround = self.CaveBot.addLabel('Configure Loot Around:', [545, 220])

        CheckBoxSQM1 = self.CaveBot.addCheck(CheckSQM1, [570, 310], InitiatedSQM1)
        CheckBoxSQM2 = self.CaveBot.addCheck(CheckSQM2, [600, 310], InitiatedSQM2)
        CheckBoxSQM3 = self.CaveBot.addCheck(CheckSQM3, [630, 310], InitiatedSQM3)
        CheckBoxSQM4 = self.CaveBot.addCheck(CheckSQM4, [570, 280], InitiatedSQM4)
        CheckBoxSQM5 = self.CaveBot.addCheck(CheckSQM5, [600, 280], InitiatedSQM5)
        CheckBoxSQM6 = self.CaveBot.addCheck(CheckSQM6, [630, 280], InitiatedSQM6)
        CheckBoxSQM7 = self.CaveBot.addCheck(CheckSQM7, [570, 250], InitiatedSQM7)
        CheckBoxSQM8 = self.CaveBot.addCheck(CheckSQM8, [600, 250], InitiatedSQM8)
        CheckBoxSQM9 = self.CaveBot.addCheck(CheckSQM9, [630, 250], InitiatedSQM9)

        # endregion

        def Checking():
            if RadioCavebotMode.get() == 0:
                print('Walker Mode:', RadioCavebotMode.get())

                self.CaveBot.addImage(Back, [23, 440])
                self.CaveBot.addImage(Back, [23, 450])
                self.CaveBot.addImage(Back2, [197, 405])

                LabelWaypoints = self.CaveBot.addLabel('Waypoints:', [236, 402])
                LabelRadius = self.CaveBot.addLabel('Radius:', [24, 451])
                LabelDelay = self.CaveBot.addLabel('Delay:', [111, 451])

                EntryRadius = self.CaveBot.addEntry([70, 452], Radius, 5)
                Radius.trace("w", ValidateRadius)
                EntryDelay = self.CaveBot.addEntry([154, 452], Delay, 5)
                Delay.trace("w", ValidateDelay)
                LabelWaypointX = self.CaveBot.addLabel('X:', [26, 479])
                EntryWaypointX = self.CaveBot.addEntry([42, 480], Waypoint_X, 5)
                Waypoint_X.trace("w", ValidateWaypoint_X)
                LabelWaypointY = self.CaveBot.addLabel('Y:', [81, 479])
                EntryWaypointY = self.CaveBot.addEntry([97, 480], Waypoint_Y, 5)
                Waypoint_Y.trace("w", ValidateWaypoint_Y)
                LabelWaypointZ = self.CaveBot.addLabel('Z:', [135, 479])
                EntryWaypointZ = self.CaveBot.addEntry([151, 480], Waypoint_Z, 5)
                Waypoint_Z.trace("w", ValidateWaypoint_Z)
                EntryStand = self.CaveBot.addEntry([244, 520], Stand, 2)
                Stand.trace("w", ValidateStand)

                ButtonRemoveWalker = self.CaveBot.addButton('<<<', RemoveWalker, [29, 23], [197, 424])
                ButtonAddWalker = self.CaveBot.addButton('>>>', AddWalker, [29, 23], [197, 479])
                if EnabledCaveBot:
                    LabelWaypoints.configure(state='disabled')
                    LabelRadius.configure(state='disabled')
                    LabelDelay.configure(state='disabled')
                    EntryRadius.configure(state='disabled')
                    EntryDelay.configure(state='disabled')
                    LabelWaypointX.configure(state='disabled')
                    EntryWaypointX.configure(state='disabled')
                    LabelWaypointY.configure(state='disabled')
                    EntryWaypointY.configure(state='disabled')
                    LabelWaypointZ.configure(state='disabled')
                    EntryWaypointZ.configure(state='disabled')
                    EntryStand.configure(state='disabled')
                    ButtonResearchMap.configure(state='disabled')
                    ButtonRemoveWalker.configure(state='disabled')
                    ButtonAddWalker.configure(state='disabled')
                else:
                    LabelWaypoints.configure(state='normal')
                    LabelRadius.configure(state='normal')
                    LabelDelay.configure(state='normal')
                    EntryRadius.configure(state='normal')
                    EntryDelay.configure(state='normal')
                    LabelWaypointX.configure(state='normal')
                    EntryWaypointX.configure(state='normal')
                    LabelWaypointY.configure(state='normal')
                    EntryWaypointY.configure(state='normal')
                    LabelWaypointZ.configure(state='normal')
                    EntryWaypointZ.configure(state='normal')
                    EntryStand.configure(state='normal')
                    ButtonResearchMap.configure(state='normal')
                    ButtonRemoveWalker.configure(state='normal')
                    ButtonAddWalker.configure(state='normal')
            elif RadioCavebotMode.get() == 1:
                print('Walker Mode:', RadioCavebotMode.get())

                self.CaveBot.addImage(Back, [23, 450])
                self.CaveBot.addImage(Back2, [197, 405])

                LabelWaypoints = self.CaveBot.addLabel('Marks:', [246, 402])

                self.CaveBot.addRadioImage('', RadioMarkValue, 1, [24, 441], CheckMarkClick, ImageMark1)
                self.CaveBot.addRadioImage('', RadioMarkValue, 2, [54, 441], CheckMarkClick, ImageMark2)
                self.CaveBot.addRadioImage('', RadioMarkValue, 3, [84, 441], CheckMarkClick, ImageMark3)
                self.CaveBot.addRadioImage('', RadioMarkValue, 4, [114, 441], CheckMarkClick, ImageMark4)
                self.CaveBot.addRadioImage('', RadioMarkValue, 5, [144, 441], CheckMarkClick, ImageMark5)
                self.CaveBot.addRadioImage('', RadioMarkValue, 6, [174, 441], CheckMarkClick, ImageMark6)
                self.CaveBot.addRadioImage('', RadioMarkValue, 7, [204, 441], CheckMarkClick, ImageMark7)
                self.CaveBot.addRadioImage('', RadioMarkValue, 8, [24, 461], CheckMarkClick, ImageMark8)
                self.CaveBot.addRadioImage('', RadioMarkValue, 9, [54, 461], CheckMarkClick, ImageMark9)
                self.CaveBot.addRadioImage('', RadioMarkValue, 0, [84, 461], CheckMarkClick, ImageMark10)
                self.CaveBot.addRadioImage('', RadioMarkValue, 11, [114, 461], CheckMarkClick, ImageMark11)
                self.CaveBot.addRadioImage('', RadioMarkValue, 12, [144, 461], CheckMarkClick, ImageMark12)
                self.CaveBot.addRadioImage('', RadioMarkValue, 13, [174, 461], CheckMarkClick, ImageMark13)
                self.CaveBot.addRadioImage('', RadioMarkValue, 14, [204, 461], CheckMarkClick, ImageMark14)
                self.CaveBot.addRadioImage('', RadioMarkValue, 15, [24, 481], CheckMarkClick, ImageMark15)
                self.CaveBot.addRadioImage('', RadioMarkValue, 16, [54, 481], CheckMarkClick, ImageMark16)
                self.CaveBot.addRadioImage('', RadioMarkValue, 17, [84, 481], CheckMarkClick, ImageMark17)
                self.CaveBot.addRadioImage('', RadioMarkValue, 18, [114, 481], CheckMarkClick, ImageMark18)
                self.CaveBot.addRadioImage('', RadioMarkValue, 19, [144, 481], CheckMarkClick, ImageMark19)
                self.CaveBot.addRadioImage('', RadioMarkValue, 20, [174, 481], CheckMarkClick, ImageMark20)

                if EnabledCaveBot:
                    LabelWaypoints.configure(state='disabled')
                else:
                    LabelWaypoints.configure(state='normal')

        def CheckingButtons():
            if EnabledCaveBot:
                CheckboxDebugging.configure(state='disabled')
                CheckboxHotkeyPause.configure(state='disabled')
                ButtonHotkeyPause.configure(state='disabled')

                OptionAttackMode.configure(state='disabled')
                CheckboxAttackOne.configure(state='disabled')
                OptionMonstersOne.configure(state='disabled')
                PriorityMonstersOne.configure(state='disabled')
                CheckboxAttackTwo.configure(state='disabled')
                OptionMonstersTwo.configure(state='disabled')
                PriorityMonstersTwo.configure(state='disabled')
                CheckboxAttackThree.configure(state='disabled')
                OptionMonstersThree.configure(state='disabled')
                PriorityMonstersThree.configure(state='disabled')
                CheckboxAttackFour.configure(state='disabled')
                OptionMonstersFour.configure(state='disabled')
                PriorityMonstersFour.configure(state='disabled')
                CheckBoxFollow.configure(state='disabled')
                CheckBoxCantAttack.configure(state='disabled')
                CheckBoxAttackPlayers.configure(state='disabled')
                CheckBoxPlayerSeen.configure(state='disabled')
                CheckBoxAttackingYou.configure(state='disabled')
                CheckBoxForceAttack.configure(state='disabled')
                LabelSuspendAfter.configure(state='disabled')
                LabelMonstersRange.configure(state='disabled')
                LabelAttackMode.configure(state='disabled')
                EntrySuspendAfter.configure(state='disabled')
                EntryMonstersRange.configure(state='disabled')

                RadioWaypoint.configure(state='disabled')
                RadioMark.configure(state='disabled')
                LabelStand.configure(state='disabled')

                CheckboxDropItems.configure(state='disabled')
                LabelGoDepot.configure(state='disabled')
                EntryCapBelowThan.configure(state='disabled')
                ButtonAutoSeller.configure(state='disabled')
                ButtonAutoBanker.configure(state='disabled')
                ButtonSortLoot.configure(state='disabled')

                LabelCapLimit.configure(state='disabled')
                EntryCapLimit.configure(state='disabled')
                CheckBoxLootWhileKilling.configure(state='disabled')
                CheckBoxTibiaCustomLoot.configure(state='disabled')
                LabelLootAround.configure(state='disabled')
                CheckBoxSQM1.configure(state='disabled')
                CheckBoxSQM2.configure(state='disabled')
                CheckBoxSQM3.configure(state='disabled')
                CheckBoxSQM4.configure(state='disabled')
                CheckBoxSQM5.configure(state='disabled')
                CheckBoxSQM6.configure(state='disabled')
                CheckBoxSQM7.configure(state='disabled')
                CheckBoxSQM8.configure(state='disabled')
                CheckBoxSQM9.configure(state='disabled')
            else:
                CheckboxDebugging.configure(state='normal')
                CheckboxHotkeyPause.configure(state='normal')
                ButtonHotkeyPause.configure(state='normal')

                OptionAttackMode.configure(state='normal')
                CheckboxAttackOne.configure(state='normal')
                CheckboxAttackTwo.configure(state='normal')
                CheckboxAttackThree.configure(state='normal')
                CheckboxAttackFour.configure(state='normal')
                if not CheckAttackOne.get():
                    OptionMonstersOne.configure(state='disabled')
                    PriorityMonstersOne.configure(state='disabled')
                else:
                    OptionMonstersOne.configure(state='normal')
                    PriorityMonstersOne.configure(state='normal')
                if not CheckAttackTwo.get():
                    OptionMonstersTwo.configure(state='disabled')
                    PriorityMonstersTwo.configure(state='disabled')
                else:
                    OptionMonstersTwo.configure(state='normal')
                    PriorityMonstersTwo.configure(state='normal')
                if not CheckAttackThree.get():
                    OptionMonstersThree.configure(state='disabled')
                    PriorityMonstersThree.configure(state='disabled')
                else:
                    OptionMonstersThree.configure(state='normal')
                    PriorityMonstersThree.configure(state='normal')
                if not CheckAttackFour.get():
                    OptionMonstersFour.configure(state='disabled')
                    PriorityMonstersFour.configure(state='disabled')
                else:
                    OptionMonstersFour.configure(state='normal')
                    PriorityMonstersFour.configure(state='normal')
                CheckBoxFollow.configure(state='normal')
                CheckBoxCantAttack.configure(state='normal')
                CheckBoxAttackPlayers.configure(state='normal')
                CheckBoxPlayerSeen.configure(state='normal')
                CheckBoxAttackingYou.configure(state='normal')
                CheckBoxForceAttack.configure(state='normal')
                LabelSuspendAfter.configure(state='normal')
                LabelMonstersRange.configure(state='normal')
                LabelAttackMode.configure(state='normal')
                EntrySuspendAfter.configure(state='normal')
                EntryMonstersRange.configure(state='normal')

                RadioWaypoint.configure(state='normal')
                RadioMark.configure(state='normal')
                LabelStand.configure(state='normal')

                CheckboxDropItems.configure(state='normal')
                if CheckDropItems.get():
                    LabelGoDepot.configure(state='disabled')
                    EntryCapBelowThan.configure(state='disabled')
                    ButtonAutoSeller.configure(state='disabled')
                    ButtonAutoBanker.configure(state='disabled')
                    ButtonSortLoot.configure(state='disabled')
                else:
                    LabelGoDepot.configure(state='normal')
                    EntryCapBelowThan.configure(state='normal')
                    ButtonAutoSeller.configure(state='normal')
                    ButtonAutoBanker.configure(state='normal')
                    ButtonSortLoot.configure(state='normal')
                LabelCapLimit.configure(state='normal')
                EntryCapLimit.configure(state='normal')
                CheckBoxLootWhileKilling.configure(state='normal')
                CheckBoxTibiaCustomLoot.configure(state='normal')
                LabelLootAround.configure(state='normal')
                CheckBoxSQM1.configure(state='normal')
                CheckBoxSQM2.configure(state='normal')
                CheckBoxSQM3.configure(state='normal')
                CheckBoxSQM4.configure(state='normal')
                CheckBoxSQM5.configure(state='normal')
                CheckBoxSQM6.configure(state='normal')
                CheckBoxSQM7.configure(state='normal')
                CheckBoxSQM8.configure(state='normal')
                CheckBoxSQM9.configure(state='normal')

                if ResearchMap.get():
                    ButtonResearchMap.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
                else:
                    ButtonResearchMap.configure(relief=RAISED, bg=rgb((127, 17, 8)))
                if LoadAutoSeller.get():
                    ButtonAutoSeller.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
                else:
                    ButtonAutoSeller.configure(relief=RAISED, bg=rgb((127, 17, 8)))
                if LoadAutoBanker.get():
                    ButtonAutoBanker.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
                else:
                    ButtonAutoBanker.configure(relief=RAISED, bg=rgb((127, 17, 8)))
                if LoadSortLoot.get():
                    ButtonSortLoot.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
                else:
                    ButtonSortLoot.configure(relief=RAISED, bg=rgb((127, 17, 8)))

        def ConstantVerify():
            if not EnabledCaveBot:
                if not CheckAttackOne.get():
                    OptionMonstersOne.configure(state='disabled')
                    PriorityMonstersOne.configure(state='disabled')
                else:
                    OptionMonstersOne.configure(state='normal')
                    PriorityMonstersOne.configure(state='normal')
                if not CheckAttackTwo.get():
                    OptionMonstersTwo.configure(state='disabled')
                    PriorityMonstersTwo.configure(state='disabled')
                else:
                    OptionMonstersTwo.configure(state='normal')
                    PriorityMonstersTwo.configure(state='normal')
                if not CheckAttackThree.get():
                    OptionMonstersThree.configure(state='disabled')
                    PriorityMonstersThree.configure(state='disabled')
                else:
                    OptionMonstersThree.configure(state='normal')
                    PriorityMonstersThree.configure(state='normal')
                if not CheckAttackFour.get():
                    OptionMonstersFour.configure(state='disabled')
                    PriorityMonstersFour.configure(state='disabled')
                else:
                    OptionMonstersFour.configure(state='normal')
                    PriorityMonstersFour.configure(state='normal')
                if CheckDropItems.get():
                    LabelGoDepot.configure(state='disabled')
                    EntryCapBelowThan.configure(state='disabled')
                    ButtonAutoSeller.configure(state='disabled')
                    ButtonAutoBanker.configure(state='disabled')
                    ButtonSortLoot.configure(state='disabled')
                else:
                    LabelGoDepot.configure(state='normal')
                    EntryCapBelowThan.configure(state='normal')
                    ButtonAutoSeller.configure(state='normal')
                    ButtonAutoBanker.configure(state='normal')
                    ButtonSortLoot.configure(state='normal')
                if not CheckHotkeyPause.get():
                    ButtonHotkeyPause.configure(state='disabled')
                elif CheckHotkeyPause.get():
                    ButtonHotkeyPause.configure(state='normal')

            self.CaveBot.After(300, ConstantVerify)

        CheckingButtons()
        ConstantVerify()

        Checking()

        self.CaveBot.Protocol(Destroy)
        self.CaveBot.loop()
