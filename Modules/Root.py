import json

from Core.GUI import *

# from Modules.AdjustConfig import AdjustConfig
# from Modules.AmmoRestack import AmmoRestack
# from Modules.ShowMap import ShowMap
# from Modules.AutoBanker import AutoBanker
# from Modules.AutoFish import AutoFish
# from Modules.AutoGrouping import AutoGrouping
from Modules.AutoHeal import AutoHeal
from Modules.AutoHur import AutoHur
# from Modules.AutoLogin import AutoLogin
# from Modules.AutoLooter import AutoLooter
from Modules.AutoMana import AutoMana
from Modules.AutoRing import AutoRing
# from Modules.AutoSeller import AutoSeller
from Modules.AutoSSA import AutoSSA
from Modules.CaveBot import CaveBot
# from Modules.ColorChange import ColorChange
# from Modules.CreatureInfo import CreatureInfo
# from Modules.FoodEater import FoodEater
# from Modules.FPSChanger import FPSChanger
# from Modules.GeneralOptions import GeneralOptions
# from Modules.HealerFriend import HealerFriend
# from Modules.LoadConfig import LoadConfig
# from Modules.Modules import Modules
# from Modules.Monsters import Monsters
# from Modules.PythonScripts import PythonScripts
# from Modules.SaveConfig import SaveConfig
# from Modules.SortLoot import SortLoot
# from Modules.TimedSpells import TimedSpells


SETTED_VARIABLES = False
MOUSE_OPTION = None

ItemsSquare = 32

mark = [0, 0]
Player = [0, 0]
Target = [0, 0]
gameWindow = [0, 0, 0, 0]
ManaLocation = [0, 0]
MapPositions = [0, 0, 0, 0]
RingPositions = [0, 0, 0, 0]
StatsPositions = [0, 0, 0, 0]
HealthLocation = [0, 0]
BattlePositions = [0, 0, 0, 0]
AmuletPositions = [0, 0, 0, 0]
SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MainPath = None
ItemsPath = None
ChestsPath = None
ContainersNamePath = None
CavebotScriptsPath = None



