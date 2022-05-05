import os
import shutil
import time
import json
import pygetwindow

from conf.conf_manager import ConfManager
from core.GUI import *
from core.Getters import *
from modules.Root import root

conf = ConfManager.get('conf.json')

items_square = 32
number_of_exceptions = []

RingPositions = [0, 0, 0, 0]
AmuletPositions = [0, 0, 0, 0]


class ChooseConfig:
    """
    windows are now created from GUI.py on 'core' folder.
    """

    def __init__(self, selected_window_name):
        self.window = GUI('ChooseConfig', 'Choose your config')
        self.window.MainWindow('Config', [414, 202], [2, 2.36])

        '''
            This Is The Main Function If The ChooseConfig...
            
            He Is Called When The Player Click On 'Load' Or 'Create' Button.
        '''

        def bootstrap():
            """
            When This Function Is Called, He Takes A Name From EntryBox, 
            To Do Some Checks In The File.
            
            If The File Already Exist, He Just Throws You For Root Window
            Because You Already Configure Your File.
            
            Else He Creates One File With The Name Got And Starts The Configuration
            """

            preferences_name = f'{NameCreateJson.get()}.json'
            preferences_path = f'scripts/{preferences_name}'

            if os.path.isfile(preferences_path):
                preferences = ConfManager.get(preferences_name)

                time.sleep(.5)

                print('')
                print('Your Configure Stats:', preferences['Stats'])

                if preferences['MouseOption'] != MouseMode.get():
                    preferences['MouseOption'] = MouseMode.get()
                    with open(preferences_path, 'w') as wJson:
                        json.dump(preferences, wJson, indent=4)

                pyautogui.PAUSE = 0.005

                if preferences['Stats']:
                    print("\nOpening TibiaAuto...")
                    self.window.destroyWindow()
                    time.sleep(0.1)
                    root(selected_window_name, preferences_name)
                else:
                    os.remove(preferences_path)
                    bootstrap()
                
                return

            '''
                Here, He Copy The Base To Default Configuration,
                
                After The Copy, He Starts The Search For Configurations,
                You Can See The Progress On Console,
                If You Dont Have Any Error, It Takes, Usually Around 4 or 5 seconds
                For Complete The Configuration
                
                I recommended You, If You Dont Have Any Errors In The Configuration,
                Save Your Configuration File In Other Folder, Because If You
                Download Another Actualization In The Github, You Can Throw The 
                Files, To Not Have Configure Again.
            '''

            print('Coping Default Json')
            start_configuration = time.time()
            Directory = os.getcwd()

            shutil.copyfile(Directory + '\\Scripts' + '\\Json.json',
                            os.path.join(Directory + '\\Scripts' + '\\' + NameCreateJson.get() + '.json'))

            TibiaAuto = pygetwindow.getWindowsWithTitle("Choose your config")[0]
            TibiaAuto.minimize()

            pyautogui.PAUSE = 0.005

            time.sleep(.8)

            with open(preferences_path, 'r') as LoadedJson:
                preferences = json.load(LoadedJson)

            time.sleep(.5)
            time.sleep(.5)

            try:
                HealthLocation = GetHealthPosition()
                print('')
                print(f"Health Location [X: {HealthLocation[0]} Y: {HealthLocation[1]}]")
                preferences['Positions']['LifePosition'][0]['x'] = HealthLocation[0]
                preferences['Positions']['LifePosition'][0]['y'] = HealthLocation[1]
                preferences['Positions']['LifePosition'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('Helth Position Error')
                preferences['Positions']['LifePosition'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("LifePosition")

                pass

            try:
                ManaLocation = GetManaPosition()
                print('')
                print(f"Mana Location [X: {ManaLocation[0]} Y: {ManaLocation[1]}]")
                print('')
                preferences['Positions']['ManaPosition'][0]['x'] = ManaLocation[0]
                preferences['Positions']['ManaPosition'][0]['y'] = ManaLocation[1]
                preferences['Positions']['ManaPosition'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('Mana Position Error')
                preferences['Positions']['ManaPosition'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("ManaPosition")

                pass

            try:
                BattlePositions[0], BattlePositions[1], BattlePositions[2], BattlePositions[3] = GetBattlePosition()
                if BattlePositions[0] and BattlePositions[1] and BattlePositions[2] and BattlePositions[3] != 0:
                    print(f"Battle Location [X: {BattlePositions[0]} Y: {BattlePositions[1]}]")
                    preferences['Positions']['BattlePosition'][0]['x'] = BattlePositions[0]
                    preferences['Positions']['BattlePosition'][0]['y'] = BattlePositions[1]
                    preferences['Positions']['BattlePosition'][0]['Stats'] = True
                    time.sleep(.4)
                    preferences['Boxes']['BattleBox'][0]['x'] = int(BattlePositions[0])
                    preferences['Boxes']['BattleBox'][0]['y'] = int(BattlePositions[1])
                    preferences['Boxes']['BattleBox'][0]['w'] = int(BattlePositions[2])
                    preferences['Boxes']['BattleBox'][0]['h'] = int(BattlePositions[3])
                    preferences['Boxes']['BattleBox'][0]['Stats'] = True
                    with open(preferences_path, 'w') as wJson:
                        json.dump(preferences, wJson, indent=4)
                else:
                    raise Exception
            except Exception:
                print('Battle Position Error')
                preferences['Positions']['BattlePosition'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("BattlePosition")

                pass

            try:
                StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3] = GetStatsPosition()
                print('')
                print(f"Status Bar Start [X: {StatsPositions[0]}, Y: {StatsPositions[1]}]")
                print(f"Status Bar End [X: {StatsPositions[2]}, Y: {StatsPositions[3]}]")
                print('')
                time.sleep(.2)
                preferences['Boxes']['StatusBarBox'][0]['x'] = int(StatsPositions[0])
                preferences['Boxes']['StatusBarBox'][0]['y'] = int(StatsPositions[1])
                preferences['Boxes']['StatusBarBox'][0]['w'] = int(StatsPositions[2])
                preferences['Boxes']['StatusBarBox'][0]['h'] = int(StatsPositions[3])
                preferences['Boxes']['StatusBarBox'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('Status Bar Error')
                preferences['Boxes']['StatusBarBox'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("StatusBarBox")

                pass

            try:
                RingPositions[0], RingPositions[1] = StatsPositions[0], StatsPositions[1] - 58
                RingPositions[2] = RingPositions[0] + items_square - 1
                RingPositions[3] = RingPositions[1] + items_square - 1
                print(f"Ring's Square Start [X: {RingPositions[0]}, Y: {RingPositions[1]}]")
                print(f"Ring's Square End [X: {RingPositions[2]}, Y: {RingPositions[3]}]")
                print('')
                time.sleep(.2)
                preferences['Boxes']['RingBox'][0]['x'] = int(RingPositions[0])
                preferences['Boxes']['RingBox'][0]['y'] = int(RingPositions[1])
                preferences['Boxes']['RingBox'][0]['w'] = int(RingPositions[2])
                preferences['Boxes']['RingBox'][0]['h'] = int(RingPositions[3])
                preferences['Boxes']['RingBox'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('RingPosition Error')
                preferences['Boxes']['RingBox'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("RingBox")

                pass

            try:
                AmuletPositions[0], AmuletPositions[1] = StatsPositions[0], StatsPositions[1] - 130
                AmuletPositions[2] = AmuletPositions[0] + items_square - 1
                AmuletPositions[3] = AmuletPositions[1] + items_square - 1
                print(f"Amulet's Square Start [X: {AmuletPositions[0]}, Y: {AmuletPositions[1]}]")
                print(f"Amulet's Square End [X: {AmuletPositions[2]}, Y: {AmuletPositions[3]}]")
                print('')
                time.sleep(.2)
                preferences['Boxes']['AmuletBox'][0]['x'] = int(AmuletPositions[0])
                preferences['Boxes']['AmuletBox'][0]['y'] = int(AmuletPositions[1])
                preferences['Boxes']['AmuletBox'][0]['w'] = int(AmuletPositions[2])
                preferences['Boxes']['AmuletBox'][0]['h'] = int(AmuletPositions[3])
                preferences['Boxes']['AmuletBox'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('AmuletPosition Error')
                preferences['Boxes']['AmuletBox'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("AmuletBox")

                pass

            try:
                MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3] = GetMapPosition()
                time.sleep(.2)
                preferences['Boxes']['MapBox'][0]['x'] = int(MapPositions[0])
                preferences['Boxes']['MapBox'][0]['y'] = int(MapPositions[1])
                preferences['Boxes']['MapBox'][0]['w'] = int(MapPositions[2])
                preferences['Boxes']['MapBox'][0]['h'] = int(MapPositions[3])
                preferences['Boxes']['MapBox'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('MapPosition Error')
                preferences['Boxes']['MapBox'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("MapBox")

                pass

            try:
                Player[0], Player[1], GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[
                    3] = GetPlayerPosition()
                print('')
                print(f"Player Position [X: {Player[0]}, Y: {Player[1]}]")
                print('')
                print(f"Game Window Start [X: {GameWindow[0]}, Y: {GameWindow[1]}]")
                print(f"Game Window End [X: {GameWindow[2]}, Y: {GameWindow[3]}]")
                print('')
                time.sleep(.2)
                preferences['Positions']['PlayerPosition'][0]['x'] = Player[0]
                preferences['Positions']['PlayerPosition'][0]['y'] = Player[1]
                preferences['Positions']['PlayerPosition'][0]['Stats'] = True
                preferences['Boxes']['GameWindowBox'][0]['x'] = int(GameWindow[0])
                preferences['Boxes']['GameWindowBox'][0]['y'] = int(GameWindow[1])
                preferences['Boxes']['GameWindowBox'][0]['w'] = int(GameWindow[2])
                preferences['Boxes']['GameWindowBox'][0]['h'] = int(GameWindow[3])
                preferences['Boxes']['GameWindowBox'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('Player Position Error')
                preferences['Positions']['PlayerPosition'][0]['Stats'] = False
                preferences['Boxes']['GameWindowBox'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("PlayerPosition")
                number_of_exceptions.append("GameWindowBox")

                pass

            try:
                SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], SQMs[7], SQMs[8], SQMs[9], SQMs[10], \
                SQMs[
                    11], SQMs[12], SQMs[13], SQMs[14], SQMs[15], SQMs[16], SQMs[17] = SetSQMs()
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
                preferences['SQM']['SQM1'][0]['x'] = int(SQMs[0])
                preferences['SQM']['SQM1'][0]['y'] = int(SQMs[1])
                preferences['SQM']['SQM1'][0]['Stats'] = True
                preferences['SQM']['SQM2'][0]['x'] = int(SQMs[2])
                preferences['SQM']['SQM2'][0]['y'] = int(SQMs[3])
                preferences['SQM']['SQM2'][0]['Stats'] = True
                preferences['SQM']['SQM3'][0]['x'] = int(SQMs[4])
                preferences['SQM']['SQM3'][0]['y'] = int(SQMs[5])
                preferences['SQM']['SQM3'][0]['Stats'] = True
                preferences['SQM']['SQM4'][0]['x'] = int(SQMs[6])
                preferences['SQM']['SQM4'][0]['y'] = int(SQMs[7])
                preferences['SQM']['SQM4'][0]['Stats'] = True
                preferences['SQM']['SQM5'][0]['x'] = int(SQMs[8])
                preferences['SQM']['SQM5'][0]['y'] = int(SQMs[9])
                preferences['SQM']['SQM5'][0]['Stats'] = True
                preferences['SQM']['SQM6'][0]['x'] = int(SQMs[10])
                preferences['SQM']['SQM6'][0]['y'] = int(SQMs[11])
                preferences['SQM']['SQM6'][0]['Stats'] = True
                preferences['SQM']['SQM7'][0]['x'] = int(SQMs[12])
                preferences['SQM']['SQM7'][0]['y'] = int(SQMs[13])
                preferences['SQM']['SQM7'][0]['Stats'] = True
                preferences['SQM']['SQM8'][0]['x'] = int(SQMs[14])
                preferences['SQM']['SQM8'][0]['y'] = int(SQMs[15])
                preferences['SQM']['SQM8'][0]['Stats'] = True
                preferences['SQM']['SQM9'][0]['x'] = int(SQMs[16])
                preferences['SQM']['SQM9'][0]['y'] = int(SQMs[17])
                preferences['SQM']['SQM9'][0]['Stats'] = True
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)
            except Exception:
                print('SQMs Error')
                preferences['SQM']['SQM1'][0]['Stats'] = False
                preferences['SQM']['SQM2'][0]['Stats'] = False
                preferences['SQM']['SQM3'][0]['Stats'] = False
                preferences['SQM']['SQM4'][0]['Stats'] = False
                preferences['SQM']['SQM5'][0]['Stats'] = False
                preferences['SQM']['SQM6'][0]['Stats'] = False
                preferences['SQM']['SQM7'][0]['Stats'] = False
                preferences['SQM']['SQM8'][0]['Stats'] = False
                preferences['SQM']['SQM9'][0]['Stats'] = False
                with open(preferences_path, 'w') as wJson:
                    json.dump(preferences, wJson, indent=4)

                number_of_exceptions.append("SQM'sPositionError")

                pass

            preferences['MouseOption'] = MouseMode.get()
            with open(preferences_path, 'w') as wJson:
                json.dump(preferences, wJson, indent=4)

            preferences['ItemsMode'] = ItemsMode.get()
            with open(preferences_path, 'w') as wJson:
                json.dump(preferences, wJson, indent=4)

            # Paths Setter
            from conf.Constants import MainPath, ChestsPath, CavebotScriptsPath, ContainersNamePath

            preferences['Paths']['MainPath'] = MainPath

            if ItemsMode.get() == "Frames":
                from conf.Constants import FramesItemsPath

                preferences['Paths']['ItemsPath'] = FramesItemsPath
            elif ItemsMode.get() == "Corners":
                from conf.Constants import CornersItemsPath

                preferences['Paths']['ItemsPath'] = CornersItemsPath
            elif ItemsMode.get() == "None":
                from conf.Constants import NoneItemsPath

                preferences['Paths']['ItemsPath'] = NoneItemsPath

            preferences['Paths']['ChestsPath'] = ChestsPath
            preferences['Paths']['ContainersNamePath'] = ContainersNamePath
            preferences['Paths']['CavebotScriptsPath'] = CavebotScriptsPath

            ConfManager.set(preferences, preferences_name)

            if len(number_of_exceptions) != 0:
                print("\nSome Errors Occurred... Opening The Manual Config.")

                print("Unfortunately, You Will Have To Manually Configure The Following Errors:\n")

                time.sleep(.3)
                self.window.destroyWindow()
                time.sleep(.1)

                def ManualConfig(ErrorName):
                    ManualConfiguration = GUI('ManualConfiguration', 'Manual Configuration')
                    ManualConfiguration.MainWindow('Config', [414, 202], [2, 2.36])

                    def Solving():
                        ManualConfiguration.destroyWindow()
                        return True

                    '''LabelError = ManualConfiguration.addLabel("Solving Manually: " + ErrorName, [85, 31])
                    LabelError.configure(font=24)'''

                    ManualConfiguration.addMinimalLabel("One Error Was Occured In: " + ErrorName, [35, 31], 10)
                    ManualConfiguration.addMinimalLabel("... But This Option Is In Development.", [35, 51])

                    ManualConfiguration.addButton('Ok', Solving, [75, 23], [310, 166])

                    ManualConfiguration.Protocol(Solving)
                    ManualConfiguration.loop()

                for i in range(len(number_of_exceptions)):
                    print("Error[" + str(i + 1) + "] =", number_of_exceptions[i])

                for i in range(len(number_of_exceptions)):
                    ManualConfig(number_of_exceptions[i])

                print("\nExiting Of The Program... Please Solve The Errors")

                exit(1)

            preferences['Stats'] = True

            ConfManager.set(preferences, preferences_name)

            conf['configured'] = True
            conf['preferences_name'] = preferences_name
            ConfManager.set(conf, 'conf.json')

            end_configuration = time.time() - start_configuration
            print('')
            print(f"Your Setup Time Is: {end_configuration:.2f} Seconds")
            print('')

            print("Opening TibiaAuto...\n")

            time.sleep(.3)
            self.window.destroyWindow()
            time.sleep(.1)

            '''
                If Dont Have Any Error, He Throw You For The Root Window, In The 'Modules'
                In the 'Root.py' File.
            '''

            root(selected_window_name, preferences_name)

        # region Valiables

        NameCreateJson = tk.StringVar()
        NameCreateJson.set('NewConfig')
        CheckAuto = tk.BooleanVar()
        CheckAuto.set(True)
        MouseMode = tk.IntVar()
        MouseMode.set(1)
        HookMode = tk.IntVar()
        HookMode.set(1)
        ItemsMode = tk.StringVar()
        ItemsMode.set("Frames")

        # endregion

        # region Buttons

        self.window.addButton('Create', bootstrap, [75, 23], [310, 166])

        self.window.addEntry([165, 35], NameCreateJson, 28)

        self.window.addLabel('Name Of The Json Conf', [24, 35])

        LabelSelectOP1 = self.window.addLabel('Select Your Mouse And Keyboard Option', [30, 76])
        LabelSelectOP1.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioMouseMoviment = self.window.addRadio('{Global} Movement Mouse On Focused Window', MouseMode, 1,
                                                        [10, 95])
        RadioMouseMoviment.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                     selectcolor=rgb((114, 94, 48)))
        RadioSenderMouse = self.window.addRadio("{OTServer} Send Mouse Events To Tibia's Window", MouseMode, 0,
                                                      [10, 114])
        RadioSenderMouse.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                   selectcolor=rgb((114, 94, 48)))

        LabelSelectOP2 = self.window.addLabel('Select Your Hook Mode', [30, 136])
        LabelSelectOP2.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioHookWindow = self.window.addRadio("{Global} Hook Directly OBS Screen", HookMode, 1, [10, 155])
        RadioHookWindow.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                  selectcolor=rgb((114, 94, 48)))

        LabelSelectOP3 = self.window.addLabel('Select The Items Mode', [280, 76])
        LabelSelectOP3.configure(bg=rgb((114, 94, 48)), fg='black')

        RadioFrames = self.window.addRadio('Frames', ItemsMode, "Frames",
                                                 [310, 95])
        RadioFrames.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                              selectcolor=rgb((114, 94, 48)))
        RadioCorners = self.window.addRadio("Corners", ItemsMode, "Corners",
                                                  [310, 114])
        RadioCorners.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                               selectcolor=rgb((114, 94, 48)))
        RadioNone = self.window.addRadio("None", ItemsMode, "None",
                                               [310, 133])
        RadioNone.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                            selectcolor=rgb((114, 94, 48)))

        # endregion

        self.window.loop()
