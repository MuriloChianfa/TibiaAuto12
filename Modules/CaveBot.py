import os
import json
import time
import threading

from Engine.GUI import *
from Engine.EngineCaveBot import EngineCaveBot
from Engine.SetGUI import SetGUI
from Engine.GUIManager import *

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

ImageMarks = []
NameMarks = [
    'CheckMark',
    'QuestionMark',
    'ExclimationMark',
    'Star',
    'Cross',
    'Church',
    'Mouth',
    'Shovel',
    'Sword',
    'Flag',
    'Lock',
    'Bag',
    'Skull',
    'Money',
    'ArrowUp',
    'ArrowDown',
    'ArrowRight',
    'ArrowLeft',
    'Above',
    'Bellow'
]


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
        InitiatedScript = self.Setter.GetVar("Script")
        Script.set(InitiatedScript)

        BackImage = 'images/Fundo.png'
        Back = self.CaveBot.openImage(BackImage, [210, 60])
        Back2 = self.CaveBot.openImage(BackImage, [210, 100])

        global EnabledCaveBot
        if not EnabledCaveBot:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: OFF', SetCaveBot, [810, 26], [10, 570])
        else:
            ButtonEnabled = self.CaveBot.addButton('CaveBot: ON', SetCaveBot, [810, 26], [10, 570])

        CheckboxDebugging = self.CaveBot.addCheck(CheckDebugging, [22, 511], InitiatedDebugging, "Enable Cavebot Debugging")

        CheckboxHotkeyPause = self.CaveBot.addCheck(CheckHotkeyPause, [22, 542], InitiatedHotkeyPause,
                                                    'Enable Hotkey To Break a  Cavebot')
        CheckboxHotkeyPause.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                      selectcolor=rgb((114, 94, 48)))

        ButtonHotkeyPause = self.CaveBot.addOption(HotkeyToPause, Hotkeys, [232, 542], 8)

        # region Functions Walker

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
            print('Clicked On Remove Waypoint: XXXXX')

        def AddWalker():
            print('Clicked On Add Waypoint:', RadioMarkValue.get(), "With Type:", RadioTypeValue.get())

        MarkDecoder = {
            'CheckMark': 0,
            'QuestionMark': 1,
            'ExclimationMark': 2,
            'Star': 3,
            'Cross': 4,
            'Church': 5,
            'Mouth': 6,
            'Shovel': 7,
            'Sword': 8,
            'Flag': 9,
            'Lock': 10,
            'Bag': 11,
            'Skull': 12,
            'Money': 13,
            'ArrowUp': 14,
            'ArrowDown': 15,
            'ArrowRight': 16,
            'ArrowLeft': 17,
            'Above': 18,
            'Bellow': 19
        }

        TypeDecoder = {
            1: "Walk",
            2: "Rope",
            3: "Shovel"
        }

        def LoadScript():
            GetScript = Script.get()
            print("\nLoading Script:", GetScript + ".json")
            if os.path.isfile('Scripts/' + GetScript + '.json'):
                print(f"\nThe File {GetScript}.json Exist... Loading Them")
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)
                    for j in range(len(DataMark)):
                        if DataMark[j]['status']:
                            PreviousMarkData = DataMark[j - 1]['mark']
                            PreviousWaypoint.configure(text=PreviousMarkData)
                            PreviousImage.configure(image=ImageMarks[MarkDecoder.get(PreviousMarkData)])
                            PreviousType.configure(text=TypeDecoder.get(DataMark[j - 1]['type']))

                            CurrentMarkData = DataMark[j]['mark']
                            CurrentWaypoint.configure(text=CurrentMarkData)
                            CurrentImage.configure(image=ImageMarks[MarkDecoder.get(CurrentMarkData)])
                            CurrentType.configure(text=TypeDecoder.get(DataMark[j]['type']))

                            NextMarkData = DataMark[j + 1]['mark']
                            NextWaypoint.configure(text=NextMarkData)
                            NextImage.configure(image=ImageMarks[MarkDecoder.get(NextMarkData)])
                            NextType.configure(text=TypeDecoder.get(DataMark[j + 1]['type']))
            else:
                print(f"\nThe File {GetScript}.json Not Exist... Please Enter With a Valid Script Name")

        def SaveScript():
            print("clicked on savescript")

        def CheckMarkClick():
            return 0

        def ResetMarks():
            GetScript = Script.get()
            if os.path.isfile('Scripts/' + GetScript + '.json'):
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)
                    for j in range(len(DataMark)):
                        if DataMark[j]['status']:
                            DataMark[j]['status'] = False
                    DataMark[0]['status'] = True
                    with open('Scripts/' + GetScript + '.json', 'w') as wJson:
                        json.dump(DataMark, wJson, indent=4)
                    print(f"{GetScript}.json Reseted !!")
        # endregion

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
            CheckingGUI(InitiatedEnableWalking, CheckEnableWalking.get(), 'EnableWalking')
            CheckingGUI(InitiatedTypeValue, RadioTypeValue.get(), 'TypeValue')
            CheckingGUI(InitiatedStand, Stand.get(), 'Stand')
            CheckingGUI(InitiatedResearchMap, ResearchMap.get(), 'ResearchMap')
            CheckingGUI(InitiatedMarkValue, RadioMarkValue.get(), 'MarkValue')
            CheckingGUI(InitiatedDropItems, CheckDropItems.get(), 'DropItems')
            CheckingGUI(InitiatedLoadAutoSeller, LoadAutoSeller.get(), 'LoadAutoSeller')
            CheckingGUI(InitiatedLoadAutoBanker, LoadAutoBanker.get(), 'LoadAutoBanker')
            CheckingGUI(InitiatedLoadSortLoot, LoadSortLoot.get(), 'LoadSortLoot')
            CheckingGUI(InitiatedCapBelowThan, CapBelowThan.get(), 'CapBelowThan')
            CheckingGUI(InitiatedScript, Script.get(), 'Script')

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

        Stand = tk.StringVar()
        InitiatedStand = self.Setter.GetVar("Stand")
        Stand.set(InitiatedStand)

        ResearchMap = tk.BooleanVar()
        InitiatedResearchMap = self.Setter.GetBoolVar("ResearchMap")
        ResearchMap.set(InitiatedResearchMap)

        for i in range(len(NameMarks)):
            ImageMark = Image.open('images/MapSettings/' + NameMarks[i] + '.png')
            ImageMark = ImageMark.resize((20, 20), Image.ANTIALIAS)
            ImageMark = ImageTk.PhotoImage(ImageMark)
            ImageMarks.append(ImageMark)

        RadioMarkValue = tk.IntVar()
        InitiatedMarkValue = self.Setter.GetVar("MarkValue")
        RadioMarkValue.set(InitiatedMarkValue)

        RadioTypeValue = tk.IntVar()
        InitiatedTypeValue = self.Setter.GetVar("TypeValue")
        RadioTypeValue.set(InitiatedTypeValue)

        CheckEnableWalking = tk.BooleanVar()
        InitiatedEnableWalking = self.Setter.GetBoolVar("EnableWalking")
        CheckEnableWalking.set(InitiatedResearchMap)

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
        CheckboxEnableWalking = self.CaveBot.addCheck(CheckEnableWalking, [560, 142], InitiatedEnableWalking,
                                                      'Enable Walking')

        self.CaveBot.addLabel("Script Name:", [430, 160])
        EntryCurrentScript = self.CaveBot.addEntry([440, 185], Script, 22)
        ButtonLoadScript = self.CaveBot.addButton('Load Script', LoadScript, [110, 30], [590, 176])
        ButtonSaveScript = self.CaveBot.addButton('Save Script', SaveScript, [100, 30], [710, 176])

        self.CaveBot.addLabel('Marks:', [431, 210])

        RadioImage1 = self.CaveBot.addRadioImage('', RadioMarkValue, 1, [470, 230], CheckMarkClick, ImageMarks[0])
        RadioImage2 = self.CaveBot.addRadioImage('', RadioMarkValue, 2, [510, 230], CheckMarkClick, ImageMarks[1])
        RadioImage3 = self.CaveBot.addRadioImage('', RadioMarkValue, 3, [550, 230], CheckMarkClick, ImageMarks[2])
        RadioImage4 = self.CaveBot.addRadioImage('', RadioMarkValue, 4, [590, 230], CheckMarkClick, ImageMarks[3])
        RadioImage5 = self.CaveBot.addRadioImage('', RadioMarkValue, 5, [630, 230], CheckMarkClick, ImageMarks[4])
        RadioImage6 = self.CaveBot.addRadioImage('', RadioMarkValue, 6, [670, 230], CheckMarkClick, ImageMarks[5])
        RadioImage7 = self.CaveBot.addRadioImage('', RadioMarkValue, 7, [710, 230], CheckMarkClick, ImageMarks[6])
        RadioImage8 = self.CaveBot.addRadioImage('', RadioMarkValue, 8, [470, 260], CheckMarkClick, ImageMarks[7])
        RadioImage9 = self.CaveBot.addRadioImage('', RadioMarkValue, 9, [510, 260], CheckMarkClick, ImageMarks[8])
        RadioImage10 = self.CaveBot.addRadioImage('', RadioMarkValue, 10, [550, 260], CheckMarkClick, ImageMarks[9])
        RadioImage11 = self.CaveBot.addRadioImage('', RadioMarkValue, 11, [590, 260], CheckMarkClick, ImageMarks[10])
        RadioImage12 = self.CaveBot.addRadioImage('', RadioMarkValue, 12, [630, 260], CheckMarkClick, ImageMarks[11])
        RadioImage13 = self.CaveBot.addRadioImage('', RadioMarkValue, 13, [670, 260], CheckMarkClick, ImageMarks[12])
        RadioImage14 = self.CaveBot.addRadioImage('', RadioMarkValue, 14, [710, 260], CheckMarkClick, ImageMarks[13])
        RadioImage15 = self.CaveBot.addRadioImage('', RadioMarkValue, 15, [470, 290], CheckMarkClick, ImageMarks[14])
        RadioImage16 = self.CaveBot.addRadioImage('', RadioMarkValue, 16, [510, 290], CheckMarkClick, ImageMarks[15])
        RadioImage17 = self.CaveBot.addRadioImage('', RadioMarkValue, 17, [550, 290], CheckMarkClick, ImageMarks[16])
        RadioImage18 = self.CaveBot.addRadioImage('', RadioMarkValue, 18, [590, 290], CheckMarkClick, ImageMarks[17])
        RadioImage19 = self.CaveBot.addRadioImage('', RadioMarkValue, 19, [630, 290], CheckMarkClick, ImageMarks[18])
        RadioImage20 = self.CaveBot.addRadioImage('', RadioMarkValue, 20, [670, 290], CheckMarkClick, ImageMarks[19])

        self.CaveBot.addLabel('Type Of Waypoint:', [470, 325])

        RadioWalk = self.CaveBot.addRadio('Walk', RadioTypeValue, 1, [580, 324])
        RadioRope = self.CaveBot.addRadio('Rope', RadioTypeValue, 2, [635, 324])
        RadioShovel = self.CaveBot.addRadio('Shovel', RadioTypeValue, 3, [690, 324])

        ButtonRemoveWalker = self.CaveBot.addButton("Remove", RemoveWalker, [70, 21], [615, 355])
        ButtonAddWalker = self.CaveBot.addButton("Add", AddWalker, [50, 21], [555, 355])

        self.CaveBot.addLabel('Waypoints In Current Script:', [431, 385])

        ButtonResetMarks = self.CaveBot.addButton('Reset Marks', ResetMarks, [100, 24], [701, 385])

        self.CaveBot.addLabel("PreviousWaypoint:", [431, 415])
        self.CaveBot.addLabel("CurrentWaypoint:", [570, 415])
        self.CaveBot.addLabel("NextWaypoint:", [720, 415])

        PreviousWaypoint = self.CaveBot.addLabel("", [435, 435])
        CurrentWaypoint = self.CaveBot.addLabel("", [574, 435])
        NextWaypoint = self.CaveBot.addLabel("", [724, 435])

        PreviousImage = self.CaveBot.addImage(None, [465, 460])
        CurrentImage = self.CaveBot.addImage(None, [614, 460])
        NextImage = self.CaveBot.addImage(None, [754, 460])

        self.CaveBot.addLabel("Type:", [431, 485])
        self.CaveBot.addLabel("Type:", [580, 485])
        self.CaveBot.addLabel("Type:", [720, 485])

        PreviousType = self.CaveBot.addLabel("", [463, 485])
        CurrentType = self.CaveBot.addLabel("", [612, 485])
        NextType = self.CaveBot.addLabel("", [752, 485])

        LabelStand = self.CaveBot.addLabel('Stand Still After Reaching Waypoint Per:', [431, 520])

        EntryStand = self.CaveBot.addEntry([653, 521], Stand, 2)
        Stand.trace("w", ValidateStand)

        ButtonResearchMap = self.CaveBot.addButton('Auto Research Map', SetResearchMap, [130, 37], [684, 519])

        # endregion

        # region GUI DepotWalker

        CheckboxDropItems = self.CaveBot.addCheck(CheckDropItems, [425, 28], InitiatedDropItems, 'Drop Items Instead Of Deposit')
        LabelGoDepot = self.CaveBot.addLabel('Go To Depot When Cap Below Than:', [480, 50])

        EntryCapBelowThan = self.CaveBot.addEntry([680, 50], CapBelowThan, 5)

        ButtonAutoSeller = self.CaveBot.addButton('Load AutoSeller', SetLoadAutoSeller, [110, 28], [450, 80])
        ButtonAutoBanker = self.CaveBot.addButton('Load AutoBanker', SetLoadAutoBanker, [120, 28], [570, 80])
        ButtonSortLoot = self.CaveBot.addButton('Load SortLoot', SetLoadSortLoot, [100, 28], [700, 80])

        # endregion

        def CheckingButtons():
            if EnabledCaveBot:
                Disable(CheckboxDebugging)
                Disable(CheckboxHotkeyPause)
                Disable(ButtonHotkeyPause)

                Disable(OptionAttackMode)
                Disable(CheckboxAttackOne)
                Disable(OptionMonstersOne)
                Disable(PriorityMonstersOne)
                Disable(CheckboxAttackTwo)
                Disable(OptionMonstersTwo)
                Disable(PriorityMonstersTwo)
                Disable(CheckboxAttackThree)
                Disable(OptionMonstersThree)
                Disable(PriorityMonstersThree)
                Disable(CheckboxAttackFour)
                Disable(OptionMonstersFour)
                Disable(PriorityMonstersFour)
                Disable(CheckBoxFollow)
                Disable(CheckBoxCantAttack)
                Disable(CheckBoxAttackPlayers)
                Disable(CheckBoxPlayerSeen)
                Disable(CheckBoxAttackingYou)
                Disable(CheckBoxForceAttack)
                Disable(LabelSuspendAfter)
                Disable(LabelMonstersRange)
                Disable(LabelAttackMode)
                Disable(EntrySuspendAfter)
                Disable(EntryMonstersRange)

                Disable(LabelStand)

                Disable(CheckboxDropItems)
                Disable(LabelGoDepot)
                Disable(EntryCapBelowThan)
                Disable(ButtonAutoSeller)
                Disable(ButtonAutoBanker)
                Disable(ButtonSortLoot)
            else:
                Enable(CheckboxDebugging)
                Enable(CheckboxDebugging)
                Enable(CheckboxHotkeyPause)
                Enable(ButtonHotkeyPause)

                Enable(OptionAttackMode)
                Enable(CheckboxAttackOne)
                Enable(CheckboxAttackTwo)
                Enable(CheckboxAttackThree)
                Enable(CheckboxAttackFour)
                if not CheckAttackOne.get():
                    Disable(OptionMonstersOne)
                    Disable(PriorityMonstersOne)
                else:
                    Enable(OptionMonstersOne)
                    Enable(PriorityMonstersOne)
                if not CheckAttackTwo.get():
                    Disable(OptionMonstersTwo)
                    Disable(PriorityMonstersTwo)
                else:
                    Enable(OptionMonstersTwo)
                    Enable(PriorityMonstersTwo)
                if not CheckAttackThree.get():
                    Disable(OptionMonstersThree)
                    Disable(PriorityMonstersThree)
                else:
                    Enable(OptionMonstersThree)
                    Enable(PriorityMonstersThree)
                if not CheckAttackFour.get():
                    Disable(OptionMonstersFour)
                    Disable(PriorityMonstersFour)
                else:
                    Enable(OptionMonstersFour)
                    Enable(PriorityMonstersFour)
                Enable(CheckBoxFollow)
                Enable(CheckBoxCantAttack)
                Enable(CheckBoxAttackPlayers)
                Enable(CheckBoxPlayerSeen)
                Enable(CheckBoxAttackingYou)
                Enable(CheckBoxForceAttack)
                Enable(LabelSuspendAfter)
                Enable(LabelMonstersRange)
                Enable(LabelAttackMode)
                Enable(EntrySuspendAfter)
                Enable(EntryMonstersRange)
                Enable(LabelStand)

                Enable(CheckboxDropItems)
                if CheckDropItems.get():
                    Disable(LabelGoDepot)
                    Disable(EntryCapBelowThan)
                    Disable(ButtonAutoSeller)
                    Disable(ButtonAutoBanker)
                    Disable(ButtonSortLoot)
                else:
                    Enable(LabelGoDepot)
                    Enable(EntryCapBelowThan)
                    Enable(ButtonAutoSeller)
                    Enable(ButtonAutoBanker)
                    Enable(ButtonSortLoot)

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
                    Disable(OptionMonstersOne)
                    Disable(PriorityMonstersOne)
                else:
                    Enable(OptionMonstersOne)
                    Enable(PriorityMonstersOne)
                if not CheckAttackTwo.get():
                    Disable(OptionMonstersTwo)
                    Disable(PriorityMonstersTwo)
                else:
                    Enable(OptionMonstersTwo)
                    Enable(PriorityMonstersTwo)
                if not CheckAttackThree.get():
                    Disable(OptionMonstersThree)
                    Disable(PriorityMonstersThree)
                else:
                    Enable(OptionMonstersThree)
                    Enable(PriorityMonstersThree)
                if not CheckAttackFour.get():
                    Disable(OptionMonstersFour)
                    Disable(PriorityMonstersFour)
                else:
                    Enable(OptionMonstersFour)
                    Enable(PriorityMonstersFour)
                if CheckDropItems.get():
                    Disable(LabelGoDepot)
                    Disable(EntryCapBelowThan)
                    Disable(ButtonAutoSeller)
                    Disable(ButtonAutoBanker)
                    Disable(ButtonSortLoot)
                else:
                    Enable(LabelGoDepot)
                    Enable(EntryCapBelowThan)
                    Enable(ButtonAutoSeller)
                    Enable(ButtonAutoBanker)
                    Enable(ButtonSortLoot)
                if not CheckHotkeyPause.get():
                    Disable(ButtonHotkeyPause)
                elif CheckHotkeyPause.get():
                    Enable(ButtonHotkeyPause)
                if not CheckEnableWalking.get():
                    Disable(EntryCurrentScript)
                    Disable(ButtonLoadScript)
                    Disable(ButtonSaveScript)
                    Disable(RadioImage1)
                    Disable(RadioImage2)
                    Disable(RadioImage3)
                    Disable(RadioImage4)
                    Disable(RadioImage5)
                    Disable(RadioImage6)
                    Disable(RadioImage7)
                    Disable(RadioImage8)
                    Disable(RadioImage9)
                    Disable(RadioImage10)
                    Disable(RadioImage11)
                    Disable(RadioImage12)
                    Disable(RadioImage13)
                    Disable(RadioImage14)
                    Disable(RadioImage15)
                    Disable(RadioImage16)
                    Disable(RadioImage17)
                    Disable(RadioImage18)
                    Disable(RadioImage19)
                    Disable(RadioImage20)
                    Disable(ButtonRemoveWalker)
                    Disable(ButtonAddWalker)
                    Disable(ButtonResetMarks)
                    Disable(PreviousImage)
                    Disable(CurrentImage)
                    Disable(NextImage)
                    Disable(EntryStand)
                    Disable(ButtonResearchMap)
                    Disable(RadioWalk)
                    Disable(RadioRope)
                    Disable(RadioShovel)
                else:
                    Enable(EntryCurrentScript)
                    Enable(ButtonLoadScript)
                    Enable(ButtonSaveScript)
                    Enable(RadioImage1)
                    Enable(RadioImage2)
                    Enable(RadioImage3)
                    Enable(RadioImage4)
                    Enable(RadioImage5)
                    Enable(RadioImage6)
                    Enable(RadioImage7)
                    Enable(RadioImage8)
                    Enable(RadioImage9)
                    Enable(RadioImage10)
                    Enable(RadioImage11)
                    Enable(RadioImage12)
                    Enable(RadioImage13)
                    Enable(RadioImage14)
                    Enable(RadioImage15)
                    Enable(RadioImage16)
                    Enable(RadioImage17)
                    Enable(RadioImage18)
                    Enable(RadioImage19)
                    Enable(RadioImage20)
                    Enable(ButtonRemoveWalker)
                    Enable(ButtonAddWalker)
                    Enable(ButtonResetMarks)
                    Enable(PreviousImage)
                    Enable(CurrentImage)
                    Enable(NextImage)
                    Enable(EntryStand)
                    Enable(ButtonResearchMap)
                    Enable(RadioWalk)
                    Enable(RadioRope)
                    Enable(RadioShovel)

            ExecGUITrigger()

            self.CaveBot.After(200, ConstantVerify)

        CheckingButtons()
        ConstantVerify()

        self.CaveBot.Protocol(Destroy)
        self.CaveBot.loop()
