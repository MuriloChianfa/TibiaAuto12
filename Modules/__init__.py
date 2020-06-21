import time
import json
import os
import threading
from random import randint

from Conf.WindowTitles import *
from Core.GUI import *
from Core.GetHWND import GetHWND
from Modules.ChooseConfig import ChooseConfig

from Modules.Root import root

Discovered = False
data = None

'''
    Starts The Interface For Your Visualization.
'''


def WindowSelectCharacter():
    SelectCharacter = tk.Tk()
    w = 260
    h = 90
    sw = SelectCharacter.winfo_screenwidth()
    sh = SelectCharacter.winfo_screenheight()
    x = (sw - w) / 2.3
    y = (sh - h) / 2.4
    SelectCharacter.geometry('%dx%d+%d+%d' % (w, h, x, y))
    SelectCharacter.resizable(width=False, height=False)
    SelectCharacter.title('Choose Your Character')
    SelectCharacter.configure(background=rgb((120, 98, 51)), takefocus=True)
    SelectCharacter.iconbitmap('images/icone2.ico')

    CHARACTERS = [""]

    print('\033[33m' + "Start in 1 Seconds...")

    '''
        This Function Is Called From Line 217...
        
        These Functions Need To Be Started With Threads For 
        Dont Interfere On Main Process With The Interface... 
        
        =] 
    '''

    def Searcher():
        time.sleep(.1)
        global Discovered, data
        while not Discovered:
            try:
                # A Loop For Search Your Character Name In Conf, On The WindowTitles.py
                TibiaName = FindTibiaTitle()
                TibiaCharacter = TibiaName.split(' - ')

                '''
                    If TibiaCharacter Received Anyway From TibiaName, He Generate One
                    Aleatory Number For Set On Your Character And Write In Loads.json, The
                    HWND Number Of Your Tibia Window.
                '''

                if TibiaCharacter:
                    Discovered = True
                    NumberOfTheClient = str(randint(1000, 9999))
                    CHARACTERS[0] = '[' + NumberOfTheClient + '] ' + TibiaCharacter[1]
                    Char.set(CHARACTERS[0])
                    print(CHARACTERS[0])
                    try:
                        hwnd = GetHWND('Tibia - ')
                        with open('Scripts/Loads.json', 'r') as LoadsJson:
                            data = json.load(LoadsJson)

                        print('You Current Tibia HWND: ', hwnd)

                        data['hwnd'] = hwnd
                        with open('Scripts/Loads.json', 'w') as wJson:
                            json.dump(data, wJson, indent=4)
                    except Exception as Ex:
                        print(Ex, ' ? O.O ')
                        exit(1)

                    '''
                        If Dont Have Any Error, He Write On ComboBox, The Name Of Your Character
                        This, Interrupts The Loop, And Wait The Player Select A Conf Option...
                    '''

                    # Write On ComboBox Your Character
                    OptionSelectCharacter.configure(*CHARACTERS[0])

                    '''
                        Now, If The Player Select:
                        
                        The Configure Button, He Throw You For Function On Line 151
                        The Reconfigure Button, He Throw You For Function On Line 119
                        The Exit Button, He Throw You For Function On Line 104
                    '''

                    break

            except Exception:
                pass

    def exiting():
        print("Exiting...")
        try:
            SelectCharacter.destroy()
        except Exception as Ex:
            print(Ex)
            exit(0)

    '''
        The Reconfigure Function, Verify If Already Exist One File
        With The Name Placed On Loads.Json.
        
        If Already Have One Archive, He Destroy The Archive And Restart The Program.
    '''

    def Reconfigure():
        ScriptName = data['ScriptName']

        if os.path.isfile('Scripts/' + ScriptName + '.json'):
            data['Auto'] = False
            data['ScriptName'] = None
            with open('Scripts/Loads.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)
            os.remove('Scripts/' + ScriptName + '.json')
            global Discovered
            Discovered = False
            CHARACTERS[0] = ""
            time.sleep(.2)
            ThreadSearcher.join()
            SelectCharacter.destroy()
            time.sleep(.4)
            from StartBot import main
            main()

    '''
        This Function Is Called When Player Click On 'Configure Button', or 'Load Up Button',
        If Dont Have One Character On Your ComboBox, He Just Ignore And Waits
        The Player Enter With One Character In The Tibia Client.
        
        Otherwise If The Player Have Already Logon, He Verify On Loads.Json,
        If The Status == True:
            He Verify The Name Of Script Placed On Loads.json
            If Exist, He Throw You For Root Window, In The 'Modules' Folder In The 'Root.py'
        If The Status == False:
            He Throw You For ChooseConfig Window In The 'Modules' Folder In The 'ChooseConfig.py'
    '''

    def ReadyToConfig():
        global data
        if CHARACTERS[0] != '':
            SelectCharacter.destroy()
            time.sleep(0.1)
            if data['Auto']:
                ScriptName = data['ScriptName']
                if os.path.isfile('Scripts/' + ScriptName + '.json'):
                    root(CHARACTERS[0], ScriptName)
                else:
                    print("File Not Loaded")
                    exiting()
            else:
                ChooseConfig(CHARACTERS[0])
        else:
            print('Please, Login First')

    Char = tk.StringVar()
    Char.set(CHARACTERS[0])

    OptionSelectCharacter = tk.OptionMenu(SelectCharacter, Char, *CHARACTERS)
    OptionSelectCharacter.configure(anchor='w')
    OptionSelectCharacter.pack()
    OptionSelectCharacter.place(w=230, h=24, x=15, y=17)

    with open('Scripts/Loads.json', 'r') as LoadsJson:
        data = json.load(LoadsJson)

    # region Buttons

    if data['Auto']:
        ConfigButton = tk.Button(SelectCharacter, width=15, text="Load Up", command=ReadyToConfig, bg=rgb((127, 17, 8)),
                                 fg='white',
                                 activebackground=rgb((123, 13, 5)))
        ConfigButton.pack()
        ConfigButton.place(w=85, h=25, x=140, y=53)
    else:
        ConfigButton = tk.Button(SelectCharacter, width=15, text="Configure", command=ReadyToConfig,
                                 bg=rgb((127, 17, 8)),
                                 fg='white',
                                 activebackground=rgb((123, 13, 5)))
        ConfigButton.pack()
        ConfigButton.place(w=85, h=25, x=140, y=53)

    if data['Auto']:
        ExitButton = tk.Button(SelectCharacter, width=15, text="Reconfigure", command=Reconfigure, bg=rgb((127, 17, 8)),
                               fg='white',
                               activebackground=rgb((123, 13, 5)))
    else:
        ExitButton = tk.Button(SelectCharacter, width=15, text="Exit", command=exiting, bg=rgb((127, 17, 8)),
                               fg='white',
                               activebackground=rgb((123, 13, 5)))

    ExitButton.pack()
    ExitButton.place(w=85, h=25, x=28, y=53)

    # endregion

    '''
        This Thread Start The Function Searcher In Other Thread For Dont
        Disturb The Interface Thread...
        
        If The Thread Already Alive, He Pass, Used If The Player Click In Reconfigure Button.
        Else Init The Thread.
    '''

    ThreadSearcher = threading.Thread(target=Searcher)
    if ThreadSearcher.is_alive():
        pass
    else:
        ThreadSearcher.start()

    SelectCharacter.mainloop()
