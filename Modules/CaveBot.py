import os
import json
import time
import shutil
import threading

from Conf.MarksConf import *
from Conf.Constants import Monsters, Priority, Hotkeys, AttackModes

from Core.GUI import *
from Core.GUIManager import *
from Core.GUISetter import GUISetter
# from Core.ThreadManager import ThreadManager

from Engine.EngineCaveBot import EngineCaveBot

GUIChanges = []

EnabledCaveBot = False
LoadedScript = False


class CaveBot:
    def __init__(self, MapPositions, BattlePositions, SQMs, MOUSE_OPTION):
        self.CaveBot = GUI('CaveBot', 'Module: Cave Bot')
        self.CaveBot.DefaultWindow('CaveBot', [830, 634], [1.2, 2.29])
        self.Setter = GUISetter("CaveBotLoader")
        # self.ThreadManager = ThreadManager("CaveBot")

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
            # self.ThreadManager.StartNewThread(ScanCaveBot)
            try:
                ThreadCaveBot = threading.Thread(target=ScanCaveBot)
                ThreadCaveBot.start()
            except:
                print("Error: Unable To Start ThreadCaveBot!")

        def ScanCaveBot():
            with open('Scripts/' + Script.get() + '.json', 'r') as rJson:
                data = json.load(rJson)
            print("The Script " + Script.get() + ".json Have a", len(data), "Marks")

            monster = SelectedMonster.get()
            while EnabledCaveBot:
                for a in range(len(data)):
                    EngineCaveBot(data, a, MapPositions, BattlePositions, monster, SQMs, MOUSE_OPTION, Script.get())
                    time.sleep(1)

        CheckDebugging, InitiatedDebugging = self.Setter.Variables.Bool('Debugging')

        CheckHotkeyPause, InitiatedHotkeyPause = self.Setter.Variables.Bool('HotkeyPause')
        HotkeyToPause, InitiatedHotkeyToPause = self.Setter.Variables.Str('HotkeyToPause')

        Script, InitiatedScript = self.Setter.Variables.Str('Script')

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
            global LoadedScript
            if not LoadedScript:
                LoadScript()

            GetScript = Script.get()

            with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                DataMark = json.load(MarksJson)

            MarkedMark = 99999

            for k in range(len(DataMark)):
                if DataMark[k]['status']:
                    DataMark[k]['status'] = False
                    del DataMark[k]
                    with open('Scripts/' + GetScript + '.json', 'w') as wJson:
                        json.dump(DataMark, wJson, indent=4)
                    MarkedMark = k
                    break

            if MarkedMark != 99999:
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)
                if MarkedMark - 1 >= len(DataMark):
                    DataMark[-1]['status'] = True
                else:
                    DataMark[MarkedMark - 1]['status'] = True
                with open('Scripts/' + GetScript + '.json', 'w') as wJson:
                    json.dump(DataMark, wJson, indent=4)
            LoadScript()

        def AddWalker():
            global LoadedScript
            if not LoadedScript:
                LoadScript()
                time.sleep(.1)

            MarkToAdd = MarkEncoder.get(RadioMarkValue.get())
            TypeToAdd = RadioTypeValue.get()

            with open('Scripts/' + Script.get() + '.json', 'r') as MarksJson:
                DataMark = json.load(MarksJson)

            MarkedMark = 99999

            print(len(DataMark))

            if DataMark[0]['status'] == "NotConfigured":
                DataMark.insert(0, {"mark": MarkToAdd, "type": TypeToAdd, "status": True})
                del DataMark[1]
                with open('Scripts/' + Script.get() + '.json', 'w') as wJson:
                    json.dump(DataMark, wJson, indent=4)

                LoadCurrent(DataMark, 0)
            else:
                for j in range(len(DataMark)):
                    if DataMark[j]['status']:

                        DataMark.insert(j + 1, {"mark": MarkToAdd, "type": TypeToAdd, "status": False})
                        with open('Scripts/' + Script.get() + '.json', 'w') as wJson:
                            json.dump(DataMark, wJson, indent=4)
                        DataMark[j]['status'] = False
                        MarkedMark = j

                if MarkedMark != 99999:
                    if MarkedMark + 1 >= len(DataMark):
                        DataMark[0]['status'] = True
                    else:
                        DataMark[MarkedMark + 1]['status'] = True
                    with open('Scripts/' + Script.get() + '.json', 'w') as wJson:
                        json.dump(DataMark, wJson, indent=4)

                LoadScript()

                print("\n" + MarkToAdd, "Added With Type:", TypeDecoder.get(TypeToAdd), "On Index Position:", MarkedMark + 2,
                      "Of Your Script")

        def LoadPrevious(DataMark, index):
            if DataMark[index] == DataMark[0]:
                PreviousMarkData = DataMark[-1]['mark']
            else:
                PreviousMarkData = DataMark[index - 1]['mark']
            PreviousWaypoint.configure(text=PreviousMarkData)

            PreviousImage.configure(image=ImageMarks[MarkDecoder.get(PreviousMarkData) - 1])

            if DataMark[index] == DataMark[0]:
                PreviousTypeData = DataMark[-1]['type']
            else:
                PreviousTypeData = DataMark[index - 1]['type']
            PreviousType.configure(text=TypeDecoder.get(PreviousTypeData))

        def LoadCurrent(DataMark, index):
            CurrentMarkData = DataMark[index]['mark']
            CurrentWaypoint.configure(text=CurrentMarkData)
            CurrentImage.configure(image=ImageMarks[MarkDecoder.get(CurrentMarkData) - 1])
            CurrentType.configure(text=TypeDecoder.get(DataMark[index]['type']))

        def LoadNext(DataMark, index):
            if DataMark[index] == DataMark[-1]:
                NextMarkData = DataMark[0]['mark']
            else:
                NextMarkData = DataMark[index + 1]['mark']
            NextWaypoint.configure(text=NextMarkData)

            NextImage.configure(image=ImageMarks[MarkDecoder.get(NextMarkData) - 1])

            if DataMark[index] == DataMark[-1]:
                NextTypeData = DataMark[0]['type']
            else:
                NextTypeData = DataMark[index + 1]['type']
            NextType.configure(text=TypeDecoder.get(NextTypeData))

        def LoadScript():
            GetScript = Script.get()

            if os.path.isfile('Scripts/' + GetScript + '.json'):
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)

                if DataMark[0]['status'] == "NotConfigured":
                    pass
                else:
                    for j in range(len(DataMark)):
                        if DataMark[j]['status']:
                            LoadPrevious(DataMark, j)
                            LoadCurrent(DataMark, j)
                            LoadNext(DataMark, j)

                            global LoadedScript
                            LoadedScript = True
            else:
                # print(f"\nThe File {GetScript}.json Not Exist... Please Enter With a Valid Script Name")
                Directory = os.getcwd()

                shutil.copyfile(Directory + '\\Scripts' + '\\DefaultWalk.json',
                                os.path.join(Directory + '\\Scripts' + '\\' + Script.get() + '.json'))

                print("Script", Script.get() + ".json Created")

                PreviousWaypoint.configure(text="")
                PreviousImage.configure(image=Back)
                PreviousType.configure(text="")

                CurrentWaypoint.configure(text="")
                CurrentImage.configure(image=Back)
                CurrentType.configure(text="")

                NextWaypoint.configure(text="")
                NextImage.configure(image=Back)
                NextType.configure(text="")

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

                global LoadedScript
                LoadedScript = False
                LoadScript()

        def SelectNextWaypoint():
            global LoadedScript
            if LoadedScript:
                GetScript = Script.get()
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)
                MarkedMark = 99999
                for j in range(len(DataMark)):
                    if DataMark[j]['status']:
                        DataMark[j]['status'] = False
                        MarkedMark = j
                if MarkedMark != 99999:
                    if MarkedMark + 1 >= len(DataMark):
                        DataMark[0]['status'] = True
                    else:
                        DataMark[MarkedMark + 1]['status'] = True
                    with open('Scripts/' + GetScript + '.json', 'w') as wJson:
                        json.dump(DataMark, wJson, indent=4)
                LoadScript()
            else:
                print("Please Load Your Script First...")

        def SelectPreviousWaypoint():
            global LoadedScript
            if LoadedScript:
                GetScript = Script.get()
                with open('Scripts/' + GetScript + '.json', 'r') as MarksJson:
                    DataMark = json.load(MarksJson)
                MarkedMark = 99999
                for j in range(len(DataMark)):
                    if DataMark[j]['status']:
                        DataMark[j]['status'] = False
                        MarkedMark = j
                if MarkedMark != 99999:
                    if MarkedMark - 1 >= len(DataMark):
                        DataMark[-1]['status'] = True
                    else:
                        DataMark[MarkedMark - 1]['status'] = True
                    with open('Scripts/' + GetScript + '.json', 'w') as wJson:
                        json.dump(DataMark, wJson, indent=4)
                LoadScript()
            else:
                print("Please Load Your Script First...")

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
            CheckingGUI(InitiatedWalkForDebug, CheckWalkForDebug.get(), 'WalkForDebug')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.CaveBot.destroyWindow()

        # region Variables MonsterAttacking

        PriorityOne, InitiatedPriorityOne = self.Setter.Variables.Int('PriorityOne')
        PriorityTwo, InitiatedPriorityTwo = self.Setter.Variables.Int('PriorityTwo')
        PriorityThree, InitiatedPriorityThree = self.Setter.Variables.Int('PriorityThree')
        PriorityFour, InitiatedPriorityFour = self.Setter.Variables.Int('PriorityFour')

        SelectedMonster, InitiatedSelectedMonster = self.Setter.Variables.Str('SelectedMonster')
        SelectedMonster2, InitiatedSelectedMonster2 = self.Setter.Variables.Str('SelectedMonster2')
        SelectedMonster3, InitiatedSelectedMonster3 = self.Setter.Variables.Str('SelectedMonster3')
        SelectedMonster4, InitiatedSelectedMonster4 = self.Setter.Variables.Str('SelectedMonster4')

        SelectedAttackMode, InitiatedSelectedAttackMode = self.Setter.Variables.Str('SelectedAttackMode')
        CheckAttackOne, InitiatedAttackOne = self.Setter.Variables.Bool('AttackOne')
        CheckAttackTwo, InitiatedAttackTwo = self.Setter.Variables.Bool('AttackTwo')
        CheckAttackThree, InitiatedAttackThree = self.Setter.Variables.Bool('AttackThree')
        CheckAttackFour, InitiatedAttackFour = self.Setter.Variables.Bool('AttackFour')

        CheckFollow, InitiatedFollow = self.Setter.Variables.Bool('Follow')
        CheckCantAttack, InitiatedCantAttack = self.Setter.Variables.Bool('CantAttack')
        CheckAttackPlayers, InitiatedAttackPlayers = self.Setter.Variables.Bool('AttackPlayers')
        CheckPlayerSeen, InitiatedPlayerSeen = self.Setter.Variables.Bool('PlayerSeen')
        CheckAttackingYou, InitiatedAttackingYou = self.Setter.Variables.Bool('AttackingYou')
        CheckForceAttack, InitiatedForceAttack = self.Setter.Variables.Bool('ForceAttack')
        SuspendAfter, InitiatedSuspendAfter = self.Setter.Variables.Str('SuspendAfter')
        MonstersRange, InitiatedMonstersRange = self.Setter.Variables.Str('MonstersRange')

        # endregion

        # region Variables Walker

        BackImage = 'images/Fundo.png'
        Back = self.CaveBot.openImage(BackImage, [20, 20])

        RadioCavebotMode, InitiatedCavebotMode = self.Setter.Variables.Int('CavebotMode')

        Radius, InitiatedRadius = self.Setter.Variables.Str('Radius')
        Delay, InitiatedDelay = self.Setter.Variables.Str('Delay')
        Stand, InitiatedStand = self.Setter.Variables.Str('Stand')

        ResearchMap, InitiatedResearchMap = self.Setter.Variables.Bool('ResearchMap')

        CheckWalkForDebug, InitiatedWalkForDebug = self.Setter.Variables.Bool('WalkForDebug')

        for i in range(len(NameMarks)):
            ImageMark = Image.open('images/MapSettings/' + NameMarks[i] + '.png')
            ImageMark = ImageMark.resize((20, 20), Image.ANTIALIAS)
            ImageMark = ImageTk.PhotoImage(ImageMark)
            ImageMarks.append(ImageMark)

        RadioMarkValue, InitiatedMarkValue = self.Setter.Variables.Int('MarkValue')
        RadioTypeValue, InitiatedTypeValue = self.Setter.Variables.Int('TypeValue')

        CheckEnableWalking, InitiatedEnableWalking = self.Setter.Variables.Bool('EnableWalking')

        # endregion

        # region Variables DepotWalker

        CheckDropItems, InitiatedDropItems = self.Setter.Variables.Bool('DropItems')

        LoadAutoSeller, InitiatedLoadAutoSeller = self.Setter.Variables.Bool('LoadAutoSeller')
        LoadAutoBanker, InitiatedLoadAutoBanker = self.Setter.Variables.Bool('LoadAutoBanker')
        LoadSortLoot, InitiatedLoadSortLoot = self.Setter.Variables.Bool('LoadSortLoot')

        CapBelowThan, InitiatedCapBelowThan = self.Setter.Variables.Str('CapBelowThan')

        # endregion

        self.CaveBot.addButton('Ok', Destroy, [74, 22], [378, 601])

        # region GUI MonsterAttacking

        OptionAttackMode = self.CaveBot.addOption(SelectedAttackMode, AttackModes, [103, 328], 10)

        CheckboxAttackOne = self.CaveBot.addCheck(CheckAttackOne, [25, 40], InitiatedAttackOne, 'Monster One')
        OptionMonstersOne = self.CaveBot.addOption(SelectedMonster, Monsters, [155, 40], 16)
        PriorityMonstersOne = self.CaveBot.addOption(PriorityOne, Priority, [300, 40])

        CheckboxAttackTwo = self.CaveBot.addCheck(CheckAttackTwo, [25, 80], InitiatedAttackTwo, 'Monster Two')
        OptionMonstersTwo = self.CaveBot.addOption(SelectedMonster2, Monsters, [155, 80], 16)
        PriorityMonstersTwo = self.CaveBot.addOption(PriorityTwo, Priority, [300, 80])

        CheckboxAttackThree = self.CaveBot.addCheck(CheckAttackThree, [25, 120], InitiatedAttackThree, 'Monster Three')
        OptionMonstersThree = self.CaveBot.addOption(SelectedMonster3, Monsters, [155, 120], 16)
        PriorityMonstersThree = self.CaveBot.addOption(PriorityThree, Priority, [300, 120])

        CheckboxAttackFour = self.CaveBot.addCheck(CheckAttackFour, [25, 160], InitiatedAttackFour, 'Monster Four')
        OptionMonstersFour = self.CaveBot.addOption(SelectedMonster4, Monsters, [155, 160], 16)
        PriorityMonstersFour = self.CaveBot.addOption(PriorityFour, Priority, [300, 160])

        CheckBoxFollow = self.CaveBot.addCheck(CheckFollow, [20, 200], InitiatedFollow, 'Auto Follow Mode')
        CheckBoxCantAttack = self.CaveBot.addCheck(CheckCantAttack, [20, 220], InitiatedCantAttack,
                                                   "Suspend When Can't Attack")
        CheckBoxAttackPlayers = self.CaveBot.addCheck(CheckAttackPlayers, [20, 240], InitiatedAttackPlayers,
                                                      "Don't Attack Players")
        CheckBoxPlayerSeen = self.CaveBot.addCheck(CheckPlayerSeen, [195, 200], InitiatedPlayerSeen,
                                                   'Reduced Attack When Player Seen')
        CheckBoxAttackingYou = self.CaveBot.addCheck(CheckAttackingYou, [183, 240], InitiatedAttackingYou,
                                                     'Attack Only Monsters Attacking You')
        CheckBoxForceAttack = self.CaveBot.addCheck(CheckForceAttack, [195, 220], InitiatedForceAttack,
                                                    'Force Attack When Attacked')

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

        self.CaveBot.addLabel("PreviousWaypoint:", [431, 410])
        self.CaveBot.addLabel("CurrentWaypoint:", [570, 410])
        self.CaveBot.addLabel("NextWaypoint:", [720, 410])

        PreviousWaypoint = self.CaveBot.addLabel("", [435, 430])
        CurrentWaypoint = self.CaveBot.addLabel("", [574, 430])
        NextWaypoint = self.CaveBot.addLabel("", [724, 430])

        PreviousImage = self.CaveBot.addImage(None, [465, 455])
        CurrentImage = self.CaveBot.addImage(None, [614, 455])
        NextImage = self.CaveBot.addImage(None, [754, 455])

        self.CaveBot.addLabel("Type:", [431, 480])
        self.CaveBot.addLabel("Type:", [580, 480])
        self.CaveBot.addLabel("Type:", [720, 480])

        PreviousType = self.CaveBot.addLabel("", [463, 480])
        CurrentType = self.CaveBot.addLabel("", [612, 480])
        NextType = self.CaveBot.addLabel("", [752, 480])

        ButtonPreviousWaypoint = self.CaveBot.addButton('<<<', SelectPreviousWaypoint, [30, 21], [430, 456])
        ButtonNextWaypoint = self.CaveBot.addButton('>>>', SelectNextWaypoint, [30, 21], [786, 456])

        CheckboxWalkForDebug = self.CaveBot.addCheck(CheckWalkForDebug, [431, 497], InitiatedWalkForDebug,
                                                     "Enable Walk For Refresh Map (RECOMMENDED)")

        self.CaveBot.addLabel('Stand Still After Reaching Waypoint Per:', [431, 520])

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

                Disable(CheckboxDropItems)
                Disable(LabelGoDepot)
                Disable(EntryCapBelowThan)
                Disable(ButtonAutoSeller)
                Disable(ButtonAutoBanker)
                Disable(ButtonSortLoot)
                
                Disable(CheckboxEnableWalking)
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

                Disable(RadioWalk)
                Disable(RadioRope)
                Disable(RadioShovel)

                Disable(ButtonRemoveWalker)
                Disable(ButtonAddWalker)

                Disable(ButtonResetMarks)

                Disable(PreviousWaypoint)
                Disable(CurrentWaypoint)
                Disable(NextWaypoint)

                Disable(PreviousImage)
                Disable(CurrentImage)
                Disable(NextImage)

                Disable(PreviousType)
                Disable(CurrentType)
                Disable(NextType)

                Disable(EntryStand)
                Disable(CheckboxWalkForDebug)
                Disable(ButtonPreviousWaypoint)
                Disable(ButtonNextWaypoint)
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
                Enable(CheckboxEnableWalking)
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

                Enable(CheckboxDropItems)
                Enable(ButtonPreviousWaypoint)
                Enable(ButtonNextWaypoint)
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
                if CheckEnableWalking.get():
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

                    Enable(RadioWalk)
                    Enable(RadioRope)
                    Enable(RadioShovel)

                    Enable(ButtonRemoveWalker)
                    Enable(ButtonAddWalker)

                    Enable(ButtonResetMarks)

                    Enable(PreviousWaypoint)
                    Enable(CurrentWaypoint)
                    Enable(NextWaypoint)

                    Enable(PreviousImage)
                    Enable(CurrentImage)
                    Enable(NextImage)

                    Enable(PreviousType)
                    Enable(CurrentType)
                    Enable(NextType)

                    Enable(EntryStand)
                    Enable(CheckboxWalkForDebug)
                    
            ExecGUITrigger()

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
                    Disable(CheckboxWalkForDebug)
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
                    Enable(CheckboxWalkForDebug)
                ExecGUITrigger()

            self.CaveBot.After(200, ConstantVerify)

        CheckingButtons()
        ConstantVerify()

        if os.path.isfile('Scripts/' + Script.get() + '.json'):
            LoadScript()

        self.CaveBot.Protocol(Destroy)
        self.CaveBot.loop()
