import json
import time
import threading

from Engine.GUI import *
from Engine.EngineCaveBot import EngineCaveBot

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

DefaultScript = 'ratThais'
data = None


class CaveBot:
    def __init__(self, root, MapPositions, BattlePositions, SQMs, MOUSE_OPTION, HOOK_OPTION):
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
        CheckHotkeyPause = tk.BooleanVar()
        CheckHotkeyPause.set(True)
        HotkeyToPause = tk.StringVar()
        HotkeyToPause.set('Page Up')
        Script = tk.StringVar()
        Script.set(DefaultScript)

        BackImage = 'images/Fundo.png'
        Back = self.CaveBot.openImage(BackImage, [210, 60])
        Back2 = self.CaveBot.openImage(BackImage, [210, 100])

        self.CaveBot.addButton('Ok', self.CaveBot.destroyWindow, [74, 22], [378, 601])

        global EnabledCaveBot
        if not EnabledCaveBot:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: OFF', SetCaveBot, [810, 26], [10, 570])
        else:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: ON', SetCaveBot, [810, 26], [10, 570])

        CheckboxDebugging = self.CaveBot.addCheck(CheckDebugging, [434, 484], 0, "Enable Cavebot Debugging")

        CheckboxHotkeyPause = self.CaveBot.addCheck(CheckHotkeyPause, [434, 526], 1,
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

        # region Variables MonsterAttacking

        PriorityOne = tk.IntVar()
        PriorityOne.set(priority[0])
        PriorityTwo = tk.IntVar()
        PriorityTwo.set(priority[1])
        PriorityThree = tk.IntVar()
        PriorityThree.set(priority[2])
        PriorityFour = tk.IntVar()
        PriorityFour.set(priority[3])

        SelectedMonster = tk.StringVar()
        SelectedMonster.set(monsters[0])
        SelectedMonster2 = tk.StringVar()
        SelectedMonster2.set(monsters[1])
        SelectedMonster3 = tk.StringVar()
        SelectedMonster3.set(monsters[2])
        SelectedMonster4 = tk.StringVar()
        SelectedMonster4.set(monsters[3])
        SelectedAttackMode = tk.StringVar()
        SelectedAttackMode.set(AttackModes[0])

        CheckAttackOne = tk.BooleanVar()
        CheckAttackOne.set(True)
        CheckAttackTwo = tk.BooleanVar()
        CheckAttackTwo.set(False)
        CheckAttackThree = tk.BooleanVar()
        CheckAttackThree.set(False)
        CheckAttackFour = tk.BooleanVar()
        CheckAttackFour.set(False)
        CheckFollow = tk.BooleanVar()
        CheckCantAttack = tk.BooleanVar()
        CheckAttackPlayers = tk.BooleanVar()
        CheckPlayerSeen = tk.BooleanVar()
        CheckAttackingYou = tk.BooleanVar()
        CheckForceAttack = tk.BooleanVar()

        SuspendAfter = tk.StringVar()
        SuspendAfter.set('15')
        MonstersRange = tk.StringVar()
        MonstersRange.set('6')

        # endregion

        # region Variables Walker

        RadioCavebotMode = tk.IntVar()
        RadioCavebotMode.set(0)
        Radius = tk.StringVar()
        Radius.set('1')
        Delay = tk.StringVar()
        Delay.set('0')
        Waypoint_X = tk.StringVar() # Lembrar de setar posição atual do player
        Waypoint_X.set('32350')
        Waypoint_Y = tk.StringVar() # Lembrar de setar posição atual do player
        Waypoint_Y.set('32219')
        Waypoint_Z = tk.StringVar() # Lembrar de setar posição atual do player
        Waypoint_Z.set('6')
        Stand = tk.StringVar()
        Stand.set('2')
        ResearchMap = tk.BooleanVar()
        ResearchMap.set(True)

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
        RadioMarkValue.set(1)

        # endregion

        # region Variables DepotWalker

        CheckDropItems = tk.BooleanVar()
        CheckDropItems.set(True)
        LoadAutoSeller = tk.BooleanVar()
        LoadAutoSeller.set(True)
        LoadAutoBanker = tk.BooleanVar()
        LoadAutoBanker.set(True)
        LoadSortLoot = tk.BooleanVar()
        LoadSortLoot.set(True)

        CapBelowThan = tk.StringVar()
        CapBelowThan.set('150')

        # endregion

        # region Variables CorpseLooting

        CheckLootWhileKilling = tk.BooleanVar()
        CheckLootWhileKilling.set(True)
        CheckTibiaCustomLoot = tk.BooleanVar()
        CheckTibiaCustomLoot.set(True)
        CheckSQM1 = tk.StringVar()
        CheckSQM1.set(True)
        CheckSQM2 = tk.StringVar()
        CheckSQM2.set(True)
        CheckSQM3 = tk.StringVar()
        CheckSQM3.set(True)
        CheckSQM4 = tk.StringVar()
        CheckSQM4.set(True)
        CheckSQM5 = tk.StringVar()
        CheckSQM5.set(True)
        CheckSQM6 = tk.StringVar()
        CheckSQM6.set(True)
        CheckSQM7 = tk.StringVar()
        CheckSQM7.set(True)
        CheckSQM8 = tk.StringVar()
        CheckSQM8.set(True)
        CheckSQM9 = tk.StringVar()
        CheckSQM9.set(True)

        CapLimit = tk.StringVar()
        CapLimit.set('50')

        # endregion

        # region GUI MonsterAttacking

        OptionAttackMode = self.CaveBot.addOption(SelectedAttackMode, AttackModes, [103, 328], 10)

        CheckboxAttackOne = self.CaveBot.addCheck(CheckAttackOne, [25, 40], 1, 'Monster One')
        OptionMonstersOne = self.CaveBot.addOption(SelectedMonster, monsters, [155, 40], 16)
        PriorityMonstersOne = self.CaveBot.addOption(PriorityOne, priority, [300, 40])

        CheckboxAttackTwo = self.CaveBot.addCheck(CheckAttackTwo, [25, 80], 0, 'Monster Two')
        OptionMonstersTwo = self.CaveBot.addOption(SelectedMonster2, monsters, [155, 80], 16)
        PriorityMonstersTwo = self.CaveBot.addOption(PriorityTwo, priority, [300, 80])

        CheckboxAttackThree = self.CaveBot.addCheck(CheckAttackThree, [25, 120], 0, 'Monster Three')
        OptionMonstersThree = self.CaveBot.addOption(SelectedMonster3, monsters, [155, 120], 16)
        PriorityMonstersThree = self.CaveBot.addOption(PriorityThree, priority, [300, 120])

        CheckboxAttackFour = self.CaveBot.addCheck(CheckAttackFour, [25, 160], 0, 'Monster Four')
        OptionMonstersFour = self.CaveBot.addOption(SelectedMonster4, monsters, [155, 160], 16)
        PriorityMonstersFour = self.CaveBot.addOption(PriorityFour, priority, [300, 160])

        CheckBoxFollow = self.CaveBot.addCheck(CheckFollow, [20, 200], 1, 'Auto Follow Mode')
        CheckBoxCantAttack = self.CaveBot.addCheck(CheckCantAttack, [20, 220], 1, "Suspend When Can't Attack")
        CheckBoxAttackPlayers = self.CaveBot.addCheck(CheckAttackPlayers, [20, 240], 1, "Don't Attack Players")
        CheckBoxPlayerSeen = self.CaveBot.addCheck(CheckPlayerSeen, [195, 200], 1, 'Reduced Attack When Player Seen')
        CheckBoxAttackingYou = self.CaveBot.addCheck(CheckAttackingYou, [183, 240], 0, 'Attack Only Monsters Attacking You')
        CheckBoxForceAttack = self.CaveBot.addCheck(CheckForceAttack, [195, 220], 0, 'Force Attack When Attacked')

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

        CheckboxDropItems = self.CaveBot.addCheck(CheckDropItems, [425, 28], 1, 'Drop Items Instead Of Deposit')
        LabelGoDepot = self.CaveBot.addLabel('Go To Depot When Cap Below Than:', [480, 50])

        EntryCapBelowThan = self.CaveBot.addEntry([680, 50], CapBelowThan, 5)

        ButtonAutoSeller = self.CaveBot.addButton('Load AutoSeller', SetLoadAutoSeller, [110, 28], [450, 80])
        ButtonAutoBanker = self.CaveBot.addButton('Load AutoBanker', SetLoadAutoBanker, [120, 28], [570, 80])
        ButtonSortLoot = self.CaveBot.addButton('Load SortLoot', SetLoadSortLoot, [100, 28], [700, 80])

        # endregion

        # region GUI CorpseLooting

        LabelCapLimit = self.CaveBot.addLabel('Loot Capacity Limit:', [435, 150])
        EntryCapLimit = self.CaveBot.addEntry([551, 148], CapLimit, 5)

        CheckBoxLootWhileKilling = self.CaveBot.addCheck(CheckLootWhileKilling, [435, 180], 1, 'Loot While Killing')
        CheckBoxTibiaCustomLoot = self.CaveBot.addCheck(CheckTibiaCustomLoot, [585, 180], 1, 'Loot From Tibia Custom Loot')

        LabelLootAround = self.CaveBot.addLabel('Configure Loot Around:', [545, 220])

        CheckBoxSQM1 = self.CaveBot.addCheck(CheckSQM1, [570, 310], 1)
        CheckBoxSQM2 = self.CaveBot.addCheck(CheckSQM2, [600, 310], 1)
        CheckBoxSQM3 = self.CaveBot.addCheck(CheckSQM3, [630, 310], 1)
        CheckBoxSQM4 = self.CaveBot.addCheck(CheckSQM4, [570, 280], 1)
        CheckBoxSQM5 = self.CaveBot.addCheck(CheckSQM5, [600, 280], 1)
        CheckBoxSQM6 = self.CaveBot.addCheck(CheckSQM6, [630, 280], 1)
        CheckBoxSQM7 = self.CaveBot.addCheck(CheckSQM7, [570, 250], 1)
        CheckBoxSQM8 = self.CaveBot.addCheck(CheckSQM8, [600, 250], 1)
        CheckBoxSQM9 = self.CaveBot.addCheck(CheckSQM9, [630, 250], 1)

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

        self.CaveBot.loop()
