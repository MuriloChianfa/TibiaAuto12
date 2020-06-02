import os
import shutil
import time
import json
import pygetwindow

from Engine.GUI import *

from Core.GetPlayerPosition import GetPlayerPosition
from Core.GetManaPosition import GetManaPosition
from Core.GetHealthPosition import GetHealthPosition
from Core.GetMapPosition import GetMapPosition
from Core.GetBattlePosition import GetBattlePosition
from Core.GetStatsPosition import GetStatsPosition

from Conf.SetSQMsPositions import SetSQMs
from Modules.Root import root


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


class Errno(Exception):
    pass


class ChooseConfig:
    def __init__(self, CharName):
        self.ChooseConfig = GUI('ChooseConfig', 'Choose You Config')
        self.ChooseConfig.MainWindow('Config', [414, 202], [2, 2.36])

        def CreateDefaultJson():
            ScriptToLoad = NameCreateJson.get()
            if os.path.isfile('Scripts/' + 'Scripts/' + ScriptToLoad + '.json'):
                with open('Scripts/' + 'Scripts/' + ScriptToLoad + '.json', 'r') as LoadsJson:
                    data = json.load(LoadsJson)

                time.sleep(.5)

                print('')
                print('Your Configure Stats:', data['Stats'])

                if data['MouseOption'] != MouseMode.get():
                    data['MouseOption'] = MouseMode.get()
                    with open('Scripts/' + 'Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                pyautogui.PAUSE = 0.005

                if data['Stats']:
                    print("\nOpening TibiaAuto...")
                    self.ChooseConfig.destroyWindow()
                    time.sleep(0.1)
                    root(CharName, ScriptToLoad)
                else:
                    os.remove('Scripts/' + 'Scripts/' + ScriptToLoad + '.json')
                    CreateDefaultJson()
            else:
                print('Coping Default Json')
                start_configuration = time.time()
                Directory = os.getcwd()

                shutil.copyfile(Directory + '\\Scripts' + '\\Json.json', os.path.join(Directory + '\\Scripts' + '\\' + NameCreateJson.get() + '.json'))

                TibiaAuto = pygetwindow.getWindowsWithTitle("Choose You Config")[0]
                TibiaAuto.minimize()

                pyautogui.PAUSE = 0.005

                time.sleep(.8)

                with open('Scripts/' + ScriptToLoad + '.json', 'r') as LoadsJson:
                    data = json.load(LoadsJson)

                time.sleep(.5)
                time.sleep(.5)

                if HookMode.get() == 1:
                    print("Hooking OBS")
                else:
                    print("Grabing Screen")

                try:
                    HealthLocation[0], HealthLocation[1] = GetHealthPosition(HookMode.get())
                    HealthLocation[0], HealthLocation[1] = int(HealthLocation[0]), int(HealthLocation[1])
                    print('')
                    print(f"Health Location [X: {HealthLocation[0]} Y: {HealthLocation[1]}]")
                    data['Positions']['LifePosition'][0]['x'] = HealthLocation[0]
                    data['Positions']['LifePosition'][0]['y'] = HealthLocation[1]
                    data['Positions']['LifePosition'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Helth Position Error')
                    data['Positions']['LifePosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    ManaLocation[0], ManaLocation[1] = GetManaPosition(HookMode.get())
                    ManaLocation[0], ManaLocation[1] = int(ManaLocation[0]), int(ManaLocation[1])
                    print('')
                    print(f"Mana Location [X: {ManaLocation[0]} Y: {ManaLocation[1]}]")
                    print('')
                    data['Positions']['ManaPosition'][0]['x'] = ManaLocation[0]
                    data['Positions']['ManaPosition'][0]['y'] = ManaLocation[1]
                    data['Positions']['ManaPosition'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Mana Position Error')
                    data['Positions']['ManaPosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    BattlePositions[0], BattlePositions[1], BattlePositions[2], BattlePositions[3] = GetBattlePosition(HookMode.get())
                    print(f"Battle Location [X: {BattlePositions[0]} Y: {BattlePositions[1]}]")
                    data['Positions']['BattlePosition'][0]['x'] = BattlePositions[0]
                    data['Positions']['BattlePosition'][0]['y'] = BattlePositions[1]
                    data['Positions']['BattlePosition'][0]['Stats'] = True
                    time.sleep(.4)
                    data['Boxes']['BattleBox'][0]['x'] = int(BattlePositions[0])
                    data['Boxes']['BattleBox'][0]['y'] = int(BattlePositions[1])
                    data['Boxes']['BattleBox'][0]['w'] = int(BattlePositions[2])
                    data['Boxes']['BattleBox'][0]['h'] = int(BattlePositions[3])
                    data['Boxes']['BattleBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Battle Position Error')
                    data['Positions']['BattlePosition'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3] = GetStatsPosition(HookMode.get())
                    print('')
                    print(f"Status Bar Start [X: {StatsPositions[0]}, Y: {StatsPositions[1]}]")
                    print(f"Status Bar End [X: {StatsPositions[2]}, Y: {StatsPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['StatusBarBox'][0]['x'] = int(StatsPositions[0])
                    data['Boxes']['StatusBarBox'][0]['y'] = int(StatsPositions[1])
                    data['Boxes']['StatusBarBox'][0]['w'] = int(StatsPositions[2])
                    data['Boxes']['StatusBarBox'][0]['h'] = int(StatsPositions[3])
                    data['Boxes']['StatusBarBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Status Bar Error')
                    data['Boxes']['StatusBarBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    RingPositions[0], RingPositions[1] = StatsPositions[0], StatsPositions[1] - 58
                    RingPositions[2] = RingPositions[0] + ItemsSquare - 1
                    RingPositions[3] = RingPositions[1] + ItemsSquare - 1
                    print(f"Ring's Square Start [X: {RingPositions[0]}, Y: {RingPositions[1]}]")
                    print(f"Ring's Square End [X: {RingPositions[2]}, Y: {RingPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['RingBox'][0]['x'] = int(RingPositions[0])
                    data['Boxes']['RingBox'][0]['y'] = int(RingPositions[1])
                    data['Boxes']['RingBox'][0]['w'] = int(RingPositions[2])
                    data['Boxes']['RingBox'][0]['h'] = int(RingPositions[3])
                    data['Boxes']['RingBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('RingPosition Error')
                    data['Boxes']['RingBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    AmuletPositions[0], AmuletPositions[1] = StatsPositions[0], StatsPositions[1] - 130
                    AmuletPositions[2] = AmuletPositions[0] + ItemsSquare - 1
                    AmuletPositions[3] = AmuletPositions[1] + ItemsSquare - 1
                    print(f"Amulet's Square Start [X: {AmuletPositions[0]}, Y: {AmuletPositions[1]}]")
                    print(f"Amulet's Square End [X: {AmuletPositions[2]}, Y: {AmuletPositions[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Boxes']['AmuletBox'][0]['x'] = int(AmuletPositions[0])
                    data['Boxes']['AmuletBox'][0]['y'] = int(AmuletPositions[1])
                    data['Boxes']['AmuletBox'][0]['w'] = int(AmuletPositions[2])
                    data['Boxes']['AmuletBox'][0]['h'] = int(AmuletPositions[3])
                    data['Boxes']['AmuletBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('AmuletPosition Error')
                    data['Boxes']['AmuletBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3] = GetMapPosition(HookMode.get())
                    time.sleep(.2)
                    data['Boxes']['MapBox'][0]['x'] = int(MapPositions[0])
                    data['Boxes']['MapBox'][0]['y'] = int(MapPositions[1])
                    data['Boxes']['MapBox'][0]['w'] = int(MapPositions[2])
                    data['Boxes']['MapBox'][0]['h'] = int(MapPositions[3])
                    data['Boxes']['MapBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('MapPosition Error')
                    data['Boxes']['MapBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                try:
                    Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[
                        3] = GetPlayerPosition(HookMode.get())
                    print('')
                    print(f"Player Position [X: {Player[0]}, Y: {Player[1]}]")
                    print('')
                    print(f"Game Window Start [X: {gameWindow[0]}, Y: {gameWindow[1]}]")
                    print(f"Game Window End [X: {gameWindow[2]}, Y: {gameWindow[3]}]")
                    print('')
                    time.sleep(.2)
                    data['Positions']['PlayerPosition'][0]['x'] = Player[0]
                    data['Positions']['PlayerPosition'][0]['y'] = Player[1]
                    data['Positions']['PlayerPosition'][0]['Stats'] = True
                    data['Boxes']['GameWindowBox'][0]['x'] = int(gameWindow[0])
                    data['Boxes']['GameWindowBox'][0]['y'] = int(gameWindow[1])
                    data['Boxes']['GameWindowBox'][0]['w'] = int(gameWindow[2])
                    data['Boxes']['GameWindowBox'][0]['h'] = int(gameWindow[3])
                    data['Boxes']['GameWindowBox'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('Player Position Error')
                    data['Positions']['PlayerPosition'][0]['Stats'] = False
                    data['Boxes']['GameWindowBox'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                    pass

                try:
                    SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], SQMs[7], SQMs[8], SQMs[9], SQMs[10], SQMs[
                        11], SQMs[12], SQMs[13], SQMs[14], SQMs[15], SQMs[16], SQMs[17] = SetSQMs(HookMode.get())
                    time.sleep(0.1)
                    print(f"1° SQM Location [X: {SQMs[0]}, Y: {SQMs[1]}]")
                    print(f"2° SQM Location [X: {SQMs[2]}, Y: {SQMs[3]}]")
                    print(f"3° SQM Location [X: {SQMs[4]}, Y: {SQMs[5]}]")
                    print(f"4° SQM Location [X: {SQMs[6]}, Y: {SQMs[7]}]")
                    print(f"5° SQM Location [X: {SQMs[8]}, Y: {SQMs[9]}]")
                    print(f"6° SQM Location [X: {SQMs[10]}, Y: {SQMs[11]}]")
                    print(f"7° SQM Location [X: {SQMs[12]}, Y: {SQMs[13]}]")
                    print(f"8° SQM Location [X: {SQMs[14]}, Y: {SQMs[15]}]")
                    print(f"9° SQM Location [X: {SQMs[16]}, Y: {SQMs[17]}]")
                    time.sleep(.4)
                    data['SQM']['SQM1'][0]['x'] = int(SQMs[0])
                    data['SQM']['SQM1'][0]['y'] = int(SQMs[1])
                    data['SQM']['SQM1'][0]['Stats'] = True
                    data['SQM']['SQM2'][0]['x'] = int(SQMs[2])
                    data['SQM']['SQM2'][0]['y'] = int(SQMs[3])
                    data['SQM']['SQM2'][0]['Stats'] = True
                    data['SQM']['SQM3'][0]['x'] = int(SQMs[4])
                    data['SQM']['SQM3'][0]['y'] = int(SQMs[5])
                    data['SQM']['SQM3'][0]['Stats'] = True
                    data['SQM']['SQM4'][0]['x'] = int(SQMs[6])
                    data['SQM']['SQM4'][0]['y'] = int(SQMs[7])
                    data['SQM']['SQM4'][0]['Stats'] = True
                    data['SQM']['SQM5'][0]['x'] = int(SQMs[8])
                    data['SQM']['SQM5'][0]['y'] = int(SQMs[9])
                    data['SQM']['SQM5'][0]['Stats'] = True
                    data['SQM']['SQM6'][0]['x'] = int(SQMs[10])
                    data['SQM']['SQM6'][0]['y'] = int(SQMs[11])
                    data['SQM']['SQM6'][0]['Stats'] = True
                    data['SQM']['SQM7'][0]['x'] = int(SQMs[12])
                    data['SQM']['SQM7'][0]['y'] = int(SQMs[13])
                    data['SQM']['SQM7'][0]['Stats'] = True
                    data['SQM']['SQM8'][0]['x'] = int(SQMs[14])
                    data['SQM']['SQM8'][0]['y'] = int(SQMs[15])
                    data['SQM']['SQM8'][0]['Stats'] = True
                    data['SQM']['SQM9'][0]['x'] = int(SQMs[16])
                    data['SQM']['SQM9'][0]['y'] = int(SQMs[17])
                    data['SQM']['SQM9'][0]['Stats'] = True
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                except Errno:
                    print('SQMs Error')
                    data['SQM']['SQM1'][0]['Stats'] = False
                    data['SQM']['SQM2'][0]['Stats'] = False
                    data['SQM']['SQM3'][0]['Stats'] = False
                    data['SQM']['SQM4'][0]['Stats'] = False
                    data['SQM']['SQM5'][0]['Stats'] = False
                    data['SQM']['SQM6'][0]['Stats'] = False
                    data['SQM']['SQM7'][0]['Stats'] = False
                    data['SQM']['SQM8'][0]['Stats'] = False
                    data['SQM']['SQM9'][0]['Stats'] = False
                    with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)

                data['Stats'] = True
                with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)

                data['MouseOption'] = MouseMode.get()
                with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)

                data['HookOption'] = HookMode.get()
                with open('Scripts/' + ScriptToLoad + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)

                if CheckAuto.get():
                    with open('Scripts/Loads.json', 'r') as LoaderJson:
                        data2 = json.load(LoaderJson)

                    data2['Auto'] = True
                    data2['ScriptName'] = ScriptToLoad
                    with open('Scripts/Loads.json', 'w') as wwJson:
                        json.dump(data2, wwJson, indent=4)

                end_configuration = time.time() - start_configuration
                print('')
                print(f"Your Setup Time Is: {end_configuration:.2f} Seconds")
                print('')

                print("Opening TibiaAuto...\n")

                time.sleep(.3)
                self.ChooseConfig.destroyWindow()
                time.sleep(.1)
                ScriptToLoad = NameCreateJson.get()
                root(CharName, ScriptToLoad)

        NameCreateJson = tk.StringVar()
        NameCreateJson.set('NewConfig')
        CheckAuto = tk.BooleanVar()
        CheckAuto.set(True)
        MouseMode = tk.IntVar()
        MouseMode.set(1)
        HookMode = tk.IntVar()
        HookMode.set(1)

        if os.path.isfile('Scripts/' + NameCreateJson.get() + '.json'):
            with open('Scripts/' + NameCreateJson.get() + '.json', 'r') as LoadsJson:
                data = json.load(LoadsJson)
            if data['Stats']:
                self.ChooseConfig.addButton('Load', CreateDefaultJson, [75, 23], [310, 166])
            else:
                self.ChooseConfig.addButton('Create', CreateDefaultJson, [75, 23], [310, 166])
        else:
            self.ChooseConfig.addButton('Create', CreateDefaultJson, [75, 23], [310, 166])

        self.ChooseConfig.addEntry([165, 35], NameCreateJson, 28)

        self.ChooseConfig.addLabel('Name Of The Json Conf', [24, 35])

        # RadioLoadAuto = self.ChooseConfig.addCheck(CheckAuto, [10, 114], 1, 'Load automatically This Script')
        # RadioLoadAuto.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)), selectcolor=rgb((114,
        # 94, 48)))

        LabelSelectOP1 = self.ChooseConfig.addLabel('Select Your Mouse And Keyboard Option', [30, 76])
        LabelSelectOP1.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioMouseMoviment = self.ChooseConfig.addRadio('{Global} Movement Mouse On Focused Window', MouseMode, 1, [10, 95])
        RadioMouseMoviment.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                     selectcolor=rgb((114, 94, 48)))
        RadioSenderMouse = self.ChooseConfig.addRadio("{OTServer} Send Mouse Events To Tibia's Window", MouseMode, 0,
                                                      [10, 114])
        RadioSenderMouse.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                   selectcolor=rgb((114, 94, 48)))

        LabelSelectOP2 = self.ChooseConfig.addLabel('Select Your Hook Mode', [30, 136])
        LabelSelectOP2.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioHookWindow = self.ChooseConfig.addRadio("{Global} Hook Directly OBS Screen", HookMode, 1, [10, 155])
        RadioHookWindow.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                  selectcolor=rgb((114, 94, 48)))
        RadioGrabScreen = self.ChooseConfig.addRadio('Grab Screen', HookMode, 0,
                                                     [10, 174])
        RadioGrabScreen.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                  selectcolor=rgb((114, 94, 48)))

        self.ChooseConfig.loop()