class root:
    def __init__(self, CharName, LoadedJson):
        self.root = GUI('root', 'TibiaAuto V12')
        self.root.MainWindow('Main', [357, 530], [2, 2.36])

        self.root.addMinimalLabel(f'Logged as: {CharName}', [14, 14])

        # regions Buttons

        self.root.addButton('Healer Friend', OpenHealerFriend, [92, 23], [23, 56])
        self.root.addButton('Color Change', OpenColorChange, [92, 23], [23, 108])
        self.root.addButton('Ammo Restack', OpenAmmoRestack, [92, 23], [23, 135])
        self.root.addButton('Auto Looter', OpenAutoLooter, [92, 23], [23, 160])

        self.root.addButton('Food Eater', OpenFoodEater, [92, 23], [23, 210])
        self.root.addButton('Auto Grouping', OpenAutoGrouping, [92, 23], [23, 236])
        self.root.addButton('Sort Loot', OpenSortLoot, [92, 23], [23, 262])
        self.root.addButton('Auto Banker', OpenAutoBanker, [92, 23], [23, 288])
        self.root.addButton('Auto Seller', OpenAutoSeller, [92, 23], [23, 340])
        self.root.addButton('FPS Changer', OpenFPSChanger, [92, 23], [23, 366])

        self.root.addButton('Auto Life', OpenAutoHeal, [92, 23], [147, 56])
        self.root.addButton('Auto Hur', OpenAutoHur, [92, 23], [245, 56])
        self.root.addButton('Auto Mana', OpenAutoMana, [92, 23], [147, 83])
        self.root.addButton('Auto Fish', OpenAutoFish, [92, 23], [245, 83])
        self.root.addButton('Auto Amulet', OpenAutoSSA, [92, 23], [147, 108])
        self.root.addButton('Auto Ring', OpenAutoRing, [92, 23], [245, 108])
        self.root.addButton('Timed Spells', OpenTimedSpells, [92, 23], [147, 135])
        self.root.addButton('Auto Login', OpenAutoLogin, [92, 23], [245, 135])

        self.root.addButton('Creature Info', OpenCreatureInfo, [92, 23], [147, 188])
        self.root.addButton('Monsters', OpenMonsters, [92, 23], [245, 188])

        self.root.addButton('Show Map', OpenShowMap, [92, 23], [147, 290])
        self.root.addButton('Cave Bot', OpenCaveBot, [92, 23], [245, 290])

        self.root.addButton('Load Config', OpenLoadConfig, [92, 23], [147, 340])
        self.root.addButton('Save Config', OpenSaveConfig, [92, 23], [245, 340])
        self.root.addButton('Adjust Config', OpenAdjustConfig, [92, 23], [147, 366])
        self.root.addButton('Modules', OpenModules, [92, 23], [245, 366])
        self.root.addButton('Python Scripts', OpenPythonScripts, [92, 23], [245, 392])

        self.root.addButton('General Options', OpenGeneralOptions, [213, 23], [134, 426])

        def Exit():
            print("Exiting...")
            self.root.destroyWindow()

        self.root.addButton('Exit', Exit, [92, 23], [10, 498])

        # endregion

        '''
            This Functions Is Called From Line 189, As Soon As Window Is Loaded.
            
            It Sets For Program, The Variables Loaded From The Script You Chose,
            So That It Can Pass To The Modules That Are Opened.
        '''

        def SetVariablesFromLoadedJson():
            global SETTED_VARIABLES
            if not SETTED_VARIABLES:
                with open('Scripts/' + LoadedJson + '.json', 'r') as LoadsJson:
                    data = json.load(LoadsJson)

                global MOUSE_OPTION
                MOUSE_OPTION = data['MouseOption']
                if MOUSE_OPTION == 0:
                    print("Your Mouse Option Is: Send Events To Client")
                else:
                    print("Your Mouse Option Is: Movement Mouse")

                if data['Positions']['LifePosition'][0]['Stats']:
                    HealthLocation[0] = data['Positions']['LifePosition'][0]['x']
                    HealthLocation[1] = data['Positions']['LifePosition'][0]['y']
                if data['Positions']['ManaPosition'][0]['Stats']:
                    ManaLocation[0] = data['Positions']['ManaPosition'][0]['x']
                    ManaLocation[1] = data['Positions']['ManaPosition'][0]['y']
                if data['Boxes']['BattleBox'][0]['Stats']:
                    BattlePositions[0] = data['Boxes']['BattleBox'][0]['x'] - 3
                    BattlePositions[1] = data['Boxes']['BattleBox'][0]['y'] - 3
                    BattlePositions[2] = data['Boxes']['BattleBox'][0]['w'] + 3
                    BattlePositions[3] = data['Boxes']['BattleBox'][0]['h'] + 3
                if data['Boxes']['StatusBarBox'][0]['Stats']:
                    StatsPositions[0] = data['Boxes']['StatusBarBox'][0]['x'] - 1
                    StatsPositions[1] = data['Boxes']['StatusBarBox'][0]['y'] - 1
                    StatsPositions[2] = data['Boxes']['StatusBarBox'][0]['w']
                    StatsPositions[3] = data['Boxes']['StatusBarBox'][0]['h']
                if data['Boxes']['RingBox'][0]['Stats']:
                    RingPositions[0] = data['Boxes']['RingBox'][0]['x']
                    RingPositions[1] = data['Boxes']['RingBox'][0]['y']
                    RingPositions[2] = data['Boxes']['RingBox'][0]['w']
                    RingPositions[3] = data['Boxes']['RingBox'][0]['h']
                if data['Boxes']['AmuletBox'][0]['Stats']:
                    AmuletPositions[0] = data['Boxes']['AmuletBox'][0]['x']
                    AmuletPositions[1] = data['Boxes']['AmuletBox'][0]['y']
                    AmuletPositions[2] = data['Boxes']['AmuletBox'][0]['w']
                    AmuletPositions[3] = data['Boxes']['AmuletBox'][0]['h']
                if data['Boxes']['MapBox'][0]['Stats']:
                    MapPositions[0] = data['Boxes']['MapBox'][0]['x'] + 1
                    MapPositions[1] = data['Boxes']['MapBox'][0]['y'] + 1
                    MapPositions[2] = data['Boxes']['MapBox'][0]['w']
                    MapPositions[3] = data['Boxes']['MapBox'][0]['h'] + 1
                if data['Positions']['PlayerPosition'][0]['Stats'] and data['Boxes']['GameWindowBox'][0]['Stats']:
                    gameWindow[0] = data['Boxes']['GameWindowBox'][0]['x']
                    gameWindow[1] = data['Boxes']['GameWindowBox'][0]['y']
                    gameWindow[2] = data['Boxes']['GameWindowBox'][0]['w']
                    gameWindow[3] = data['Boxes']['GameWindowBox'][0]['h']
                    Player[0] = data['Positions']['PlayerPosition'][0]['x']
                    Player[1] = data['Positions']['PlayerPosition'][0]['y']
                if data['SQM']['SQM1'][0]['Stats'] and data['SQM']['SQM2'][0]['Stats'] and data['SQM']['SQM3'][0][
                    'Stats'] and data['SQM']['SQM4'][0]['Stats'] and data['SQM']['SQM5'][0]['Stats'] and data['SQM'][
                    'SQM6'][0]['Stats'] and data['SQM']['SQM7'][0]['Stats'] and data['SQM']['SQM8'][0][
                    'Stats'] and data['SQM']['SQM9'][0]['Stats']:
                    SQMs[0] = data['SQM']['SQM1'][0]['x']
                    SQMs[1] = data['SQM']['SQM1'][0]['y']
                    SQMs[2] = data['SQM']['SQM2'][0]['x']
                    SQMs[3] = data['SQM']['SQM2'][0]['y']
                    SQMs[4] = data['SQM']['SQM3'][0]['x']
                    SQMs[5] = data['SQM']['SQM3'][0]['y']
                    SQMs[6] = data['SQM']['SQM4'][0]['x']
                    SQMs[7] = data['SQM']['SQM4'][0]['y']
                    SQMs[8] = data['SQM']['SQM5'][0]['x']
                    SQMs[9] = data['SQM']['SQM5'][0]['y']
                    SQMs[10] = data['SQM']['SQM6'][0]['x']
                    SQMs[11] = data['SQM']['SQM6'][0]['y']
                    SQMs[12] = data['SQM']['SQM7'][0]['x']
                    SQMs[13] = data['SQM']['SQM7'][0]['y']
                    SQMs[14] = data['SQM']['SQM8'][0]['x']
                    SQMs[15] = data['SQM']['SQM8'][0]['y']
                    SQMs[16] = data['SQM']['SQM9'][0]['x']
                    SQMs[17] = data['SQM']['SQM9'][0]['y']

                global MainPath, ItemsPath, ChestsPath, ContainersNamePath, CavebotScriptsPath
                MainPath = data["Paths"]["MainPath"]
                ItemsPath = data["Paths"]["ItemsPath"]
                ChestsPath = data["Paths"]["ChestsPath"]
                ContainersNamePath = data["Paths"]["ContainersNamePath"]
                CavebotScriptsPath = data["Paths"]["CavebotScriptsPath"]

                SETTED_VARIABLES = True

        SetVariablesFromLoadedJson()

        self.root.loop()


'''
    Functions For Open The Modules, Passing The Arguments Necessary Loaded From The Script.
'''

# region Functions


def OpenAdjustConfig():
    print("AdjustConfig In Development...")
    # AdjustConfig(root)


def OpenAmmoRestack():
    print("AmmoRestack In Development...")
    # AmmoRestack(root)


def OpenShowMap():
    print("ShowMap In Development...")
    # ShowMap(SQMs, BattlePositions)


def OpenAutoBanker():
    print("AutoBanker In Development...")
    # AutoBanker(root)


def OpenAutoFish():
    print("AutoFish In Development...")
    # AutoFish(root)


def OpenAutoGrouping():
    print("AutoGroupin In Development...")
    # AutoGrouping(root)


def OpenAutoHeal():
    AutoHeal(HealthLocation, MOUSE_OPTION)


def OpenAutoHur():
    AutoHur(StatsPositions, MOUSE_OPTION)


def OpenAutoLogin():
    print("AutoLogin In Development...")
    # AutoLogin(root)


def OpenAutoLooter():
    print("AutoLooter In Development...")
    # AutoLooter(Player, SQMs)


def OpenAutoMana():
    AutoMana(ManaLocation, MOUSE_OPTION)


def OpenAutoRing():
    AutoRing(root, RingPositions, HealthLocation, MOUSE_OPTION, ItemsPath)


def OpenAutoSeller():
    print("AutoSeller In Development...")
    # AutoSeller(root)


def OpenAutoSSA():
    AutoSSA(root, AmuletPositions, HealthLocation, MOUSE_OPTION)


def OpenCaveBot():
    CaveBot(MapPositions, BattlePositions, SQMs, MOUSE_OPTION)


def OpenColorChange():
    print("ColorChange In Development...")
    # ColorChange(Player)


def OpenCreatureInfo():
    print("CreatureInfo In Development...")
    # CreatureInfo(root)


def OpenFoodEater():
    print("FoodEater In Development...")
    # FoodEater(root)


def OpenFPSChanger():
    print("FPSChanger In Development...")
    # FPSChanger(root)


def OpenGeneralOptions():
    print("GeneralOption In Development...")
    # GeneralOptions(root)


def OpenHealerFriend():
    print("HealerFriend In Development...")
    # HealerFriend(root)


def OpenLoadConfig():
    print("LoadConfig In Development...")
    # LoadConfig(root)


def OpenModules():
    print("Modules In Development...")
    # Modules(root)


def OpenMonsters():
    print("Monsters In Development...")
    # Monsters(root)


def OpenPythonScripts():
    print("PythonScripts In Development...")
    # PythonScripts(root)


def OpenSaveConfig():
    print("SaveConfig In Development...")
    # SaveConfig(root)


def OpenSortLoot():
    print("SortLoot In Development...")
    # SortLoot(root)


def OpenTimedSpells():
    print("TimedSpells In Development...")
    # TimedSpells(root)

# endregion
